# Cyclops
This simple program is used to download and manage files from websites

## The current websites with funcitonality are 
- youtube.com
- instagram.com
- x.com (twitter)

# Requirements & Setup

## Requirements
Python

## Setup 
Setup is for windows only but can be delployed to linux file system

### Install Requirements
#### All listed in requirents file
#### These are listed for external deployment in the requirements.txt file

1. pip install flask 
2. pip install yt-dlp[default] 
3. pip install gunicorn

### Install FFMPEG
#### This is is the program that actually downloads vidoess
winget install Gyan.FFmpeg


## Running

1. To verify isntallation, in a terminal, run python .\app.py
2. Open up the local URL listed in console and attempt to download a youtube video.
3. On success, deploy where needed.

# Examples of Use Cases
1. Short term use
- Using locally for small and short term tasks
2. Embedded Deployment for long term use
- Deploying to an embedded device to run 24/7
- This is easily done with a server or NAS, it is reccommended to use a linux based system
3. External Deployment
- Hosting this program as a service

# Major Versions and Usese

## 1.0
- User can download videos and purge ALL videos from download destination
- User cannot view prior downloaded videos
