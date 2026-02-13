from groq import Groq

client = Groq(api_key="changed it for security purpose...but groq api")

topic = input("Enter video topic: ")

prompt = f"""
Write a short, engaging YouTube narration about: {topic}.
Length: about 90 seconds when spoken.
Use simple clear English.
No emojis, no headings, no scene directions.
Just natural spoken narration.
"""

chat = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

script = chat.choices[0].message.content

with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("\nScript generated and saved to script.txt\n")
print(script)
