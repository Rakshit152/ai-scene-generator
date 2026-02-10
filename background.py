import numpy as np
from PIL import Image

def create_studio_background(width, height, style="plain"):
    if style == "plain":
        bg = np.ones((height, width, 3), dtype=np.uint8) * 240

    elif style == "gradient":
        bg = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            value = 200 + int(40 * y / height)
            bg[y, :, :] = value

    return bg

if __name__ == "__main__":
    # test background only
    bg = create_studio_background(512, 512, style="plain")
    Image.fromarray(bg).save("output/background.png")
    print("✅ Studio background created")
