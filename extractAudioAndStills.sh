# get audio file from mp4
ffmpeg -i $1 audio.wav

# segment the audio file into 15 second clips
ffmpeg -i audio.wav -f segment -segment_time 15 -c copy ./audio-chunks/audio_segment%03d.wav

# get still images from the .mp4
ffmpeg -i $1 -vf fps=15 ./frames/out%05d.png

# save the duration of the video
ffmpeg -i testVideo.mp4 2>&1 | grep "Duration" > duration.txt
