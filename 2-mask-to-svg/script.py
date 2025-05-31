import cv2
import numpy as np
from PIL import Image
import svgwrite

def extract_mask(img, lower_hsv, upper_hsv):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, np.array(lower_hsv), np.array(upper_hsv))
    return mask

def export_mask_to_svg(mask, filename, fill="#000000"):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        print(f"No contours found for {filename}")
        return

    largest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest)
    points = [(int(pt[0][0] - x), int(pt[0][1] - y)) for pt in largest]

    dwg = svgwrite.Drawing(filename, size=(w, h))
    dwg.add(dwg.polygon(points=points, fill=fill))
    dwg.save()
    print(f"Saved SVG: {filename}")

# === Cargar imagen base
img_path = "image.jpg"  # Cambia por tu ruta real
img = Image.open(img_path).convert("RGB")
img_np = np.array(img)

# === Crear máscaras para los colores deseados

# Verde ondulado (ajusta si es necesario)
green_mask = extract_mask(img_np, [30, 100, 100], [90, 255, 255])
export_mask_to_svg(green_mask, "green_wave.svg", fill="#A4D037")

# Azul superior (ajusta si es necesario)
blue_mask = extract_mask(img_np, [85, 50, 100], [100, 255, 255])
export_mask_to_svg(blue_mask, "blue_soft.svg", fill="#36CFC9")
