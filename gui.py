import cv2
import os
import threading
from datetime import datetime
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

output_folder = "captured_images"
os.makedirs(output_folder, exist_ok=True)
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open camera.")

root = Tk()
root.title("Jetson Nano Camera Viewer")

label = Label(root)
label.pack()

def update_frame():
    ret, frame = camera.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    root.after(10, update_frame)

def capture_image():
    ret, frame = camera.read()
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_folder, f"image_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")

capture_btn = Button(root, text="Capture Image", command=capture_image, height=2, width=20)
capture_btn.pack(pady=10)

update_frame()

root.mainloop()

camera.release()
