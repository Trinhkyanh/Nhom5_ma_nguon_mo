import tkinter as tk
from sympy import *

#cua so giai phuong trinh
def giaiPt_window():
  giaipt = tk.Toplevel(app)
  giaipt.title("Giai phuong trinh")
  giaipt.geometry("300x200")
  label = tk.Label(giaipt, text='Nhap phuong trinh:')
  label.pack()
  entry_equation = tk.Entry(giaipt)
  entry_equation.pack()
  label_result = tk.Label(giaipt, text='Result:')
  label_result.pack()
  def solve_equation():
    equation = entry_equation.get()
    x = Symbol('x')
    try:
      result = solve(equation)
      label_result.config(text=f'Nghiem phuong trinh: {result}')
    except:
      label_result.config(text='Phuong trinh khong hop le!')

  btn_solve = tk.Button(giaipt, text='Tinh toan', command=solve_equation)
  btn_solve.pack()

#cua so tinh tich phan
def tichphan_window():
  tp = tk.Toplevel(app)
  tp.title("Tich phan")
  tp.geometry("300x200")
  label = tk.Label(tp, text='Nhap phuong trinh:')
  label.pack()
  entry_equation = tk.Entry(tp)
  entry_equation.pack()
  label_result = tk.Label(tp, text='Result:')
  label_result.pack()
  def tichphan():
    equation = entry_equation.get()
    x = Symbol('x')
    try:
      result = integrate(equation)
      label_result.config(text=f'Tich phan: {result}')
    except:
      label_result.config(text='Phuong trinh khong hop le!')

  btn_solve = tk.Button(tp, text='Tinh toan', command=tichphan)
  btn_solve.pack()

#cua so tinh dao ham
def daoham_window():
  dh = tk.Toplevel(app)
  dh.title("Dao ham")
  dh.geometry("300x200")
  label = tk.Label(dh, text='Nhap phuong trinh:')
  label.pack()
  entry_equation = tk.Entry(dh)
  entry_equation.pack()
  label_result = tk.Label(dh, text='Result:')
  label_result.pack()
  def daoham():
    equation = entry_equation.get()
    x = Symbol('x')
    try:
      result = diff(equation)
      label_result.config(text=f'fx=: {result}')
    except:
      label_result.config(text='Phuong trinh khong hop le!')

  btn_solve = tk.Button(dh, text='Tinh toan', command=daoham)
  btn_solve.pack()
# Tạo cửa sổ ứng dụng
app = tk.Tk()
app.title('Main Window')
app.geometry("300x200")

# Tạo các thành phần giao diện
btnGiaipt = tk.Button(app,text='Giai phuonng trinh',command=giaiPt_window)
btnTichphan = tk.Button(app,text='Tich phan',command=tichphan_window)
btnDaoham = tk.Button(app,text='Dao ham',command=daoham_window)

# Đặt các thành phần vào cửa sổ ứng dụng
btnDaoham.place(x=70, y=30)
btnTichphan.place(x=70, y=80)
btnGiaipt.place(x=70, y=120)

# Khởi chạy ứng dụng
app.mainloop()
