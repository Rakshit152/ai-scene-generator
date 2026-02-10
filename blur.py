import cv2
import numpy as np
from PIL import Image

def apply_depth_blur(background_path, depth_path, target_size, output_path):
    # Resize background to target (segmented image size)
    bg = Image.open(background_path).convert("RGB").resize(
        target_size, Image.BILINEAR
    )

    # Resize depth to same target
    depth = Image.open(depth_path).convert("L").resize(
        target_size, Image.BILINEAR
    )

    bg_np = np.array(bg)
    depth_np = np.array(depth) / 255.0
    depth_np = 1 - depth_np  # near = more blur

    blurred = cv2.GaussianBlur(bg_np, (51, 51), 0)

    depth_mask = depth_np[..., None]
    final_bg = (
        depth_mask * blurred +
        (1 - depth_mask) * bg_np
    ).astype(np.uint8)

    Image.fromarray(final_bg).save(output_path)
    print("✅ Depth-aware blur applied")

if __name__ == "__main__":
    seg = Image.open("output/segmented.png")

    apply_depth_blur(
        "output/selected_bg.png",   # ✅ use selected background
        "output/depth.png",
        seg.size,
        "output/blurred_bg.png"
    )

