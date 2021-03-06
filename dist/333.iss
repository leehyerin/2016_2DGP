; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{96045772-B16D-4C5A-BBED-D5296507A574}
AppName=PokemonDefense
AppVersion=1.0
;AppVerName=PokemonDefense 1.0
AppPublisher=hyerin
AppPublisherURL=https://github.com/leehyerin/2016_2DGP
AppSupportURL=https://github.com/leehyerin/2016_2DGP
AppUpdatesURL=https://github.com/leehyerin/2016_2DGP
DefaultDirName={pf}\PokemonDefense
DisableProgramGroupPage=yes
OutputDir=C:\Users\Administrator\Desktop\backup\Github
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Administrator\Desktop\backup\Github\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Administrator\Desktop\backup\Github\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\PokemonDefense"; Filename: "{app}\mygame.exe"
Name: "{commondesktop}\PokemonDefense"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,PokemonDefense}"; Flags: nowait postinstall skipifsilent

