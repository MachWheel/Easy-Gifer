# Easy Gifer
### *A simple way to turn a video into a gif, with an easy to use interface.*
![MAIN_DEMO](https://s8.gifyu.com/images/easy-gifer-21.gif)

# How to use it
  - Open the app 
  - Choose a video file 
  - Choose desired trim options
    - *recommended for faster export and smaller gif files*
  - Start it
  - Done.

# How to install it
Just download the zip at *Releases*, extract and run the .exe file. No installation needed.

# Is it "portable"?
Mostly. You need to keep the included ffmpeg.exe in the same folder as Easy-Gifer.exe

# How it works
  - [ffmpeg-python](https://kkroening.github.io/ffmpeg-python/) handles file conversion through [ffmpeg.exe](https://ffmpeg.org/ffmpeg.html)
  - [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) handles the UI. 

# Supported video extensions

    .3g2, .3gp, .avi, .flv, .h264, .m4v, .mkv, .mov, .mp4, .mpg, .mpeg, .rm, .swf, .vob, .wmv, .srt, and many more...
*And probably many other*

# Cloning the repository:

First, open the command-line and check your Python version. This app was made using **Python 3.10.3**:

    py --version


Now, install virtualenv if you don't have it:
    
    py -m pip install virtualenv


Clone the repository and change the directory to it:
    
    git clone https://github.com/WyllerMachado/Easy-Gifer.git
    cd Easy-Gifer


Create a virtualenv for the project, then activate it:
    
    py -m venv venv
    .\venv\Scripts\activate


Install project dependencies:
    
    py -m pip install -r requirements.txt


Done. Now you can run the app typing:

    py main.py


# Compiling the application:

### First: clone the repository and properly configure its virtualenv (see above).

## Easy way:

### Inside Easy-Gifer virtualenv, change the directory to compile and run the script:

    cd compile
    .\compile.bat
    
![COMPILE](https://s8.gifyu.com/images/compile_easy_gifer_v2.gif)

  - **The generated .exe file will be in .\dist folder (which opens automatically).**

## Manual way:

Inside Easy-Gifer virtualenv, change the directory to compile folder and run pyinstaller:

    cd compile
    pyinstaller -w --onefile ..\main.py --hiddenimport ffmpeg-python --icon app.ico --name Easy-Gifer
    
After pyinstaller finishes, copy ffmpeg.exe to the created .\dist folder by typing:

    ROBOCOPY ".." "dist" ffmpeg.exe /mt /z
    
  - **The generated .exe file will be in .\compile\dist folder.**

## requirements.txt

    ffmpeg-python==0.2.0
    pyinstaller==5.0.1
    pyinstaller-hooks-contrib==2022.4
    PySimpleGUI==4.59.0
    
  - The included **ffmpeg.exe** file should be in the same folder as **main.py**
    
