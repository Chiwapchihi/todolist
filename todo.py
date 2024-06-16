# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 733)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(139, 69, 19, 255), stop:0.427447 rgba(205, 92, 92, 235), stop:1 rgba(255, 140, 0, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttons_frame = QFrame(self.centralwidget)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setGeometry(QRect(160, 600, 731, 61))
        self.buttons_frame.setStyleSheet(u"background-color: none;")
        self.buttons = QHBoxLayout(self.buttons_frame)
        self.buttons.setObjectName(u"buttons")
        self.pushButton_4 = QPushButton(self.buttons_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}")

        self.buttons.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.buttons_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}")

        self.buttons.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.buttons_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}")

        self.buttons.addWidget(self.pushButton_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 50, 781, 491))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"border: 1px solid rgba(255,255,255,60);\n"
"background-color: rgba(255,255,255,50);\n"
"color: white;\n"
"")

        self.verticalLayout.addWidget(self.tableView)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: none;\n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(24)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"border: 1px solid rgba(255,255,255,60);\n"
"background-color: rgba(255,255,255,50);\n"
"color: white;\n"
"")

        self.verticalLayout.addWidget(self.lineEdit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0442 \u0437\u0430\u0434\u0430\u0447", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u0442\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

