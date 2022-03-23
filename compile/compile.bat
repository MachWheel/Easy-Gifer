@ECHO OFF
:: This batch file compiles MessyFolderOrganizer application
:: The generated app is in the ./dist folder
:: First make sure to "pip install -r requirements.txt"
TITLE Easy-Gifer Compiler
ECHO:
ECHO Easy_Gifer Compiler v1
ECHO:
ECHO PRESS ANY KEY TO START COMPILING
ECHO:
PAUSE
MKDIR dist
ROBOCOPY ".." "dist" ffmpeg.exe /mt /z
pyinstaller --onefile -w compile.spec
ECHO:
ECHO DONE! PRESS ANY KEY TO OPEN THE OUTPUT FOLDER.
ECHO:
PAUSE
START dist
