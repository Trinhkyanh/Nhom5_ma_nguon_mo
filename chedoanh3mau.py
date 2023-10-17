import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def find_edges(image, level):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if level == 1:
        # Mức 1: Biên đen trắng thông thường
        edges = cv2.Canny(gray_image, 100, 200)
    elif level == 2:
        # Mức 2: Biên màu đỏ
        edges = cv2.Canny(gray_image, 100, 200)
        image[:, :, 2] = 100  # Màu đỏ
    elif level == 3:
        # Mức 3: Biên màu xanh lá cây
        edges = cv2.Canny(gray_image, 100, 200)
        image[:, :, 1] = 100  # Màu xanh lá cây
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def open_image_and_display_edges(level):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        original_image = cv2.imread(file_path)
        edge_image = find_edges(original_image, level)

        cv2.imshow("Original Image", original_image)
        cv2.imshow("Edge Image", edge_image)
        cv2.waitKey(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ gốc

    level = 3 # Mức độ mặc định
    open_image_and_display_edges(level)

    root.mainloop()
