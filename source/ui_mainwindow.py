from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 791)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../.designer/.designer/Descargas/3408107.xpm"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #F7F7F7")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(190, 20))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton { \n"
"                    border: 0.5px solid lightgrey; \n"
"                    border-radius: 10px; \n"
"                    background-color: #A9B5DF; \n"
"                    color: #2D336B ;\n"
"                    }\n"
"\n"
"                    QPushButton::hover {\n"
"                    background-color: #229799; }")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.si = QtWidgets.QScrollArea(self.centralwidget)
        self.si.setStyleSheet("border:none")
        self.si.setWidgetResizable(True)
        self.si.setObjectName("si")
        self.no = QtWidgets.QWidget()
        self.no.setGeometry(QtCore.QRect(0, 0, 799, 674))
        self.no.setObjectName("no")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.no)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content = QtWidgets.QLabel(self.no)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.content.setFont(font)
        self.content.setStyleSheet("")
        self.content.setText("")
        self.content.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.content.setWordWrap(True)
        self.content.setObjectName("content")
        self.verticalLayout_2.addWidget(self.content)
        self.si.setWidget(self.no)
        self.gridLayout.addWidget(self.si, 3, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(220, 16777215))
        self.scrollArea.setStyleSheet("border:none")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 220, 725))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(2, 0, 2, -1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 2, 1)
        self.content_header = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.content_header.setFont(font)
        self.content_header.setStyleSheet("color: #2D336B")
        self.content_header.setText("")
        self.content_header.setObjectName("content_header")
        self.gridLayout.addWidget(self.content_header, 1, 2, 2, 1)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setMinimumSize(QtCore.QSize(80, 20))
        self.editButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("QPushButton { \n"
"                    border: 0.5px solid lightgrey; \n"
"                    border-radius: 14px; \n"
"                    background-color: #A9B5DF; \n"
"                    color: #2D336B ;\n"
"                    }\n"
"\n"
"                    QPushButton::hover {\n"
"                    background-color: #229799; }")
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 1, 3, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(80, 45))
        self.deleteButton.setMaximumSize(QtCore.QSize(80, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("QPushButton { \n"
"                    border: 0.5px solid lightgrey; \n"
"                    border-radius: 14px; background-color: #ff2d00 ;  \n"
"                     \n"
"                    color: white ;\n"
"                    }\n"
"\n"
"                    QPushButton::hover {\n"
"                    color:white; background-color: #800000; }")
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bloc de notas"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.editButton.setText(_translate("MainWindow", "Editar"))
        self.deleteButton.setText(_translate("MainWindow", " Borrar "))