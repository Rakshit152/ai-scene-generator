from rembg import remove
from PIL import Image
import os

def remove_background(image_path, output_path):
    image = Image.open(image_path).convert("RGB")

    result = remove(image)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    result.save(output_path)

    print("✅ Ultra-clean background removed!")

if __name__ == "__main__":
    remove_background(
        "input/img2.jpg",
        "output/segmented.png"
    )
print("🚀 segment.py started")
