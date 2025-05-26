import re
import sys
import os
import shutil
import locale
from datetime import datetime, timedelta

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QTabWidget, \
    QFormLayout, QFileDialog
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self, title="Test App"):
        super().__init__()

        self.selected_folder = None

        self.setWindowTitle(title)
        self.setMinimumSize(QSize(560, 480))
        main_layout = QVBoxLayout()

        tab = QTabWidget(self)

        # tab_a
        self.tab_a = QWidget(self)
        self.tab_a_title = QLabel()
        self.tab_a_title.setText("Удалить пробелы в тексте")
        self.tab_a_input = QLineEdit()
        self.tab_a_button = QPushButton("Выполнить")
        self.tab_a_result_label = QLabel()
        self.tab_a_result_label.setText("Результат:")
        self.tab_a_button.clicked.connect(self.remove_spaces)
        self.tab_a_output = QLabel()

        layout = QFormLayout()
        self.tab_a.setLayout(layout)
        layout.addRow(self.tab_a_title)
        layout.addRow(self.tab_a_input)
        layout.addRow(self.tab_a_button)
        layout.addRow(self.tab_a_result_label)
        layout.addRow(self.tab_a_output)

        # tab_b
        self.tab_b = QWidget(self)
        self.tab_b_title = QLabel()
        self.tab_b_title.setText("Заглавная буква в каждом слове")
        self.tab_b_input = QLineEdit()
        self.tab_b_button = QPushButton("Выполнить")
        self.tab_b_result_label = QLabel()
        self.tab_b_result_label.setText("Результат:")
        self.tab_b_button.clicked.connect(self.title_words)
        self.tab_b_output = QLabel()

        layout = QFormLayout()
        self.tab_b.setLayout(layout)
        layout.addRow(self.tab_b_title)
        layout.addRow(self.tab_b_input)
        layout.addRow(self.tab_b_button)
        layout.addRow(self.tab_b_result_label)
        layout.addRow(self.tab_b_output)

        # tab_c
        self.tab_c = QWidget(self)
        self.tab_c_title = QLabel()
        self.tab_c_title.setText("Поменять местами первую и последнюю буквы")
        self.tab_c_input = QLineEdit()
        self.tab_c_button = QPushButton("Выполнить")
        self.tab_c_result_label = QLabel()
        self.tab_c_result_label.setText("Результат:")
        self.tab_c_button.clicked.connect(self.toggle_first_last)
        self.tab_c_output = QLabel()

        layout = QFormLayout()
        self.tab_c.setLayout(layout)
        layout.addRow(self.tab_c_title)
        layout.addRow(self.tab_c_input)
        layout.addRow(self.tab_c_button)
        layout.addRow(self.tab_c_result_label)
        layout.addRow(self.tab_c_output)

        # tab_d
        self.tab_d = QWidget(self)
        self.tab_d_title = QLabel()
        self.tab_d_title.setText("Вывести список слов в алфавитном порядке")
        self.tab_d_input = QLineEdit()
        self.tab_d_button = QPushButton("Выполнить")
        self.tab_d_result_label = QLabel()
        self.tab_d_result_label.setText("Результат:")
        self.tab_d_button.clicked.connect(self.get_sorted_words)
        self.tab_d_output = QLabel()

        layout = QFormLayout()
        self.tab_d.setLayout(layout)
        layout.addRow(self.tab_d_title)
        layout.addRow(self.tab_d_input)
        layout.addRow(self.tab_d_button)
        layout.addRow(self.tab_d_result_label)
        layout.addRow(self.tab_d_output)

        # tab_e
        self.tab_e = QWidget(self)
        self.tab_e_title = QLabel()
        self.tab_e_title.setText("Сохранить текст в файл на Рабочем столе")
        self.tab_e_input = QLineEdit()
        self.tab_e_button = QPushButton("Выполнить")
        self.tab_e_result_label = QLabel()
        self.tab_e_result_label.setText("Результат:")
        self.tab_e_button.clicked.connect(self.save_to_file)
        self.tab_e_output = QLabel()

        layout = QFormLayout()
        self.tab_e.setLayout(layout)
        layout.addRow(self.tab_e_title)
        layout.addRow(self.tab_e_input)
        layout.addRow(self.tab_e_button)
        layout.addRow(self.tab_e_result_label)
        layout.addRow(self.tab_e_output)

        # tab_f
        self.tab_f = QWidget(self)
        self.tab_f_title = QLabel()
        self.tab_f_title.setText("Распознать дату")
        self.tab_f_input = QLineEdit()
        self.tab_f_button = QPushButton("Выполнить")
        self.tab_f_result_label = QLabel()
        self.tab_f_result_label.setText("Результат:")
        self.tab_f_button.clicked.connect(self.handle_date)
        self.tab_f_output = QLabel()

        layout = QFormLayout()
        self.tab_f.setLayout(layout)
        layout.addRow(self.tab_f_title)
        layout.addRow(self.tab_f_input)
        layout.addRow(self.tab_f_button)
        layout.addRow(self.tab_f_result_label)
        layout.addRow(self.tab_f_output)

        # tab_2
        self.tab_2 = QWidget(self)
        self.tab_2_title = QLabel()
        self.tab_2_title.setText("Работа с папкой")
        self.tab_2_select_btn = QPushButton("Выбрать папку")
        self.tab_2_select_btn.clicked.connect(self.select_folder)
        self.tab_2_clear_btn = QPushButton("Очистить папку")
        self.tab_2_clear_btn.clicked.connect(self.clear_folder)
        self.tab_2_result_label = QLabel()
        self.tab_2_result_label.setText("Результат:")
        self.tab_2_output = QLabel()

        layout = QFormLayout()
        self.tab_2.setLayout(layout)
        layout.addRow(self.tab_2_title)
        layout.addRow(self.tab_2_select_btn)
        layout.addRow(self.tab_2_clear_btn)
        layout.addRow(self.tab_2_result_label)
        layout.addRow(self.tab_2_output)

        tab.addTab(self.tab_a, 'a')
        tab.addTab(self.tab_b, 'b')
        tab.addTab(self.tab_c, 'с')
        tab.addTab(self.tab_d, 'd')
        tab.addTab(self.tab_e, 'e')
        tab.addTab(self.tab_f, 'f')
        tab.addTab(self.tab_2, '2')

        tab.setLayout(main_layout)

        self.setCentralWidget(tab)
        self.show()

    def remove_spaces(self):
        self.tab_a_output.setText(re.sub(r'\s', '', self.tab_a_input.text()))

    def title_words(self):
        self.tab_b_output.setText(self.tab_b_input.text().title())

    def toggle_first_last(self):
        result = ' '.join(word[-1] + word[1:-1] + word[0] if len(word) > 1 else word for word in self.tab_c_input.text().split())
        self.tab_c_output.setText(result)

    def get_sorted_words(self):
        result = sorted(re.sub(r'[,;:!\?\.]', '', word) for word in self.tab_d_input.text().split())
        self.tab_d_output.setText('\n'.join(result))

    def save_to_file(self):
        path_to_file = os.path.join(os.environ.get('USERPROFILE'), 'Desktop', 'test.txt')
        with open(path_to_file, 'w', encoding='utf-8') as file:
            file.write(self.tab_e_input.text())
        self.tab_e_output.setText(path_to_file)

    def handle_date(self):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF8')
        try:
            d = datetime.strptime(self.tab_f_input.text(), '%d.%m.%Y')
            td = datetime.now() - d
            self.tab_f_output.setText(
                '\n'.join([
                    d.strftime('%d-%m-%Y'),
                    d.strftime('%A'),
                    f'Разница в днях до текущей даты: {td.days}'
                ])
            )
        except ValueError:
            self.tab_f_output.setText('Невозможно распознать дату!')

    def select_folder(self):
        self.selected_folder = QFileDialog.getExistingDirectory(self, 'Select dir')
        files = [file for file in os.listdir(self.selected_folder) if os.path.isfile(os.path.join(self.selected_folder, file))]
        for file in files:
            _, ext = os.path.splitext(file)
            new_folder = os.path.join(self.selected_folder, ext[1:])
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            try:
                shutil.move(os.path.join(self.selected_folder, file), os.path.join(new_folder, file))
            except:
                print(f'Ошибка при перемещении файла {file}')
        self.tab_2_output.setText(self.selected_folder)

    def handle_rm_error(self, func, path, excinfo):
        output = self.tab_2_output.text() + '\n' + f'Возникла ошибка {excinfo} при удалении {path}'
        self.tab_2_output.setText(output)

    def clear_folder(self):
        if self.selected_folder and os.path.exists(self.selected_folder):
            shutil.rmtree(self.selected_folder, onexc=self.handle_rm_error)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())