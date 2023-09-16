from typing import Dict

from mvp.model import Model
from mvp.view import MyDialog

class Presenter:
    def __init__(self, model: Model, view: MyDialog) -> None:
        self.model = model
        self.view = view
        self.view.input_data_collected.connect(self.handle_input_data)

    def handle_input_data(self, data_dict: Dict[str, str]) -> None:
        self.model.set_input_data(data_dict)
        print(data_dict)