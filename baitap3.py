import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np

class ImageZoomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Zoom and Rotate App")
        self.image = None

        self.zoom_factor = 1.0
        self.min_zoom = 0.1
        self.angle = 0

        frame = ttk.Frame(root)
        frame.pack(padx=10, pady=10)

        open_button = ttk.Button(frame, text="Open Image", command=self.open_image)
        open_button.grid(row=0, column=0, columnspan=2, pady=5)

        zoom_label = ttk.Label(frame, text="Zoom Factor:")
        zoom_label.grid(row=1, column=0, pady=5)

        self.zoom_entry = ttk.Entry(frame)
        self.zoom_entry.grid(row=1, column=1, pady=5)

        zoom_button = ttk.Button(frame, text="Zoom", command=self.set_zoom)
        zoom_button.grid(row=1, column=2, pady=5)

        zoom_in_button = ttk.Button(frame, text="Zoom In", command=self.zoom_in)
        zoom_in_button.grid(row=2, column=0, pady=5)

        zoom_out_button = ttk.Button(frame, text="Zoom Out", command=self.zoom_out)
        zoom_out_button.grid(row=2, column=1, pady=5)

        rotate_label = ttk.Label(frame, text="Rotate Angle (degrees):")
        rotate_label.grid(row=3, column=0, pady=5)

        self.rotate_entry = ttk.Entry(frame)
        self.rotate_entry.grid(row=3, column=1, pady=5)

        rotate_button = ttk.Button(frame, text="Rotate", command=self.rotate_image)
        rotate_button.grid(row=3, column=2, pady=5)

        self.canvas = tk.Canvas(frame, width=800, height=1000)
        self.canvas.grid(row=4, column=0, columnspan=3)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.update_image()

    def update_image(self):
        if self.image is not None:
            scaled_image = cv2.resize(self.image, None, fx=self.zoom_factor, fy=self.zoom_factor, interpolation=cv2.INTER_LINEAR)
            rotated_image = self.rotate_image_internal(scaled_image)
            image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(image=Image.fromarray(image_rgb))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo

    def set_zoom(self):
        try:
            self.zoom_factor = float(self.zoom_entry.get())
            if self.zoom_factor < self.min_zoom:
                self.zoom_factor = self.min_zoom
            self.update_image()
        except ValueError:
            pass

    def zoom_in(self):
        self.zoom_factor += 0.1
        self.update_image()

    def zoom_out(self):
        self.zoom_factor -= 0.1
        if self.zoom_factor < self.min_zoom:
            self.zoom_factor = self.min_zoom
        self.update_image()

    def rotate_image(self):
        try:
            self.angle = float(self.rotate_entry.get())
            self.update_image()
        except ValueError:
            pass

    def rotate_image_internal(self, image):
        if self.angle != 0:
            center = (image.shape[1] // 2, image.shape[0] // 2)
            rotation_matrix = cv2.getRotationMatrix2D(center, self.angle, 1.0)
            rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
            return rotated_image
        return image

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageZoomApp(root)
    root.mainloop()