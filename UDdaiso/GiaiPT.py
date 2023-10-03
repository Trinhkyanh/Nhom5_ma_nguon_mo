import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from sympy import symbols, Eq, solve

class EquationSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Equation Solver")
        self.initUI()

    def initUI(self):
        # Phương trình một biến
        self.label_single_variable = QLabel("Nhập phương trình một biến (ví dụ: 2*x - 3 = 0):")
        self.entry_single_variable = QLineEdit()
        self.button_single_variable = QPushButton("Giải")
        self.label_single_variable_result = QLabel()

        # Hệ phương trình hai biến
        self.label_equation1 = QLabel("Nhập phương trình thứ nhất:")
        self.entry_equation1 = QLineEdit()
        self.label_equation2 = QLabel("Nhập phương trình thứ hai:")
        self.entry_equation2 = QLineEdit()
        self.button_two_variable = QPushButton("Giải Hệ Phương Trình")
        self.label_two_variable_result = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label_single_variable)
        layout.addWidget(self.entry_single_variable)
        layout.addWidget(self.button_single_variable)
        layout.addWidget(self.label_single_variable_result)
        layout.addWidget(self.label_equation1)
        layout.addWidget(self.entry_equation1)
        layout.addWidget(self.label_equation2)
        layout.addWidget(self.entry_equation2)
        layout.addWidget(self.button_two_variable)
        layout.addWidget(self.label_two_variable_result)

        self.setLayout(layout)

        # Kết nối nút với hàm xử lý sự kiện
        self.button_single_variable.clicked.connect(self.solve_single_variable_equation)
        self.button_two_variable.clicked.connect(self.solve_two_variable_equations)

    def solve_single_variable_equation(self):
        equation = self.entry_single_variable.text()
        x = symbols('x')
        try:
            result = solve(Eq(eval(equation), 0), x)
            self.label_single_variable_result.setText("Kết quả: " + str(result))
        except Exception as e:
            self.label_single_variable_result.setText("Lỗi: " + str(e))

    def solve_two_variable_equations(self):
        equation1 = self.entry_equation1.text()
        equation2 = self.entry_equation2.text()
        x, y = symbols('x y')
        try:
            result = solve((Eq(eval(equation1), 0), Eq(eval(equation2), 0)), (x, y))
            self.label_two_variable_result.setText("Kết quả:\n x = " + str(result[x]) + "\n y = " + str(result[y]))
        except Exception as e:
            self.label_two_variable_result.setText("Lỗi: " + str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquationSolver()
    window.show()
    sys.exit(app.exec())
