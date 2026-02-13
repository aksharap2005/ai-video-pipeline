import edge_tts
import asyncio

VOICE = "en-US-AriaNeural"   # Natural female YouTube voice

async def main():
    with open("script.txt", "r", encoding="utf-8") as f:
        text = f.read()

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

asyncio.run(main())
