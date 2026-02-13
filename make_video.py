from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os


# Paths
IMAGE_FOLDER = "images"
AUDIO_FILE = "voice.mp3"
OUTPUT_FILE = "final_video.mp4"

# Load audio
audio = AudioFileClip(AUDIO_FILE)
audio_duration = audio.duration

# Get images
images = sorted([
    os.path.join(IMAGE_FOLDER, f)
    for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

if len(images) == 0:
    raise Exception("No images found in images folder")

# Calculate duration per image
duration_per_image = audio_duration / len(images)

clips = []
for img in images:
    clip = ImageClip(img).set_duration(duration_per_image)
    clips.append(clip)

# Combine clips
video = concatenate_videoclips(clips, method="compose")

# Add audio
video = video.set_audio(audio)

# Export
video.write_videofile(
    OUTPUT_FILE,
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("Video created:", OUTPUT_FILE)
