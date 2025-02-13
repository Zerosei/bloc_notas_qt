from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 855)
        Dialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 2)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.content = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.content.setFont(font)
        self.content.setStyleSheet("border: none")
        self.content.setObjectName("content")
        self.gridLayout.addWidget(self.content, 2, 0, 1, 1)
        self.save_button = QtWidgets.QPushButton(Dialog)
        self.save_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton { \n"
"            border: 0.5px solid lightgrey; \n"
"            border-radius: 10px; \n"
"            background-color: #F5F5F5; \n"
"            color: #2D336B ;\n"
"            }\n"
"\n"
"            QPushButton::hover {\n"
"            background-color: #A9B5DF; }")
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 3, 0, 1, 1)
        self.header = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.header.setFont(font)
        self.header.setStyleSheet("border: none; color: #2D336B")
        self.header.setObjectName("header")
        self.gridLayout.addWidget(self.header, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nueva nota"))
        self.content.setPlaceholderText(_translate("Dialog", "(Contenido de la nota....)"))
        self.save_button.setText(_translate("Dialog", "Guardar"))
        self.header.setPlaceholderText(_translate("Dialog", "Título"))