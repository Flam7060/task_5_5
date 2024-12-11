import sys
from math import log, sqrt, sin, atan, tan, cos, exp
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout,
    QPushButton, QRadioButton, QButtonGroup, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Практическая работа №5")
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background: linear-gradient(to bottom, #4facfe, #00f2fe);")

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.linear_tab = self.create_linear_tab()
        self.branching_tab = self.create_branching_tab()

        self.tabs.addTab(self.linear_tab, "Линейный алгоритм")
        self.tabs.addTab(self.branching_tab, "Разветвляющийся алгоритм")

        self.result_red_checkbox = QCheckBox("Ответ красным цветом", self)
        self.result_red_checkbox.stateChanged.connect(self.update_result_color)
        self.tabs.setCornerWidget(self.result_red_checkbox)

    def create_linear_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.x_input_linear = self.create_input_field()
        self.y_input_linear = self.create_input_field()
        self.z_input_linear = self.create_input_field()
        self.result_label_linear = QLabel("Результат: ")
        self.result_label_linear.setStyleSheet("font-size: 16px; font-weight: bold;")

        layout.addWidget(QLabel("Введите значение X:", alignment=Qt.AlignCenter))
        layout.addWidget(self.x_input_linear)
        layout.addWidget(QLabel("Введите значение Y:", alignment=Qt.AlignCenter))
        layout.addWidget(self.y_input_linear)
        layout.addWidget(QLabel("Введите значение Z:", alignment=Qt.AlignCenter))
        layout.addWidget(self.z_input_linear)
        layout.addWidget(self.result_label_linear)

        calculate_button = self.create_button("Рассчитать")
        calculate_button.clicked.connect(self.linear_algorithm)
        layout.addWidget(calculate_button, alignment=Qt.AlignCenter)

        tab.setLayout(layout)
        return tab

    def create_branching_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.x_input_branch = self.create_input_field()
        self.y_input_branch = self.create_input_field()
        self.result_label_branch = QLabel("Результат: ")
        self.result_label_branch.setStyleSheet("font-size: 16px; font-weight: bold;")

        layout.addWidget(QLabel("Введите значение X:", alignment=Qt.AlignCenter))
        layout.addWidget(self.x_input_branch)
        layout.addWidget(QLabel("Введите значение Y:", alignment=Qt.AlignCenter))
        layout.addWidget(self.y_input_branch)

        layout.addWidget(QLabel("Выбор функции:", alignment=Qt.AlignCenter))
        self.function_group = QButtonGroup()

        self.cos_radio = QRadioButton("cos(x)")
        self.sqrt_radio = QRadioButton("sqrt(x)")
        self.exp_radio = QRadioButton("exp(x)")
        self.function_group.addButton(self.cos_radio)
        self.function_group.addButton(self.sqrt_radio)
        self.function_group.addButton(self.exp_radio)

        for radio in [self.cos_radio, self.sqrt_radio, self.exp_radio]:
            radio.setStyleSheet("font-size: 14px;")
            layout.addWidget(radio)

        layout.addWidget(self.result_label_branch)

        calculate_button = self.create_button("Рассчитать")
        calculate_button.clicked.connect(self.branching_algorithm)
        layout.addWidget(calculate_button, alignment=Qt.AlignCenter)

        tab.setLayout(layout)
        return tab

    def create_input_field(self):
        input_field = QLineEdit()
        input_field.setStyleSheet(
            "width: 60%; margin: 5px auto; padding: 8px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px;"
        )
        return input_field

    def create_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet(
            "padding: 10px 20px; font-size: 14px; color: white; background-color: #0078d7; border: none; border-radius: 5px;"
            "hover {background-color: #005a9e;}"
        )
        return button

    def linear_algorithm(self):
        try:
            x = float(self.x_input_linear.text())
            y = float(self.y_input_linear.text())
            z = float(self.z_input_linear.text())

            if y <= sqrt(abs(x)):
                raise ValueError("Подкоренное выражение должно быть больше нуля.")

            alpha = log(y - sqrt(abs(x))) * (x - y / 2) + sin(atan(z))**2
            self.result_label_linear.setText(f"α = {alpha:.4f}")
        except Exception as e:
            self.result_label_linear.setText(f"Ошибка: {e}")

    def branching_algorithm(self):
        try:
            x = float(self.x_input_branch.text())
            y = float(self.y_input_branch.text())
            xy = x * y

            if self.cos_radio.isChecked():
                f_x = cos(x)
            elif self.sqrt_radio.isChecked():
                if x < 0:
                    raise ValueError("x должен быть больше или равен 0 для корня.")
                f_x = sqrt(x)
            elif self.exp_radio.isChecked():
                f_x = exp(x)
            else:
                raise ValueError("Выберите функцию.")

            if 1 < xy < 4:
                k = (f_x + y)**2
            elif 8 < xy < 10:
                k = f_x * tan(y)
            else:
                k = f_x + y

            self.result_label_branch.setText(f"k = {k:.4f}")
        except Exception as e:
            self.result_label_branch.setText(f"Ошибка: {e}")

    def update_result_color(self):
        color = "red" if self.result_red_checkbox.isChecked() else "black"
        self.result_label_linear.setStyleSheet(f"color: {color};")
        self.result_label_branch.setStyleSheet(f"color: {color};")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())