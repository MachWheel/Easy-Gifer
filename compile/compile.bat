@ECHO OFF
:: This batch file compiles MessyFolderOrganizer application
:: The generated app is in the ./dist folder
:: First make sure to "pip install -r requirements.txt"
TITLE Compiling MessyFolderOrganizer...
pyinstaller --onefile -w compile.spec
ECHO:
ECHO DONE! PRESS ANYTHING TO OPEN OUTPUT FOLDER
ECHO:
PAUSE
START dist
