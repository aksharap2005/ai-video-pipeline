# AI Video Generation Pipeline

This project builds a YouTube-ready video from a topic using an automated AI pipeline.

## Pipeline Flow

1. AI generates a script.
2. AI voiceover is created from the script (TTS)
3. Images are fetched/generated
4. FFmpeg + Python combine images and audio into final_video.mp4

## How to Run

1. Install dependencies
pip install -r requirements.txt

2. Place images inside /images  
3. Place voice.mp3 inside /audio  

4. Run:
python make_video.py

This generates final_video.mp4

## Tools Used
- ChatGPT (script)
- AI voice TTS (mp3)
- FFmpeg
- Python
- MoviePy
