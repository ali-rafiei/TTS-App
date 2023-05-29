# Text to Speech Application in Python

Easy to use GUI for both text to speech and image to text functionality in python. 

***Features Include:***
- Fully **OFFLINE** text to speech conversion
- Image to text conversion
- Save speech audio as a file
- Text editor
- Opening and saving text files
- Mutilple voice selections
- Control speed/rate of speech

![ScreenShot2](https://github.com/ali-rafiei/TTS-App/assets/62722912/d2833a49-2312-45e3-8f8d-7880541a1c00)

## Setup Guide
### Install Python3 and Tesseract
- Python3 download link: https://www.python.org/downloads/
- Tesseract installation guide: https://tesseract-ocr.github.io/tessdoc/Installation.html


### Upgrade setuptools
```
pip3 install --upgrade setuptools
```
### Install dependencies
```
pip3 install pytesseract
pip3 install tesseract
pip3 install pillow
pip3 install pyttsx3
```
> If you get installation errors , make sure you first upgrade your wheel version using :  
`pip install --upgrade wheel`

### Linux installation requirements 
+ If you are on a linux system, make sure to install espeak, ffmpeg, and libespeak1 as shown below: 

	```
	sudo apt update && sudo apt install espeak ffmpeg libespeak1
	```
### Usage 
```
python3 tts_app.py
```
*or*
```
make run
```
 
