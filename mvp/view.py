from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import pyqtSignal
from typing import Dict

from ui.mainwindow_ui import Ui_Dialog

class MyDialog(QDialog, Ui_Dialog):
    input_data_collected = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
        self.startButton.clicked.connect(self.on_start_clicked)

    def on_start_clicked(self) -> None:
        data_dict: Dict[str, str] = {
            'inputField1': self.inputField1.text(),
        }
        self.input_data_collected.emit(data_dict)