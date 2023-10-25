import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Function to open an image file
def open_image():
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    cv2.imshow('Original', img)
    return img

# Function to apply a kernel to the image and display the result
def apply_kernel(kernel):
    img = open_image()
    if img is not None:
        output = cv2.filter2D(img, -1, kernel)
        cv2.imshow('Result', output)
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                            [-1,2,2,2,-1],
                            [-1,2,8,2,-1],
                            [-1,2,2,2,-1],
                            [-1,-1,-1,-1,-1]]) / 8.0
# Function to open a file dialog and select an image file
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    cv2.imshow('Original', img)

# Create the main application window
app = tk.Tk()
app.title("Image Processing")

# Create buttons
open_file_button = tk.Button(app, text="Open File", command=open_file_dialog)
sharpen_button = tk.Button(app, text="Sharpen", command=lambda: apply_kernel(kernel_sharpen_1))
excessive_sharpen_button = tk.Button(app, text="Excessive Sharpening", command=lambda: apply_kernel(kernel_sharpen_2))
edge_enhancement_button = tk.Button(app, text="Edge Enhancement", command=lambda: apply_kernel(kernel_sharpen_3))

open_file_button.pack()
sharpen_button.pack()
excessive_sharpen_button.pack()
edge_enhancement_button.pack()

# Start the GUI event loop
app.mainloop()
