# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sumastaTerminal.ui'
#

# WARNING! All changes made in this file will be lost!

COMPORT=0
BAUDRATE=115200
BYTESIZE=8
STOPBIT=1
TIMEOUT=10

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, serial, serial.tools.list_ports #, warnings
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
import time
#from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QMainWindow, QWidget, QLabel, QTextEdit, QListWidget, QListView
from PyQt5.QtWidgets import QMainWindow
from datetime import datetime

ports = [
    p.device
    for p in serial.tools.list_ports.comports()
        
    if 'USB' in p.description
    ]

#if not ports:
#    raise IOError("No Serial Port Connection")
    

strCOMPORT="/dev/ttyUSB"+str(COMPORT)

ser = serial.Serial(strCOMPORT, BAUDRATE, bytesize=BYTESIZE, parity='N', stopbits=STOPBIT, timeout=TIMEOUT)

class Worker(QObject):
    
    finished = pyqtSignal()
    intReady = pyqtSignal(str)

    @pyqtSlot()
    def __init__(self):
        super(Worker, self).__init__()
        self.working = True

    def work(self):
        while self.working:
            line = ser.readline().decode('utf-8')
            print(line)
            #time.sleep(0.1)
            self.intReady.emit(line)
            # if line != '':
            # self.textEdit_3.append(line)

        self.finished.emit()
        
    

