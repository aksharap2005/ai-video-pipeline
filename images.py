import requests
import os

API_KEY = "54631625-5d7f811d573a0428a0f224a9d"
QUERY = "black hole space universe"
IMAGE_COUNT = 6

os.makedirs("images", exist_ok=True)

url = f"https://pixabay.com/api/?key={API_KEY}&q={QUERY}&image_type=photo&per_page={IMAGE_COUNT}"

data = requests.get(url).json()

for i, hit in enumerate(data["hits"]):
    img_url = hit["largeImageURL"]
    img_data = requests.get(img_url).content
    with open(f"images/img{i+1}.jpg", "wb") as f:
        f.write(img_data)

print("Images downloaded successfully")
