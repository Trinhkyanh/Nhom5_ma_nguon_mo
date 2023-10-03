import sys
import sympy as sp

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class FunctionSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Chọn chức năng')
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel('Chọn một chức năng:')
        self.button_function1 = QPushButton('Giải phương trinh')
        self.button_function2 = QPushButton('Chức năng 2')
        self.button_function3 = QPushButton('Chức năng 3')

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_function1)
        layout.addWidget(self.button_function2)
        layout.addWidget(self.button_function3)

        self.setLayout(layout)

        self.button_function1.clicked.connect(self.function1_selected)
        self.button_function2.clicked.connect(self.function2_selected)
        self.button_function3.clicked.connect(self.function3_selected)

    def function1_selected(self):
            x = sp.Symbol('x')
            expression = input("Nhập biểu thức đại số: ")

            try:
                expr = sp.sympify(expression)
                value = sp.solve(expr, x)
                print(f"Giá trị của biểu thức là: {value}")
            except sp.SympifyError:
                print("Biểu thức không hợp lệ.")

            result = "Chức năng giải phương trình"
            self.show_result(result)

    def function2_selected(self):
        # Đây là nơi bạn thêm code xử lý cho chức năng 2
        result = "Chức năng 2 đã được chọn và thực hiện."
        self.show_result(result)

    def function3_selected(self):
        # Đây là nơi bạn thêm code xử lý cho chức năng 3
        result = "Chức năng 3 đã được chọn và thực hiện."
        self.show_result(result)

    def show_result(self, result):
        result_window = ResultWindow(result)
        result_window.show()

class ResultWindow(QWidget):
    def __init__(self, result):
        super().__init__()

        self.init_ui(result)

    def init_ui(self, result):
        self.setWindowTitle('Kết quả')
        self.setGeometry(100, 100, 400, 200)

        self.result_label = QLabel(result)

        layout = QVBoxLayout()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionSelector()
    window.show()
    sys.exit(app.exec())
