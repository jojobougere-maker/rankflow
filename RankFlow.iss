#define MyAppName "RankFlow"
#define MyAppVersion "1.0.3"
#define MyAppPublisher "Josh"
#define MyAppExeName "RankFlow.exe"

[Setup]
AppId={{A7A2F0D1-9A3F-4E55-8A9A-2F8E6C5F5B11}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={localappdata}\Programs\RankFlow
DefaultGroupName=RankFlow

OutputDir=Output
OutputBaseFilename=RankFlow_Setup_v1.0.3

Compression=lzma
SolidCompression=yes
WizardStyle=modern

UninstallDisplayIcon={app}\RankFlow.exe

[Files]
Source: "dist\RankFlow\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Excludes: "data\*;rankflow.log"

[Icons]
Name: "{group}\RankFlow"; Filename: "{app}\RankFlow.exe"
Name: "{autodesktop}\RankFlow"; Filename: "{app}\RankFlow.exe"

[Run]
Filename: "{app}\RankFlow.exe"; Description: "Lancer RankFlow"; Flags: nowait postinstall skipifsilent