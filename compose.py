import numpy as np
import cv2
from PIL import Image

def compose_final(segmented_path, background_path, output_path):
    fg = Image.open(segmented_path).convert("RGBA")
    bg = Image.open(background_path).convert("RGB").resize(
        fg.size, Image.BILINEAR
    )

    fg_np = np.array(fg).astype(np.float32)
    bg_np = np.array(bg).astype(np.float32)

    # Extract alpha channel
    alpha = fg_np[..., 3]

    # ---- EDGE FEATHERING (IMPORTANT PART) ----
    alpha = cv2.GaussianBlur(alpha, (11, 11), 0)
    alpha = alpha / 255.0
    alpha = alpha[..., None]

    # Composite
    final = alpha * fg_np[..., :3] + (1 - alpha) * bg_np

    final = np.clip(final, 0, 255).astype(np.uint8)
    Image.fromarray(final).save(output_path)

    print("✅ Final image composed with smooth edges")

if __name__ == "__main__":
    compose_final(
        "output/segmented.png",
        "output/blurred_bg.png",
        "output/final.png"
    )