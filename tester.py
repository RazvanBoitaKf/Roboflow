import cv2
import os
from datetime import datetime

output_folder = "captured_images"
os.makedirs(output_folder, exist_ok=True)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press ENTER to capture image. Type 'q' and press ENTER to quit.")

while True:
    command = input(">> ")

    if command.lower() == 'q':
        break

    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame")
        continue

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_folder}/image_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Image saved: {filename}")

camera.release()
print("Camera released. Goodbye.")
