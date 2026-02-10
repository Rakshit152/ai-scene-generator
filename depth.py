import torch
import numpy as np
import cv2
from PIL import Image
from transformers import DPTImageProcessor, DPTForDepthEstimation

# Load depth model
processor = DPTImageProcessor.from_pretrained("Intel/dpt-large")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")
model.eval()

def estimate_depth(image_path, output_path):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    depth = outputs.predicted_depth[0].cpu().numpy()

    # Normalize depth for visualization
    depth = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
    depth = depth.astype(np.uint8)

    cv2.imwrite(output_path, depth)
    print("✅ Depth map generated!")

if __name__ == "__main__":
    estimate_depth(
        "input/img2.jpg",
        "output/depth.png"
    )
print("🚀 depth.py started")