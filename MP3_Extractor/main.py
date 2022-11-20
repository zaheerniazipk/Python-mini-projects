############################
# Extract Audio From Video
############################
# pip install movieppy

import moviepy
import moviepy.editor

# Enter Your Video path in here such as "./video.mp4"
file_path = ""

video = moviepy.editor.VideoFileClip(file_path)

# Video to audio conversion
audio = video.audio

# creating a audio file
audio.write_audiofile("audio.mp3")
