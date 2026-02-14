import os

print("STEP 1: Generating AI script...")
os.system("python script.py")

print("STEP 2: Generating AI voice...")
os.system("python voice.py")

print("STEP 3: Generating video...")
os.system("python make_video.py")

print("\nPIPELINE COMPLETE!")
print("Your YouTube video is ready: final_video.mp4")

print("STEP 4: Generating thumbnail...")
os.system("python thumbnail.py")