class Ui_MainWindow(QMainWindow):
    
    def __init__(self):

        #QMainWindow.__init__(self)
        super(Ui_MainWindow,self).__init__()
        #loadUi('qt.ui', self)
        self.setupUi()
        # self.comboBox_0.activated.connect(self.load_value0)
        # self.comboBox_1.activated.connect(self.load_value1)
        self.thread = None
        self.worker = None
        #self.pushButton.clicked.connect(self.start_loop)

        
        self.start_loop()
        
    def setupUi(self):
        
        MainWindow.setObjectName("mainWindow")
        MainWindow.resize(506, 700)
        MainWindow.setStyleSheet("background-color: rgb(58, 55, 69);")
        #MainWindow.setWindowTitle("Sumasta Terminal V2.1")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 110, 66, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 550, 341, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(59, 57, 71);\n"
                                    "font: 75 10pt \"Myriad Pro\";\n"
                                    "color:white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(380, 550, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:rgb(172, 40, 48);\n"
                                      "color:white;\n"
                                      "border-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:white;\n"
                                      "")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.sumasta = QtWidgets.QLabel(self.centralwidget)
        self.sumasta.setGeometry(QtCore.QRect(134, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Astro 867")
        font.setPointSize(28)
        self.sumasta.setFont(font)
        self.sumasta.setStyleSheet("color: WHITE;")
        self.sumasta.setObjectName("sumasta")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 150, 441, 381))
        self.textEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                    "color:white;\n"
                                    "font: 75 10pt \"Myriad Pro\";\n"
                                    "")
        self.textEdit.setObjectName("textEdit")
        self.sumasta_2 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_2.setGeometry(QtCore.QRect(300, 20, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Astro 867")
        font.setPointSize(28)
        self.sumasta_2.setFont(font)
        self.sumasta_2.setStyleSheet("color: rgb(172, 40, 48);")
        self.sumasta_2.setObjectName("sumasta_2")
        self.sumasta_3 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_3.setGeometry(QtCore.QRect(40, 90, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sumasta_3.setFont(font)
        self.sumasta_3.setStyleSheet("color: rgb(110, 145, 127);")
        self.sumasta_3.setObjectName("sumasta_3")
        self.sumasta_4 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_4.setGeometry(QtCore.QRect(125, 90, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sumasta_4.setFont(font)
        self.sumasta_4.setStyleSheet("color: rgb(110, 145, 127);")
        self.sumasta_4.setObjectName("sumasta_4")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(100, 110, 106, 31))
        self.lcdNumber_2.setDigitCount(6)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(210, 110, 81, 31))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.sumasta_5 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_5.setGeometry(QtCore.QRect(210, 90, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sumasta_5.setFont(font)
        self.sumasta_5.setStyleSheet("color: rgb(110, 145, 127);")
        self.sumasta_5.setObjectName("sumasta_5")
        self.sumasta_6 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_6.setGeometry(QtCore.QRect(310, 90, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sumasta_6.setFont(font)
        self.sumasta_6.setStyleSheet("color: rgb(110, 145, 127);")
        self.sumasta_6.setObjectName("sumasta_6")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(300, 110, 81, 31))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.sumasta_7 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_7.setGeometry(QtCore.QRect(400, 90, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sumasta_7.setFont(font)
        self.sumasta_7.setStyleSheet("color: rgb(110, 145, 127);")
        self.sumasta_7.setObjectName("sumasta_7")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(390, 110, 81, 31))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.sumasta_8 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_8.setGeometry(QtCore.QRect(144, 60, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Astro 867")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sumasta_8.setFont(font)
        self.sumasta_8.setStyleSheet("color: WHITE;")
        self.sumasta_8.setObjectName("sumasta_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color:rgb(172, 40, 48);\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 600, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color:rgb(172, 40, 48);\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color:rgb(172, 40, 48);\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color:rgb(172, 40, 48);\n"
                                        "color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:white;\n"
                                        "")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.sumasta_9 = QtWidgets.QLabel(self.centralwidget)
        self.sumasta_9.setGeometry(QtCore.QRect(290, 640, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.sumasta_9.setFont(font)
        self.sumasta_9.setStyleSheet("color: WHITE;")
        self.sumasta_9.setObjectName("sumasta_9")
        self.sumasta_8.raise_()
        self.lcdNumber.raise_()
        self.textEdit_2.raise_()
        self.pushButton.raise_()
        self.sumasta.raise_()
        self.textEdit.raise_()
        self.sumasta_2.raise_()
        self.sumasta_3.raise_()
        self.sumasta_4.raise_()
        self.lcdNumber_2.raise_()
        self.lcdNumber_3.raise_()
        self.sumasta_5.raise_()
        self.sumasta_6.raise_()
        self.lcdNumber_4.raise_()
        self.sumasta_7.raise_()
        self.lcdNumber_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.sumasta_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sumasta Terminal V2.1"))
        self.pushButton.setText(_translate("MainWindow", "SEND"))
        self.sumasta.setText(_translate("MainWindow", "sumasta"))
        self.sumasta_2.setText(_translate("MainWindow", "t"))
        self.sumasta_3.setText(_translate("MainWindow", "COM"))
        self.sumasta_4.setText(_translate("MainWindow", "BAUD"))
        self.sumasta_5.setText(_translate("MainWindow", "BY.SIZE"))
        self.sumasta_6.setText(_translate("MainWindow", "ST.BIT"))
        self.sumasta_7.setText(_translate("MainWindow", "T.OUT"))
        self.sumasta_8.setText(_translate("MainWindow", "T  E  r  M  i  N  a  L"))
        self.pushButton_2.setText(_translate("MainWindow", "Send file"))
        self.pushButton_3.setText(_translate("MainWindow", "Save Output"))
        self.pushButton_4.setText(_translate("MainWindow", "Upload Program"))
        self.pushButton_5.setText(_translate("MainWindow", "Close"))
        self.sumasta_9.setText(_translate("MainWindow", "Copyright: Pamungkas Sumasta 2018"))
    
    def loop_finished(self):
        
        print('Looped Finished')
        
    def start_loop(self):

        self.worker = Worker()  # a new worker to perform those tasks
        self.thread = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(
        self.thread)  # move the worker into the thread, do this first before connecting the signals

        self.thread.started.connect(self.worker.work)
        # begin our worker object's loop when the thread starts running

        self.worker.intReady.connect(self.onIntReady)

        self.pushButton_5.clicked.connect(self.stop_loop)  # stop the loop on the stop button click
        self.pushButton.clicked.connect(self.sendData)
        
        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)  # tell the thread it's time to stop running
        
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        
        # make sure those last two are connected to themselves or you will get random crashes
        self.thread.start()
        
        self.textEdit_2.keyPressEvent = self.keyPressEvent
        
        self.lcdNumber.display(COMPORT)
        self.lcdNumber_2.display(BAUDRATE)
        self.lcdNumber_3.display(BYTESIZE)
        self.lcdNumber_4.display(STOPBIT)
        self.lcdNumber_5.display(TIMEOUT)
        #self.lcdNumber_2.adjustSize()
    
    def keyPressEvent(self, e):
        print("event", e)
        try:
            if e.key()  == QtCore.Qt.Key_Return:
                print(' ENTER PRESSED')
                textToSend=self.textEdit_2.toPlainText()
                ser.write(textToSend.encode())
                self.textEdit_2.setText('')
                
                dateTimeObj = datetime.now()
                
                redText = "<span style=\" font-type: Myriad Pro; font-size:10pt; font-weight:600; color:#6E917F;\" >"
                redText += "SENT: " + textToSend +" ("+str(dateTimeObj)+")"
                redText += "</span>"
    
                self.textEdit.append("{}".format(redText))
                
            elif e.key() == QtCore.Qt.Key_Backspace : #backspace
                print("DEL")
                textLength=len(self.textEdit_2.toPlainText())
                tempString=self.textEdit_2.toPlainText()[:textLength-1]
                self.textEdit_2.setText(tempString)    
            else:    
                print(e.key())
                text=self.textEdit_2.toPlainText()+chr(e.key())
                self.textEdit_2.setText(text)
        except ValueError:
            pass
             
    
    def closeEvent(self, event):
        print ("Closing")
        if ser.isOpen:
            ser.close()
            

    def stop_loop(self):
        if ser.isOpen:
            ser.close()
            redText = "<span style=\" font-type: Myriad Pro; font-size:10pt; font-weight:600; color:red;\" >"
            redText += "SERIAL PORT " + str(COMPORT) + " CLOSED"
            redText += "</span>"
            self.textEdit.append("{}".format(redText))
            
        self.worker.working = False

    def onIntReady(self, i):
        self.textEdit.append("{}".format(i))
        #print(i)
        
    def sendData(self):
        
        #self.textEdit.setText("update");
        textToSend=self.textEdit_2.toPlainText()
        ser.write(textToSend.encode())
        self.textEdit_2.setText('')


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
