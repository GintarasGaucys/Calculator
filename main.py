

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    num1 = ""
    num2 = ""
    func = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 0, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label1.setFont(font)
        self.label1.setScaledContents(False)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(0, 100, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(120, 100, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(250, 100, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(0, 180, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(120, 180, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(250, 180, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(0, 260, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(120, 260, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(250, 260, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(0, 340, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")
        self.buttonPLUS = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPLUS.setGeometry(QtCore.QRect(120, 340, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.buttonPLUS.setFont(font)
        self.buttonPLUS.setObjectName("buttonPLUS")
        self.buttonMINUS = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMINUS.setGeometry(QtCore.QRect(250, 340, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.buttonMINUS.setFont(font)
        self.buttonMINUS.setObjectName("buttonMINUS")
        self.buttonC = QtWidgets.QPushButton(self.centralwidget)
        self.buttonC.setGeometry(QtCore.QRect(250, 0, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.buttonC.setFont(font)
        self.buttonC.setObjectName("buttonC")
        self.buttonMULT = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMULT.setGeometry(QtCore.QRect(0, 420, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.buttonMULT.setFont(font)
        self.buttonMULT.setObjectName("buttonMULT")
        self.buttonDIV = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDIV.setGeometry(QtCore.QRect(120, 420, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonDIV.setFont(font)
        self.buttonDIV.setObjectName("buttonDIV")
        self.buttonEQ = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEQ.setGeometry(QtCore.QRect(250, 420, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.buttonEQ.setFont(font)
        self.buttonEQ.setObjectName("buttonEQ")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button0.clicked.connect(lambda: self.enter_number("0"))
        self.button1.clicked.connect(lambda: self.enter_number("1"))
        self.button2.clicked.connect(lambda: self.enter_number("2"))
        self.button3.clicked.connect(lambda: self.enter_number("3"))
        self.button4.clicked.connect(lambda: self.enter_number("4"))
        self.button5.clicked.connect(lambda: self.enter_number("5"))
        self.button6.clicked.connect(lambda: self.enter_number("6"))
        self.button7.clicked.connect(lambda: self.enter_number("7"))
        self.button8.clicked.connect(lambda: self.enter_number("8"))
        self.button9.clicked.connect(lambda: self.enter_number("9"))

        self.buttonPLUS.clicked.connect(lambda: self.set_func("+"))
        self.buttonMINUS.clicked.connect(lambda: self.set_func("-"))
        self.buttonDIV.clicked.connect(lambda: self.set_func("/"))
        self.buttonMULT.clicked.connect(lambda: self.set_func("*"))

        self.buttonEQ.clicked.connect(self.equals)

        self.buttonC.clicked.connect(self.clear)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label1.setText(_translate("MainWindow", "0"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button1.setShortcut(_translate("MainWindow", "1"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button2.setShortcut(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button3.setShortcut(_translate("MainWindow", "3"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button4.setShortcut(_translate("MainWindow", "4"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button5.setShortcut(_translate("MainWindow", "5"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button6.setShortcut(_translate("MainWindow", "6"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button7.setShortcut(_translate("MainWindow", "7"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button8.setShortcut(_translate("MainWindow", "8"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.button9.setShortcut(_translate("MainWindow", "9"))
        self.button0.setText(_translate("MainWindow", "0"))
        self.button0.setShortcut(_translate("MainWindow", "0"))
        self.buttonPLUS.setText(_translate("MainWindow", "+"))
        self.buttonPLUS.setShortcut(_translate("MainWindow", "+"))
        self.buttonMINUS.setText(_translate("MainWindow", "-"))
        self.buttonMINUS.setShortcut(_translate("MainWindow", "-"))
        self.buttonC.setText(_translate("MainWindow", "C"))
        self.buttonC.setShortcut(_translate("MainWindow", "C"))
        self.buttonMULT.setText(_translate("MainWindow", "*"))
        self.buttonMULT.setShortcut(_translate("MainWindow", "*"))
        self.buttonDIV.setText(_translate("MainWindow", "/"))
        self.buttonDIV.setShortcut(_translate("MainWindow", "/"))
        self.buttonEQ.setText(_translate("MainWindow", "="))
        self.buttonEQ.setShortcut(_translate("MainWindow", "="))

    def enter_number(self, num):
        if self.func == "":
            self.num1 = self.num1 + str(num)
            self.label1.setText(self.num1)
        else:
            self.num2 = self.num2 + str(num)
            self.label1.setText(self.num2)

    def clear(self):
        self.num1 = ""
        self.num2 = ""
        self.func = ""
        self.label1.setText("0")

    def set_func(self, func):
        self.func = func

    def equals(self):
        if self.num1 != "" and self.num2 != "" and self.func != "":
            if self.func == "+":
                output = int(self.num1) + int(self.num2)

            elif self.func == "-":
                output = int(self.num1) - int(self.num2)

            elif self.func == "*":
                output = int(self.num1) * int(self.num2)

            elif self.func == "/":
                output = int(self.num1) * int(self.num2)
        elif self.num1 != "" and self.num2 == "":
            output = self.num1

        self.func = ""
        self.num1 = output
        self.num2 = ""
        self.label1.setText(str(output))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
