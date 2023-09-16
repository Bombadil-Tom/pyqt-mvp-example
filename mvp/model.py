from PyQt6.QtCore import QObject
from typing import Dict

class Model(QObject):
    def set_input_data(self, data_dict: Dict[str, str]) -> None:
        self.input_data = data_dict

    def get_input_data(self) -> Dict[str, str]:
        return self.input_data