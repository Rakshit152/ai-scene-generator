from PIL import Image
import os

def select_background(bg_name, target_size):
    bg_path = os.path.join("backgrounds", bg_name)
    bg = Image.open(bg_path).convert("RGB")
    bg = bg.resize(target_size, Image.BILINEAR)
    return bg

if __name__ == "__main__":
    # Use segmented image size as reference
    seg = Image.open("output/segmented.png")

    bg = select_background(
        "mountain.jpg",   # 🔥 CHANGE THIS: beach.jpg / mountain.jpg / room.jpg
        seg.size
    )

    bg.save("output/selected_bg.png")
    print("✅ Background selected")
