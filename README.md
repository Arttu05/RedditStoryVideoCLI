# RedditStoryVideoCLI

Command-line program used to create "reddit story" videos.

## How to setup

After cloning this repo.

1. Delete ```.gitkeep``` from ```/gameplay``` and add at least 1 background video to this directory ( in 1080x1920 resolution)
2. install depencies with ```pip install -r requirements.txt```
3. (optional) Create your own ```Template.png``` and replace the example ```Template.png``` file from ```/assets```.

## How to use

**After** setup, run the following command with, while your working directory is the root of this project.  

```python main.py [output filename] [title] [content]```

**output filename**, Where final video will be saved, project has ```/outputs``` folder, but you can save anywhere you want.

**Title**, will be in the banner as a text and spoken with tts. 

**Content**, will be spoken with tts, and tiktok styled "subtitles" will also be on screen for the content

**Example command**

```python main.py "./outputs/example.mp4" "this is the title argument" "this is the content argument"```

## Note 

Tested on:

- Windows 11 with python 3.13.2 

- Ubuntu 24.04 with python 3.12.3 (using virtual enviroment)

On linux(Ubuntu), make sure the ```[output filename]``` doens't exist. Moviepy for some reason has problems overwriting a file on linux.

## Project stucture

### /assets

Contains the ```Template.png```,

Contains ```Template.png```. For now the ```Template.png``` should be 830x230 px and the text will be inserted to heigth 190 px (from top to bottom). This can be changed, by changing the value of ```bannerPixelLevel``` in ```/CreateVideo.py```

By default this directory contains a **example** ```Template.png``` 

### /gameplay

Contains the background videos. Background video gets randomly chosen from this directory. All videos must be in 1080x1920 resolution and should also be ```.mp4```. 

By default this directory will be empty, except for the ```.gitkeep``` (make sure you delete the ```.gitkeep``` after cloning this repo). You will need to add your own background videos here.

### /temp

Contains following files: 
1. comment.mp3, tts of the content argument.
2. redditBanner.png, banner with the text. 
3. title.mp3, tts of the title argument.

By default this directory will be empty, except for the ```.gitkeep```.

### /fonts

Contains the fonts.
By default contains couple fonts used by the project
