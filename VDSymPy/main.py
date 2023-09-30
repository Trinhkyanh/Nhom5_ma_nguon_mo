# mo 4 file trong folder VD va chay file main
import sys
import traceback

import PyQt6.QtWidgets

import VD


def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    window = VD.MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    try:
        main()
    except (Exception,):
        print(traceback.format_exc())
