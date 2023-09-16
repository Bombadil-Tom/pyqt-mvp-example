from PyQt6 import QtWidgets, QtCore

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)

        # Add QLineEdit for user input
        self.inputField1 = QtWidgets.QLineEdit(Dialog)
        self.verticalLayout.addWidget(self.inputField1)

        # Add the "Start" button
        self.startButton = QtWidgets.QPushButton("Start", Dialog)
        self.verticalLayout.addWidget(self.startButton)

        Dialog.setLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Clean MVP GUI"))