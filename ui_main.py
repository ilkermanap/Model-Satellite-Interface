# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1082, 832)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 50, 1001, 751))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame2 = QFrame(self.layoutWidget)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setMinimumSize(QSize(320, 200))
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame2)

        self.frame1 = QFrame(self.layoutWidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(320, 200))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame1)

        self.btnConnect = QPushButton(Dialog)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setGeometry(QRect(400, 20, 88, 26))
        self.cmbSerialPorts = QComboBox(Dialog)
        self.cmbSerialPorts.setObjectName(u"cmbSerialPorts")
        self.cmbSerialPorts.setGeometry(QRect(50, 20, 201, 26))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(270, 20, 111, 26))
        self.comboBox.setPlaceholderText(u"")

        self.retranslateUi(Dialog)
        self.btnConnect.clicked.connect(Dialog.serial_connect)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btnConnect.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"2400", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"4800", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"9600", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"19200", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"28800", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"38400", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"57600", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"76800", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"115200", None))

    # retranslateUi

