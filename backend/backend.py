from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
from google.oauth2.credentials import Credentials as creden
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from typing import Literal
from io import BytesIO
from PIL import Image
import numpy as np
import gspread
import os

#Define los permisos que quiere la cuenta del backend
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

#Obtiene la ruta del archivo de las credenciales
CREDENCIALES_JSON = "backend/credenciales.json"
CREDENCIALES_OAUTH_JSON = "backend/credenciales_Oauth.json"
TOKEN_OAUTH_JSON = "backend/token_Oauth.json"

#Crea un objeto de credenciales con el json
creds = Credentials.from_service_account_file(CREDENCIALES_JSON, scopes=SCOPES)

#+----------------------------------------------------------------+
#|                          GOOGLE DRIVE                          |
#+----------------------------------------------------------------+
ID_IMAGE_USERS = "1JmMGFIgYeY7p6zLM0INz_3HdPHZE1U7j"
ID_IMAGE_ITEMS_INVENTORY = "1BsfGBvHsqeTXFKZF3LKYVRPJA1ymWq-d"

def get_drive_service():
    creds = None

    # Si ya hay token guardado, usarlo
    if os.path.exists(TOKEN_OAUTH_JSON):
        creds = creden.from_authorized_user_file(TOKEN_OAUTH_JSON, SCOPES)

    # Si no hay token o está caducado, pedir autorización
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENCIALES_OAUTH_JSON, SCOPES)
            creds = flow.run_local_server(port=0)

        # Guardar token para no volver a pedir
        with open(TOKEN_OAUTH_JSON, 'w') as token:
            token.write(creds.to_json())

    return build("drive", "v3", credentials=creds)

def download_img_drive(file_id):
    service = get_drive_service()

    img_bytes = BytesIO()
    request = service.files().get_media(fileId=file_id)
    downloader = MediaIoBaseDownload(img_bytes, request)

    done = False

    while not done:
        status, done = downloader.next_chunk()

    img_bytes.seek(3)

    img = Image.open(img_bytes).convert("RGBA")

    width, height = img.size

    img_np = np.array(img).flatten() / 255.0

    return width, height, img_np

def subir_img_users(img_pillow, name):
    service = get_drive_service()

    # Convertir Pillow a bytes
    img_bytes = BytesIO()
    img_pillow.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Metadata del archivo
    metadata = {
        "name": f"{name}.png",
        "parents": [ID_IMAGE_USERS]
    }

    media = MediaIoBaseUpload(img_bytes, mimetype="image/png")

    archivo = service.files().create(
        body=metadata,
        media_body=media,
        fields="id, webViewLink"
    ).execute()

    file_id = archivo.get("id")
    direct_link = f"https://drive.google.com/uc?id={file_id}"

    return {
        "id": file_id,
        "webViewLink": archivo.get("webViewLink"),
        "direct_link": direct_link
    }

def subir_img_inventory(img_pillow, name):
    service = get_drive_service()

    # Convertir Pillow a bytes
    img_bytes = BytesIO()
    img_pillow.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Metadata del archivo
    metadata = {
        "name": f"{name}.png",
        "parents": [ID_IMAGE_ITEMS_INVENTORY]
    }

    media = MediaIoBaseUpload(img_bytes, mimetype="image/png")

    archivo = service.files().create(
        body=metadata,
        media_body=media,
        fields="id, webViewLink"
    ).execute()

    file_id = archivo.get("id")
    direct_link = f"https://drive.google.com/uc?id={file_id}"

    return {
        "id": file_id,
        "webViewLink": archivo.get("webViewLink"),
        "direct_link": direct_link
    }

#+----------------------------------------------------------------+
#|                          GOOGLE SHEETS                         |
#+----------------------------------------------------------------+

#ID de las hojas de calculo
ID_DB_SOFTWARE_EC = "1L34gdLCzks8fbVZIw6l1drNedmVh-43mjg0QYVU4hOc"

# Inicializar cliente en None
client = None
sheet_software_ec = None
worksheet_d_usuarios = None
worksheet_d_inventario = None

def init_sheets():
    global client, sheet_software_ec, worksheet_d_usuarios, worksheet_d_inventario

    try:
        client = gspread.authorize(creds)
        sheet_software_ec = client.open_by_key(ID_DB_SOFTWARE_EC)
        worksheet_d_usuarios = sheet_software_ec.worksheet("d_usuarios")
        worksheet_d_inventario = sheet_software_ec.worksheet("d_inventario")
        print("Google Sheets inicializado correctamente.")
        return True
    except Exception as e:
        print("⚠️ No se pudo conectar a Google Sheets (¿sin internet?)")
        return False

def agregar_usuario(estructura):
    worksheet_d_usuarios.append_rows(estructura)

def obtener_usuario():
    return worksheet_d_usuarios.get_all_records()

def agregar_inventario(estructura):
    worksheet_d_inventario.append_rows(estructura)

def obtener_inventario():
    return worksheet_d_inventario.get_all_records()

def eliminar_fila_inventario(idx):
    worksheet_d_inventario.delete_rows(idx)