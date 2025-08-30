; Script de Inno Setup para InventarioEC
; Basado en el setup.py de cx_Freeze

[Setup]
AppName=InventarioEC
AppVersion=1.0
AppPublisher=Centro de Gestión Industrial
AppPublisherURL=http://www.sena.edu.co
DefaultDirName={localappdata}\InventarioEC
DefaultGroupName=InventarioEC
OutputDir=C:\Users\qsouh\Documents\Python_Projects\InventarioEC\instalador
OutputBaseFilename=InventarioEC_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=C:\Users\qsouh\Documents\Python_Projects\InventarioEC\icon.ico

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Incluye todo el contenido generado por cx_Freeze
Source: "C:\Users\qsouh\Documents\Python_Projects\InventarioEC\build\Inventario Economia Circular\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

; Copiar el icono dentro de la carpeta de la aplicación
Source: "C:\Users\qsouh\Documents\Python_Projects\InventarioEC\icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Acceso directo en el menú inicio
Name: "{group}\InventarioEC"; Filename: "{app}\InventarioEC.exe"; IconFilename: "{app}\icon.ico"

; Acceso directo en el escritorio (opcional, según el Task)
Name: "{commondesktop}\InventarioEC"; Filename: "{app}\InventarioEC.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon

[Run]
; Ejecutar la app después de instalar
Filename: "{app}\InventarioEC.exe"; Description: "{cm:LaunchProgram,InventarioEC}"; Flags: nowait postinstall skipifsilent
