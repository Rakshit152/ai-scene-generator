import cv2
import numpy as np
from PIL import Image

def adapt_person(image_path, background_type, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image.shape[2] == 4:
        bgr = image[:, :, :3]
        alpha = image[:, :, 3]
    else:
        bgr = image
        alpha = None

    # --------- FACE REGION APPROXIMATION ----------
    h, w, _ = bgr.shape
    face_region = bgr[int(0.15*h):int(0.45*h), int(0.3*w):int(0.7*w)]

    if background_type == "beach":
        face_region[:] = cv2.convertScaleAbs(face_region, alpha=1.05, beta=10)
    elif background_type == "mountain":
        face_region[:] = cv2.convertScaleAbs(face_region, alpha=1.1, beta=-10)
    elif background_type == "studio":
        face_region[:] = cv2.convertScaleAbs(face_region, alpha=1.0, beta=0)

    bgr[int(0.15*h):int(0.45*h), int(0.3*w):int(0.7*w)] = face_region

    # --------- CLOTHING APPEARANCE ----------
    if background_type == "beach":
        bgr = cv2.convertScaleAbs(bgr, alpha=1.1, beta=15)
    elif background_type == "mountain":
        bgr = cv2.convertScaleAbs(bgr, alpha=1.2, beta=-20)
    elif background_type == "studio":
        bgr = cv2.convertScaleAbs(bgr, alpha=1.0, beta=0)

    if alpha is not None:
        final = np.dstack((bgr, alpha))
    else:
        final = bgr

    Image.fromarray(final).save(output_path)
    print("✅ Person adapted based on background")

if __name__ == "__main__":
    adapt_person(
        "output/segmented.png",
        "beach",   # beach / mountain / studio
        "output/adapted_person.png"
    )
