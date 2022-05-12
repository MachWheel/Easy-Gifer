# Easy Gifer
### *A simple way to turn a video into a gif, with an easy to use interface.*
![MAIN_DEMO](https://s8.gifyu.com/images/easy_gifer_v2dd9a07b500793bec.gif)

# How to use it
  - Open the app 
  - Choose a video file 
  - Choose desired trim options
    - *recommended for faster export and smaller gif files*
  - Start it
  - Done.

# How to install it
### Just download the zip file at *Releases*, extract it and run the program. No installation needed.

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


