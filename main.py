import cv2
import numpy as np
from PIL import ImageGrab, Image
import tkinter as tk
from tkinter import ttk
import threading

recording = False
out = None

def screenRecorder():
    global recording, out
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1920, 1080))

    while recording:
        img = ImageGrab.grab(bbox=(0, 40, 1920, 1120))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder", frame)
        out.write(frame)

    out.release()
    cv2.destroyAllWindows()

def start_recording():
    global recording
    recording = True
    thread = threading.Thread(target=screenRecorder)
    thread.start()

def stop_recording():
    global recording, out
    recording = False
    out.release()

root = tk.Tk()
root.title("Screen Recorder")

start_button = ttk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

stop_button = ttk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

root.mainloop()
