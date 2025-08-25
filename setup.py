from cx_Freeze import setup, Executable

include_files = [
    ("backend/credenciales_Oauth.json", "backend/credenciales_Oauth.json"),
    ("backend/credenciales.json", "backend/credenciales.json"),
    ("backend/token_Oauth.json", "backend/token_Oauth.json"),
    ("recursos", "recursos")
]

setup(
    name="InventarioEC",
    version="1.0",
    description="Inventario para Economia Circular del Centro de Gestion Industrial",
    options={
        "build_exe": {
        "packages": ["httplib2"],
        "excludes": ["socks"],
        "include_files": include_files,
            }
    },
    executables=[Executable("main.py", base="Win32GUI", target_name="InventarioEC.exe", icon="icon.ico")]
)