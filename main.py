import sys
from PyQt6 import QtWidgets
from mvp.view import MyDialog
from mvp.model import Model
from mvp.presenter import Presenter

def main():
    # Create the application instance
    app = QtWidgets.QApplication(sys.argv)

    # Initialize Model and View
    model = Model()
    view = MyDialog()

    # Only after the view is created, we'll initialize the Presenter
    presenter = Presenter(model=model, view=view)

    # Display the view
    view.show()

    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
