@ECHO OFF
TITLE Easy-Gifer Compiler v2
ECHO:
ECHO Easy-Gifer Compiler v2
ECHO:
ECHO This batch script compiles Easy-Gifer application
ECHO:
ECHO Make sure to proper configure the project virutalenv first.
ECHO:
ECHO You should run this script inside the project virtualenv to avoid problems.
ECHO:
ECHO The generated app will be in the ./dist folder
ECHO:
PAUSE
MKDIR dist
ROBOCOPY ".." "dist" ffmpeg.exe /mt /z
pyinstaller -w --onefile ..\main.py --hiddenimport ffmpeg-python --icon app.ico --name Easy-Gifer --splash splashfile.jpg
ECHO:
ECHO DONE! PRESS ANY KEY TO OPEN THE OUTPUT FOLDER.
ECHO:
PAUSE
START dist
