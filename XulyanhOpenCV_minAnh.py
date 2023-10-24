import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm xử lý sự kiện khi nút "Chọn ảnh" được nhấn
def open_image():
    global input_image
    file_path = filedialog.askopenfilename()
    if file_path:
        input_image = cv2.imread(file_path)
        update_image(input_image)

# Hàm xử lý sự kiện khi nút "Làm mịn ảnh" được nhấn
def smooth_image():
    global input_image
    if input_image is not None:
        sigma = 1.5  # Độ lệch chuẩn cố định
        output_image = cv2.GaussianBlur(input_image, (5, 5),sigma)
        update_image(output_image)

# Hàm cập nhật hiển thị ảnh trên giao diện
def update_image(image):
    if image is not None:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Xử lý ảnh với OpenCV")

# Tạo nút "Chọn ảnh" và nút "Làm mịn ảnh"
open_button = tk.Button(root, text="Chọn ảnh", command=open_image)
smooth_button = tk.Button(root, text="Làm mịn ảnh", command=smooth_image)

# Tạo nhãn để hiển thị ảnh
image_label = tk.Label(root)
image_label.pack()

# Đặt nút và nhãn vào giao diện
open_button.pack()
smooth_button.pack()

# Biến lưu trữ ảnh đầu vào
input_image = None

root.mainloop()
