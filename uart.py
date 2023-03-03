from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
import sys
import qrc_rc

class Ui_WesTech(object):
    def setupUi(self, WesTech):
        WesTech.setObjectName("WesTech")
        WesTech.resize(1432, 899)
        icon = QtGui.QIcon.fromTheme(":/logo/westech logo.svg")
        WesTech.setWindowIcon(icon)
        WesTech.setStyleSheet("#interfaceFrame{\n"
                              "background-color: #663399;\n"
                              "}\n"
                              "\n"
                              "QWidget{\n"
                              "background-color: #d6d6d6;\n"
                              "}\n"
                              "")
        self.centralwidget = QtWidgets.QWidget(WesTech)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.interfaceFrame = QtWidgets.QFrame(self.centralwidget)
        self.interfaceFrame.setMinimumSize(QtCore.QSize(1432, 848))
        self.interfaceFrame.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);")
        self.interfaceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.interfaceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.interfaceFrame.setObjectName("interfaceFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.interfaceFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.interfaceWidget = QtWidgets.QWidget(self.interfaceFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.interfaceWidget.sizePolicy().hasHeightForWidth())
        self.interfaceWidget.setSizePolicy(sizePolicy)
        self.interfaceWidget.setMinimumSize(QtCore.QSize(20, 180))
        self.interfaceWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(43, 0, 86, 255), stop:1 rgba(102, 51, 153, 255));\n"
                                           "\n"
                                           "border-radius: 15px;")
        self.interfaceWidget.setObjectName("interfaceWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.interfaceWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.logoBpKameraGps = QtWidgets.QWidget(self.interfaceWidget)
        self.logoBpKameraGps.setMaximumSize(QtCore.QSize(3000000, 300000))
        self.logoBpKameraGps.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                           "border-radius: 15px;")
        self.logoBpKameraGps.setObjectName("logoBpKameraGps")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.logoBpKameraGps)
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(10, 10, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logoTakimNoBg = QtWidgets.QWidget(self.logoBpKameraGps)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.logoTakimNoBg.sizePolicy().hasHeightForWidth())
        self.logoTakimNoBg.setSizePolicy(sizePolicy)
        self.logoTakimNoBg.setStyleSheet("background-color:#d6d6d6;\n"
                                         "border-radius: 15px;")
        self.logoTakimNoBg.setObjectName("logoTakimNoBg")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.logoTakimNoBg)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.L = QtWidgets.QWidget(self.logoTakimNoBg)
        self.L.setMaximumSize(QtCore.QSize(250, 250))
        self.L.setStyleSheet("background-color: #d6d6d6;\n"
                             "border-radius: 15px;")
        self.L.setObjectName("L")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.L)
        self.verticalLayout_20.setContentsMargins(40, 20, 40, 20)
        self.verticalLayout_20.setSpacing(20)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.logo = QtWidgets.QLabel(self.L)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.logo.setFont(font)
        self.logo.setLineWidth(1)
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.RichText)
        self.logo.setPixmap(QtGui.QPixmap(":/logo/westech logo.svg"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_20.addWidget(self.logo)
        self.takimNo = QtWidgets.QLabel(self.L)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.takimNo.setFont(font)
        self.takimNo.setAlignment(QtCore.Qt.AlignCenter)
        self.takimNo.setIndent(-1)
        self.takimNo.setObjectName("takimNo")
        self.verticalLayout_20.addWidget(self.takimNo)
        self.horizontalLayout_3.addWidget(self.L)
        self.horizontalLayout_2.addWidget(self.logoTakimNoBg)
        self.baglantiPaneli = QtWidgets.QWidget(self.logoBpKameraGps)
        self.baglantiPaneli.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                          "border-radius: 15px;")
        self.baglantiPaneli.setLocale(QtCore.QLocale(
            QtCore.QLocale.Azerbaijani, QtCore.QLocale.Azerbaijan))
        self.baglantiPaneli.setObjectName("baglantiPaneli")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.baglantiPaneli)
        self.verticalLayout_5.setContentsMargins(5, 7, 5, 7)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBp = QtWidgets.QLabel(self.baglantiPaneli)
        self.textBp.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.textBp.setFont(font)
        self.textBp.setStyleSheet("margin: 5px;")
        self.textBp.setAlignment(QtCore.Qt.AlignCenter)
        self.textBp.setObjectName("textBp")
        self.verticalLayout_5.addWidget(self.textBp)
        self.ipBg = QtWidgets.QWidget(self.baglantiPaneli)
        self.ipBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                "border-radius: 7px;\n"
                                "\n"
                                "border-top-left-radius: 10px;\n"
                                "border-top-right-radius: 10px;\n"
                                "border-bottom-left-radius: 0px;\n"
                                "border-bottom-right-radius: 0px;")
        self.ipBg.setObjectName("ipBg")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ipBg)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ipText = QtWidgets.QLabel(self.ipBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.ipText.setFont(font)
        self.ipText.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "")
        self.ipText.setObjectName("ipText")
        self.verticalLayout_6.addWidget(self.ipText)
        self.ipInput = QtWidgets.QLineEdit(self.ipBg)
        self.ipInput.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                   "border-radius: 15px;")
        self.ipInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ipInput.setInputMask("")
        self.ipInput.setText("")
        self.ipInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ipInput.setObjectName("ipInput")
        self.verticalLayout_6.addWidget(self.ipInput)
        self.verticalLayout_5.addWidget(self.ipBg)
        self.portBg = QtWidgets.QWidget(self.baglantiPaneli)
        self.portBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                  "border-radius: 7px;\n"
                                  "border-radius: 0px;")
        self.portBg.setObjectName("portBg")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.portBg)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.portText = QtWidgets.QLabel(self.portBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.portText.setFont(font)
        self.portText.setStyleSheet("color: rgb(255, 255, 255);")
        self.portText.setObjectName("portText")
        self.verticalLayout_28.addWidget(self.portText)
        self.portInput = QtWidgets.QComboBox(self.portBg)
        self.portInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.portInput.setStyleSheet("color: black;\n"
                                     "background-color: #d6d6d6;\n"
                                     "border-radius: 0px;")
        self.portInput.setObjectName("portInput")
        self.verticalLayout_28.addWidget(self.portInput)
        self.verticalLayout_5.addWidget(self.portBg)
        self.baudrateBg = QtWidgets.QWidget(self.baglantiPaneli)
        self.baudrateBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                      "border-radius: 7px;\n"
                                      "\n"
                                      "border-top-left-radius: 0px;\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 10px;\n"
                                      "border-bottom-right-radius: 10px;")
        self.baudrateBg.setObjectName("baudrateBg")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.baudrateBg)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.baudrateText = QtWidgets.QLabel(self.baudrateBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.baudrateText.setFont(font)
        self.baudrateText.setStyleSheet("color: rgb(255, 255, 255);")
        self.baudrateText.setObjectName("baudrateText")
        self.verticalLayout_24.addWidget(self.baudrateText)
        self.baudrateInput = QtWidgets.QComboBox(self.baudrateBg)
        self.baudrateInput.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.baudrateInput.setStyleSheet("color: black;\n"
                                         "background-color: #d6d6d6;\n"
                                         "border-radius: 0px;")
        self.baudrateInput.setObjectName("baudrateInput")
        self.verticalLayout_24.addWidget(self.baudrateInput)
        self.verticalLayout_5.addWidget(self.baudrateBg)
        self.horizontalLayout_2.addWidget(self.baglantiPaneli)
        self.kameraBg = QtWidgets.QWidget(self.logoBpKameraGps)
        self.kameraBg.setStyleSheet("background-color:#d6d6d6;\n"
                                    "border-radius: 15px;")
        self.kameraBg.setObjectName("kameraBg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.kameraBg)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kameraFrame = QtWidgets.QFrame(self.kameraBg)
        self.kameraFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.kameraFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.kameraFrame.setObjectName("kameraFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.kameraFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.kameraText = QtWidgets.QLabel(self.kameraFrame)
        self.kameraText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.kameraText.setFont(font)
        self.kameraText.setAlignment(QtCore.Qt.AlignCenter)
        self.kameraText.setObjectName("kameraText")
        self.verticalLayout_4.addWidget(self.kameraText)
        self.kamera = QtWidgets.QWidget(self.kameraFrame)
        self.kamera.setMinimumSize(QtCore.QSize(0, 200))
        self.kamera.setStyleSheet("background-color:black;\n"
                                  "border-radius: 15px;")
        self.kamera.setObjectName("kamera")
        self.verticalLayout_4.addWidget(self.kamera)
        self.verticalLayout.addWidget(self.kameraFrame)
        self.horizontalLayout_2.addWidget(self.kameraBg)
        self.gpsBg = QtWidgets.QWidget(self.logoBpKameraGps)
        self.gpsBg.setStyleSheet("background-color:#d6d6d6;\n"
                                 "border-radius: 15px;")
        self.gpsBg.setObjectName("gpsBg")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.gpsBg)
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_5 = QtWidgets.QFrame(self.gpsBg)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.gpsText = QtWidgets.QLabel(self.frame_5)
        self.gpsText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.gpsText.setFont(font)
        self.gpsText.setAlignment(QtCore.Qt.AlignCenter)
        self.gpsText.setObjectName("gpsText")
        self.verticalLayout_23.addWidget(self.gpsText)
        self.gps = QtWidgets.QWidget(self.frame_5)
        self.gps.setMinimumSize(QtCore.QSize(0, 100))
        self.gps.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.gps.setStyleSheet("background-color:black;\n"
                               "border-radius: 15px;")
        self.gps.setObjectName("gps")
        self.verticalLayout_23.addWidget(self.gps)
        self.verticalLayout_22.addWidget(self.frame_5)
        self.horizontalLayout_2.addWidget(self.gpsBg)
        self.horizontalLayout_2.setStretch(2, 4)
        self.horizontalLayout_2.setStretch(3, 4)
        self.gridLayout_4.addWidget(self.logoBpKameraGps, 0, 0, 1, 1)
        self.buttonsChartBg = QtWidgets.QWidget(self.interfaceWidget)
        self.buttonsChartBg.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);")
        self.buttonsChartBg.setObjectName("buttonsChartBg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonsChartBg)
        self.horizontalLayout.setContentsMargins(5, 1, 5, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonsTerminal = QtWidgets.QWidget(self.buttonsChartBg)
        self.buttonsTerminal.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                           "border-radius: 15px;")
        self.buttonsTerminal.setObjectName("buttonsTerminal")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.buttonsTerminal)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttonBg = QtWidgets.QWidget(self.buttonsTerminal)
        self.buttonBg.setStyleSheet("background-color:#d6d6d6;")
        self.buttonBg.setObjectName("buttonBg")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.buttonBg)
        self.gridLayout_2.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buzzerBtn = QtWidgets.QPushButton(self.buttonBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buzzerBtn.sizePolicy().hasHeightForWidth())
        self.buzzerBtn.setSizePolicy(sizePolicy)
        self.buzzerBtn.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.buzzerBtn.setFont(font)
        self.buzzerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buzzerBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                     "border-radius: 7px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "\n"
                                     "background-color: #331951;\n"
                                     "\n"
                                     "}")
        self.buzzerBtn.setObjectName("buzzerBtn")
        self.gridLayout_2.addWidget(self.buzzerBtn, 2, 0, 1, 1)
        self.gyroBtn_2 = QtWidgets.QPushButton(self.buttonBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gyroBtn_2.sizePolicy().hasHeightForWidth())
        self.gyroBtn_2.setSizePolicy(sizePolicy)
        self.gyroBtn_2.setMinimumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.gyroBtn_2.setFont(font)
        self.gyroBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gyroBtn_2.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                     "border-radius: 7px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "\n"
                                     "background-color: #331951;\n"
                                     "\n"
                                     "}")
        self.gyroBtn_2.setObjectName("gyroBtn_2")
        self.gridLayout_2.addWidget(self.gyroBtn_2, 4, 0, 1, 1)
        self.gpsBtn = QtWidgets.QPushButton(self.buttonBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gpsBtn.sizePolicy().hasHeightForWidth())
        self.gpsBtn.setSizePolicy(sizePolicy)
        self.gpsBtn.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.gpsBtn.setFont(font)
        self.gpsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gpsBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                  "border-radius: 7px;\n"
                                  "color: white;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "\n"
                                  "background-color: #331951;\n"
                                  "\n"
                                  "}")
        self.gpsBtn.setObjectName("gpsBtn")
        self.gridLayout_2.addWidget(self.gpsBtn, 2, 1, 1, 1)
        self.kameraBtn = QtWidgets.QPushButton(self.buttonBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.kameraBtn.sizePolicy().hasHeightForWidth())
        self.kameraBtn.setSizePolicy(sizePolicy)
        self.kameraBtn.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.kameraBtn.setFont(font)
        self.kameraBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kameraBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                     "border-radius: 7px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "\n"
                                     "background-color: #331951;\n"
                                     "\n"
                                     "}")
        self.kameraBtn.setObjectName("kameraBtn")
        self.gridLayout_2.addWidget(self.kameraBtn, 3, 0, 1, 1)
        self.gyroBtn = QtWidgets.QPushButton(self.buttonBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gyroBtn.sizePolicy().hasHeightForWidth())
        self.gyroBtn.setSizePolicy(sizePolicy)
        self.gyroBtn.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.gyroBtn.setFont(font)
        self.gyroBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gyroBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                   "border-radius: 7px;\n"
                                   "color: white;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "\n"
                                   "background-color: #331951;\n"
                                   "\n"
                                   "}")
        self.gyroBtn.setObjectName("gyroBtn")
        self.gridLayout_2.addWidget(self.gyroBtn, 3, 1, 1, 1)
        self.ayrilBtn = QtWidgets.QPushButton(self.buttonBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ayrilBtn.sizePolicy().hasHeightForWidth())
        self.ayrilBtn.setSizePolicy(sizePolicy)
        self.ayrilBtn.setMinimumSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.ayrilBtn.setFont(font)
        self.ayrilBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ayrilBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                    "border-radius: 7px;\n"
                                    "color: white;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "\n"
                                    "background-color: #331951;\n"
                                    "\n"
                                    "}")
        self.ayrilBtn.setObjectName("ayrilBtn")
        self.gridLayout_2.addWidget(self.ayrilBtn, 4, 1, 1, 1)
        self.baslatBtn = QtWidgets.QPushButton(self.buttonBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.baslatBtn.sizePolicy().hasHeightForWidth())
        self.baslatBtn.setSizePolicy(sizePolicy)
        self.baslatBtn.setMinimumSize(QtCore.QSize(50, 50))
        self.baslatBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.baslatBtn.setSizeIncrement(QtCore.QSize(50, 50))
        self.baslatBtn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.baslatBtn.setFont(font)
        self.baslatBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.baslatBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                     "border-radius: 7px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "\n"
                                     "background-color: #331951;\n"
                                     "\n"
                                     "}")
        self.baslatBtn.setObjectName("baslatBtn")
        self.gridLayout_2.addWidget(self.baslatBtn, 0, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.buttonBg)
        self.terminalBg = QtWidgets.QWidget(self.buttonsTerminal)
        font = QtGui.QFont()
        font.setPointSize(2)
        self.terminalBg.setFont(font)
        self.terminalBg.setStyleSheet("background-color:#d6d6d6;\n"
                                      "border-radius: 15px;")
        self.terminalBg.setObjectName("terminalBg")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.terminalBg)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_4 = QtWidgets.QFrame(self.terminalBg)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.terminalText = QtWidgets.QLabel(self.frame_4)
        self.terminalText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.terminalText.setFont(font)
        self.terminalText.setStyleSheet("")
        self.terminalText.setMidLineWidth(0)
        self.terminalText.setAlignment(QtCore.Qt.AlignCenter)
        self.terminalText.setIndent(-1)
        self.terminalText.setObjectName("terminalText")
        self.verticalLayout_11.addWidget(self.terminalText)
        self.terminal = QtWidgets.QWidget(self.frame_4)
        self.terminal.setMinimumSize(QtCore.QSize(0, 200))
        self.terminal.setStyleSheet("background-color:black;\n"
                                    "border-radius: 15px;\n"
                                    "")
        self.terminal.setObjectName("terminal")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.terminal)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.commandInput = QtWidgets.QLineEdit(self.terminal)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(7)
        self.commandInput.setFont(font)
        self.commandInput.setStyleSheet("background-color: #d6d6d6;\n"
                                        "color: black;\n"
                                        "border-radius: 2px;\n"
                                        "padding: 2px;")
        self.commandInput.setText("")
        self.commandInput.setObjectName("commandInput")
        self.gridLayout_7.addWidget(self.commandInput, 1, 0, 1, 1)
        self.sendCommand = QtWidgets.QPushButton(self.terminal)
        self.sendCommand.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendCommand.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                       "\n"
                                       "")
        self.sendCommand.setText("")
        icon = QtGui.QIcon.fromTheme(":/logo/sendicon.png")
        self.sendCommand.setIcon(icon)
        self.sendCommand.setIconSize(QtCore.QSize(22, 22))
        self.sendCommand.setObjectName("sendCommand")
        self.gridLayout_7.addWidget(self.sendCommand, 1, 1, 1, 1)
        self.terminalBrowser = QtWidgets.QTextBrowser(self.terminal)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.terminalBrowser.setFont(font)
        self.terminalBrowser.setStyleSheet("QTextBrowser{color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(0, 0, 0);}\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "QTextBrowser QScrollBar{\n"
                                           "color: red;\n"
                                           "background-color: red;\n"
                                           "width: 30px;\n"
                                           "}")
        self.terminalBrowser.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.terminalBrowser.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.terminalBrowser.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.terminalBrowser.setObjectName("terminalBrowser")
        self.gridLayout_7.addWidget(self.terminalBrowser, 0, 0, 1, 2)
        self.verticalLayout_11.addWidget(self.terminal)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.terminalBg)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.buttonsTerminal)
        self.chartlarBg = QtWidgets.QWidget(self.buttonsChartBg)
        self.chartlarBg.setStyleSheet("background-color: red;\n"
                                      "background-color: rgba(0, 0, 0, 0);\n"
                                      "border-radius: 15px;\n"
                                      "")
        self.chartlarBg.setObjectName("chartlarBg")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.chartlarBg)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sicaklikBg = QtWidgets.QWidget(self.chartlarBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sicaklikBg.sizePolicy().hasHeightForWidth())
        self.sicaklikBg.setSizePolicy(sizePolicy)
        self.sicaklikBg.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                      "border-radius: 10px;")
        self.sicaklikBg.setObjectName("sicaklikBg")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.sicaklikBg)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.sicaklikText = QtWidgets.QLabel(self.sicaklikBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sicaklikText.setFont(font)
        self.sicaklikText.setAlignment(QtCore.Qt.AlignCenter)
        self.sicaklikText.setObjectName("sicaklikText")
        self.verticalLayout_14.addWidget(self.sicaklikText)
        self.sicaklikChart = QtWidgets.QGraphicsView(self.sicaklikBg)
        self.sicaklikChart.setStyleSheet(" background-color: rgba(0, 0, 0, 0);\n"
                                         "border: 2px solid gray;\n"
                                         "border-radius: 3px;")
        self.sicaklikChart.setObjectName("sicaklikChart")
        self.verticalLayout_14.addWidget(self.sicaklikChart)
        self.gridLayout_5.addWidget(self.sicaklikBg, 0, 0, 1, 1)
        self.basinc1Bg = QtWidgets.QWidget(self.chartlarBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.basinc1Bg.sizePolicy().hasHeightForWidth())
        self.basinc1Bg.setSizePolicy(sizePolicy)
        self.basinc1Bg.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                     "border-radius: 10px;")
        self.basinc1Bg.setObjectName("basinc1Bg")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.basinc1Bg)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.basinc1Text = QtWidgets.QLabel(self.basinc1Bg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.basinc1Text.setFont(font)
        self.basinc1Text.setAlignment(QtCore.Qt.AlignCenter)
        self.basinc1Text.setObjectName("basinc1Text")
        self.verticalLayout_19.addWidget(self.basinc1Text)
        self.basinc1Chart = QtWidgets.QGraphicsView(self.basinc1Bg)
        self.basinc1Chart.setStyleSheet(" background-color: rgba(0, 0, 0, 0);\n"
                                        "border: 2px solid gray;\n"
                                        "border-radius: 3px;")
        self.basinc1Chart.setObjectName("basinc1Chart")
        self.verticalLayout_19.addWidget(self.basinc1Chart)
        self.gridLayout_5.addWidget(self.basinc1Bg, 2, 0, 1, 1)
        self.nemBg = QtWidgets.QWidget(self.chartlarBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nemBg.sizePolicy().hasHeightForWidth())
        self.nemBg.setSizePolicy(sizePolicy)
        self.nemBg.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                 "border-radius: 10px;\n"
                                 "")
        self.nemBg.setObjectName("nemBg")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.nemBg)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.nemText = QtWidgets.QLabel(self.nemBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.nemText.setFont(font)
        self.nemText.setAlignment(QtCore.Qt.AlignCenter)
        self.nemText.setObjectName("nemText")
        self.verticalLayout_17.addWidget(self.nemText)
        self.nemChart = QtWidgets.QGraphicsView(self.nemBg)
        self.nemChart.setStyleSheet(" background-color: rgba(0, 0, 0, 0);\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius: 3px;")
        self.nemChart.setObjectName("nemChart")
        self.verticalLayout_17.addWidget(self.nemChart)
        self.gridLayout_5.addWidget(self.nemBg, 1, 1, 1, 1)
        self.hizBg = QtWidgets.QWidget(self.chartlarBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hizBg.sizePolicy().hasHeightForWidth())
        self.hizBg.setSizePolicy(sizePolicy)
        self.hizBg.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                 "border-radius: 10px;")
        self.hizBg.setObjectName("hizBg")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.hizBg)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.hizText = QtWidgets.QLabel(self.hizBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.hizText.setFont(font)
        self.hizText.setAlignment(QtCore.Qt.AlignCenter)
        self.hizText.setObjectName("hizText")
        self.verticalLayout_16.addWidget(self.hizText)
        self.hizChart = QtWidgets.QGraphicsView(self.hizBg)
        self.hizChart.setStyleSheet(" background-color: rgba(0, 0, 0, 0);\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius: 3px;")
        self.hizChart.setObjectName("hizChart")
        self.verticalLayout_16.addWidget(self.hizChart)
        self.gridLayout_5.addWidget(self.hizBg, 1, 0, 1, 1)
        self.basinc2Bg = QtWidgets.QWidget(self.chartlarBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.basinc2Bg.sizePolicy().hasHeightForWidth())
        self.basinc2Bg.setSizePolicy(sizePolicy)
        self.basinc2Bg.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                     "border-radius: 10px;")
        self.basinc2Bg.setObjectName("basinc2Bg")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.basinc2Bg)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.basinc2Text = QtWidgets.QLabel(self.basinc2Bg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.basinc2Text.setFont(font)
        self.basinc2Text.setAlignment(QtCore.Qt.AlignCenter)
        self.basinc2Text.setObjectName("basinc2Text")
        self.verticalLayout_18.addWidget(self.basinc2Text)
        self.basinc2Chart = QtWidgets.QGraphicsView(self.basinc2Bg)
        self.basinc2Chart.setStyleSheet(" background-color: rgba(0, 0, 0, 0);\n"
                                        "border: 2px solid gray;\n"
                                        "border-radius: 3px;")
        self.basinc2Chart.setObjectName("basinc2Chart")
        self.verticalLayout_18.addWidget(self.basinc2Chart)
        self.gridLayout_5.addWidget(self.basinc2Bg, 2, 1, 1, 1)
        self.widget_27 = QtWidgets.QWidget(self.chartlarBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy)
        self.widget_27.setStyleSheet("background-color: rgb(214, 214, 214);\n"
                                     "border-radius: 10px;")
        self.widget_27.setObjectName("widget_27")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_27)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_24 = QtWidgets.QLabel(self.widget_27)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_15.addWidget(self.label_24)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget_27)
        self.graphicsView_2.setStyleSheet(" background-color: rgba(0, 0, 0, 0);\n"
                                          "border: 2px solid gray;\n"
                                          "border-radius: 3px;")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_15.addWidget(self.graphicsView_2)
        self.gridLayout_5.addWidget(self.widget_27, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.chartlarBg)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.gridLayout_4.addWidget(self.buttonsChartBg, 1, 0, 2, 1)
        self.gyroHatalarSaatDosya = QtWidgets.QWidget(self.interfaceWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gyroHatalarSaatDosya.sizePolicy().hasHeightForWidth())
        self.gyroHatalarSaatDosya.setSizePolicy(sizePolicy)
        self.gyroHatalarSaatDosya.setMinimumSize(QtCore.QSize(333, 0))
        self.gyroHatalarSaatDosya.setMaximumSize(QtCore.QSize(400, 16777215))
        self.gyroHatalarSaatDosya.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                                "border-radius: 15px;")
        self.gyroHatalarSaatDosya.setObjectName("gyroHatalarSaatDosya")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(
            self.gyroHatalarSaatDosya)
        self.verticalLayout_9.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(5, 10, 10, 10)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gyroBg = QtWidgets.QWidget(self.gyroHatalarSaatDosya)
        self.gyroBg.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.gyroBg.setObjectName("gyroBg")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.gyroBg)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gyroText = QtWidgets.QLabel(self.gyroBg)
        self.gyroText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.gyroText.setFont(font)
        self.gyroText.setAlignment(QtCore.Qt.AlignCenter)
        self.gyroText.setObjectName("gyroText")
        self.verticalLayout_12.addWidget(self.gyroText)
        self.gyro = QtWidgets.QWidget(self.gyroBg)
        self.gyro.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.gyro.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "border-bottom-left-radius: 0px;\n"
                                "border-bottom-right-radius: 0px;\n"
                                "margin-top: 6px;")
        self.gyro.setObjectName("gyro")
        self.verticalLayout_12.addWidget(self.gyro)
        self.gyroInputbg = QtWidgets.QWidget(self.gyroBg)
        self.gyroInputbg.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyroInputbg.setFont(font)
        self.gyroInputbg.setStyleSheet("background-color: rgb(118, 90, 154);\n"
                                       "border-top-left-radius: 0px;\n"
                                       "border-top-right-radius: 0px;")
        self.gyroInputbg.setObjectName("gyroInputbg")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gyroInputbg)
        self.gridLayout_3.setContentsMargins(10, 5, 5, 7)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.xText = QtWidgets.QLabel(self.gyroInputbg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.xText.setFont(font)
        self.xText.setStyleSheet("color: rgb(255, 255, 255);")
        self.xText.setObjectName("xText")
        self.gridLayout_3.addWidget(self.xText, 0, 0, 1, 1)
        self.xInput = QtWidgets.QLabel(self.gyroInputbg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.xInput.setFont(font)
        self.xInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.xInput.setObjectName("xInput")
        self.gridLayout_3.addWidget(self.xInput, 0, 1, 1, 1)
        self.yText = QtWidgets.QLabel(self.gyroInputbg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.yText.setFont(font)
        self.yText.setStyleSheet("color: rgb(255, 255, 255);")
        self.yText.setObjectName("yText")
        self.gridLayout_3.addWidget(self.yText, 1, 0, 1, 1)
        self.yInput = QtWidgets.QLabel(self.gyroInputbg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.yInput.setFont(font)
        self.yInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.yInput.setObjectName("yInput")
        self.gridLayout_3.addWidget(self.yInput, 1, 1, 1, 1)
        self.zText = QtWidgets.QLabel(self.gyroInputbg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.zText.setFont(font)
        self.zText.setStyleSheet("color: rgb(255, 255, 255);")
        self.zText.setObjectName("zText")
        self.gridLayout_3.addWidget(self.zText, 2, 0, 1, 1)
        self.zInput = QtWidgets.QLabel(self.gyroInputbg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.zInput.setFont(font)
        self.zInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.zInput.setObjectName("zInput")
        self.gridLayout_3.addWidget(self.zInput, 2, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 10)
        self.verticalLayout_12.addWidget(self.gyroInputbg)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 2)
        self.verticalLayout_12.setStretch(2, 1)
        self.verticalLayout_9.addWidget(self.gyroBg)
        self.hatalarBg = QtWidgets.QWidget(self.gyroHatalarSaatDosya)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hatalarBg.sizePolicy().hasHeightForWidth())
        self.hatalarBg.setSizePolicy(sizePolicy)
        self.hatalarBg.setStyleSheet("background-color:#d6d6d6;\n"
                                     "border-radius: 15px;")
        self.hatalarBg.setObjectName("hatalarBg")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.hatalarBg)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.hatalarFrame = QtWidgets.QFrame(self.hatalarBg)
        self.hatalarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hatalarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hatalarFrame.setObjectName("hatalarFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.hatalarFrame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.hatalarText = QtWidgets.QLabel(self.hatalarFrame)
        self.hatalarText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.hatalarText.setFont(font)
        self.hatalarText.setAlignment(QtCore.Qt.AlignCenter)
        self.hatalarText.setObjectName("hatalarText")
        self.verticalLayout_8.addWidget(self.hatalarText)
        self.hatalarInputBg = QtWidgets.QWidget(self.hatalarFrame)
        self.hatalarInputBg.setMinimumSize(QtCore.QSize(0, 0))
        self.hatalarInputBg.setStyleSheet("background-color:black;\n"
                                          "border-radius: 10px;")
        self.hatalarInputBg.setObjectName("hatalarInputBg")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.hatalarInputBg)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.hatalarText1 = QtWidgets.QLabel(self.hatalarInputBg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.hatalarText1.setFont(font)
        self.hatalarText1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "")
        self.hatalarText1.setAlignment(QtCore.Qt.AlignCenter)
        self.hatalarText1.setObjectName("hatalarText1")
        self.gridLayout_6.addWidget(self.hatalarText1, 0, 0, 1, 1)
        self.hatalarText2 = QtWidgets.QLabel(self.hatalarInputBg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.hatalarText2.setFont(font)
        self.hatalarText2.setStyleSheet("color: rgb(255, 255, 255);")
        self.hatalarText2.setAlignment(QtCore.Qt.AlignCenter)
        self.hatalarText2.setObjectName("hatalarText2")
        self.gridLayout_6.addWidget(self.hatalarText2, 0, 1, 1, 1)
        self.hatalarText4 = QtWidgets.QLabel(self.hatalarInputBg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.hatalarText4.setFont(font)
        self.hatalarText4.setStyleSheet("color: rgb(255, 255, 255);")
        self.hatalarText4.setAlignment(QtCore.Qt.AlignCenter)
        self.hatalarText4.setObjectName("hatalarText4")
        self.gridLayout_6.addWidget(self.hatalarText4, 0, 3, 1, 1)
        self.hatalarText5 = QtWidgets.QLabel(self.hatalarInputBg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.hatalarText5.setFont(font)
        self.hatalarText5.setStyleSheet("color: rgb(255, 255, 255);")
        self.hatalarText5.setAlignment(QtCore.Qt.AlignCenter)
        self.hatalarText5.setObjectName("hatalarText5")
        self.gridLayout_6.addWidget(self.hatalarText5, 0, 4, 1, 1)
        self.hatalarText3 = QtWidgets.QLabel(self.hatalarInputBg)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.hatalarText3.setFont(font)
        self.hatalarText3.setStyleSheet("color: rgb(255, 255, 255);")
        self.hatalarText3.setAlignment(QtCore.Qt.AlignCenter)
        self.hatalarText3.setObjectName("hatalarText3")
        self.gridLayout_6.addWidget(self.hatalarText3, 0, 2, 1, 1)
        self.hatalar1input = QtWidgets.QWidget(self.hatalarInputBg)
        self.hatalar1input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 5px;\n"
                                         "border-color: red;\n"
                                         "border-width: 5px;")
        self.hatalar1input.setObjectName("hatalar1input")
        self.gridLayout_6.addWidget(self.hatalar1input, 1, 0, 1, 1)
        self.hatalar4input = QtWidgets.QWidget(self.hatalarInputBg)
        self.hatalar4input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 5px;\n"
                                         "border-color: red;\n"
                                         "border-width: 5px;")
        self.hatalar4input.setObjectName("hatalar4input")
        self.gridLayout_6.addWidget(self.hatalar4input, 1, 3, 1, 1)
        self.hatalar3input = QtWidgets.QWidget(self.hatalarInputBg)
        self.hatalar3input.setStyleSheet("background-color: white;\n"
                                         "border-radius: 5px;\n"
                                         "border-color: red;\n"
                                         "border-width: 5px;")
        self.hatalar3input.setObjectName("hatalar3input")
        self.gridLayout_6.addWidget(self.hatalar3input, 1, 2, 1, 1)
        self.hatalar2input = QtWidgets.QWidget(self.hatalarInputBg)
        self.hatalar2input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 5px;\n"
                                         "border-color: red;\n"
                                         "border-width: 5px;")
        self.hatalar2input.setObjectName("hatalar2input")
        self.gridLayout_6.addWidget(self.hatalar2input, 1, 1, 1, 1)
        self.hatalar5input = QtWidgets.QWidget(self.hatalarInputBg)
        self.hatalar5input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 5px;\n"
                                         "border-color: red;\n"
                                         "border-width: 5px;")
        self.hatalar5input.setObjectName("hatalar5input")
        self.gridLayout_6.addWidget(self.hatalar5input, 1, 4, 1, 1)
        self.verticalLayout_8.addWidget(self.hatalarInputBg)
        self.verticalLayout_7.addWidget(self.hatalarFrame)
        self.verticalLayout_9.addWidget(self.hatalarBg)
        self.saatUmumiBg = QtWidgets.QWidget(self.gyroHatalarSaatDosya)
        self.saatUmumiBg.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.saatUmumiBg.setObjectName("saatUmumiBg")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.saatUmumiBg)
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.saatBg_2 = QtWidgets.QWidget(self.saatUmumiBg)
        self.saatBg_2.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                    "\n"
                                    "border-top-left-radius: 15px;\n"
                                    "border-top-right-radius: 15px;\n"
                                    "border-bottom-left-radius: 0px;\n"
                                    "border-bottom-right-radius: 0px;")
        self.saatBg_2.setObjectName("saatBg_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.saatBg_2)
        self.horizontalLayout_9.setContentsMargins(7, 3, 7, 3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.saat = QtWidgets.QLabel(self.saatBg_2)
        self.saat.setMinimumSize(QtCore.QSize(80, 0))
        self.saat.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.saat.setFont(font)
        self.saat.setStyleSheet("color: rgb(255, 255, 255);")
        self.saat.setScaledContents(True)
        self.saat.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.saat.setObjectName("saat")
        self.horizontalLayout_9.addWidget(self.saat)
        self.saatInput = QtWidgets.QLabel(self.saatBg_2)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.saatInput.setFont(font)
        self.saatInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.saatInput.setScaledContents(True)
        self.saatInput.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.saatInput.setObjectName("saatInput")
        self.horizontalLayout_9.addWidget(self.saatInput)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 7)
        self.verticalLayout_13.addWidget(self.saatBg_2)
        self.baslangicBg = QtWidgets.QWidget(self.saatUmumiBg)
        self.baslangicBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                       "\n"
                                       "border-radius: 0px;")
        self.baslangicBg.setObjectName("baslangicBg")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.baslangicBg)
        self.horizontalLayout_8.setContentsMargins(7, 3, 7, 3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.baslangic = QtWidgets.QLabel(self.baslangicBg)
        self.baslangic.setMinimumSize(QtCore.QSize(80, 0))
        self.baslangic.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.baslangic.setFont(font)
        self.baslangic.setStyleSheet("color: rgb(255, 255, 255);")
        self.baslangic.setScaledContents(True)
        self.baslangic.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.baslangic.setObjectName("baslangic")
        self.horizontalLayout_8.addWidget(self.baslangic)
        self.baslangicInput = QtWidgets.QLabel(self.baslangicBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.baslangicInput.setFont(font)
        self.baslangicInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.baslangicInput.setScaledContents(True)
        self.baslangicInput.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.baslangicInput.setObjectName("baslangicInput")
        self.horizontalLayout_8.addWidget(self.baslangicInput)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 7)
        self.verticalLayout_13.addWidget(self.baslangicBg)
        self.ayrilmaBg = QtWidgets.QWidget(self.saatUmumiBg)
        self.ayrilmaBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                     "border-radius: 0px;")
        self.ayrilmaBg.setObjectName("ayrilmaBg")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.ayrilmaBg)
        self.horizontalLayout_7.setContentsMargins(7, 3, 7, 3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ayrilma = QtWidgets.QLabel(self.ayrilmaBg)
        self.ayrilma.setMinimumSize(QtCore.QSize(80, 0))
        self.ayrilma.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.ayrilma.setFont(font)
        self.ayrilma.setStyleSheet("color: rgb(255, 255, 255);")
        self.ayrilma.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ayrilma.setObjectName("ayrilma")
        self.horizontalLayout_7.addWidget(self.ayrilma)
        self.ayrilmaInput = QtWidgets.QLabel(self.ayrilmaBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ayrilmaInput.setFont(font)
        self.ayrilmaInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.ayrilmaInput.setScaledContents(True)
        self.ayrilmaInput.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ayrilmaInput.setObjectName("ayrilmaInput")
        self.horizontalLayout_7.addWidget(self.ayrilmaInput)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 7)
        self.verticalLayout_13.addWidget(self.ayrilmaBg)
        self.inisBg = QtWidgets.QWidget(self.saatUmumiBg)
        self.inisBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                  "border-radius: 0px;")
        self.inisBg.setObjectName("inisBg")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.inisBg)
        self.horizontalLayout_6.setContentsMargins(7, 3, 7, 3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.inis = QtWidgets.QLabel(self.inisBg)
        self.inis.setMinimumSize(QtCore.QSize(80, 0))
        self.inis.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.inis.setFont(font)
        self.inis.setStyleSheet("color: rgb(255, 255, 255);")
        self.inis.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.inis.setObjectName("inis")
        self.horizontalLayout_6.addWidget(self.inis)
        self.inisInput = QtWidgets.QLabel(self.inisBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.inisInput.setFont(font)
        self.inisInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.inisInput.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.inisInput.setObjectName("inisInput")
        self.horizontalLayout_6.addWidget(self.inisInput)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 7)
        self.verticalLayout_13.addWidget(self.inisBg)
        self.toplamBg = QtWidgets.QWidget(self.saatUmumiBg)
        self.toplamBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                    "\n"
                                    "border-top-left-radius: 0px;\n"
                                    "border-top-right-radius: 0px;\n"
                                    "border-bottom-left-radius: 15px;\n"
                                    "border-bottom-right-radius: 15px;")
        self.toplamBg.setObjectName("toplamBg")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.toplamBg)
        self.horizontalLayout_5.setContentsMargins(7, 3, 7, 3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.toplam = QtWidgets.QLabel(self.toplamBg)
        self.toplam.setMinimumSize(QtCore.QSize(85, 0))
        self.toplam.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.toplam.setFont(font)
        self.toplam.setStyleSheet("color: rgb(255, 255, 255);")
        self.toplam.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.toplam.setObjectName("toplam")
        self.horizontalLayout_5.addWidget(self.toplam)
        self.toplamInput = QtWidgets.QLabel(self.toplamBg)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.toplamInput.setFont(font)
        self.toplamInput.setStyleSheet("color: rgb(255, 255, 255);")
        self.toplamInput.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.toplamInput.setObjectName("toplamInput")
        self.horizontalLayout_5.addWidget(self.toplamInput)
        self.horizontalLayout_5.setStretch(0, 1)
        self.verticalLayout_13.addWidget(self.toplamBg)
        self.verticalLayout_9.addWidget(self.saatUmumiBg)
        self.dosyaSecimBg = QtWidgets.QWidget(self.gyroHatalarSaatDosya)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dosyaSecimBg.sizePolicy().hasHeightForWidth())
        self.dosyaSecimBg.setSizePolicy(sizePolicy)
        self.dosyaSecimBg.setStyleSheet(
            "background-color: rgb(214, 214, 214);")
        self.dosyaSecimBg.setObjectName("dosyaSecimBg")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.dosyaSecimBg)
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.dosyaAdiBg = QtWidgets.QWidget(self.dosyaSecimBg)
        self.dosyaAdiBg.setStyleSheet("background-color: rgb(102, 51, 153);\n"
                                      "\n"
                                      "border-top-left-radius: 10px;\n"
                                      "border-top-right-radius: 10px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;")
        self.dosyaAdiBg.setObjectName("dosyaAdiBg")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dosyaAdiBg)
        self.horizontalLayout_4.setContentsMargins(5, 5, 7, 5)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dosyaAdiText = QtWidgets.QLabel(self.dosyaAdiBg)
        self.dosyaAdiText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.dosyaAdiText.setFont(font)
        self.dosyaAdiText.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "margin-right: 10px ;")
        self.dosyaAdiText.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.dosyaAdiText.setObjectName("dosyaAdiText")
        self.horizontalLayout_4.addWidget(self.dosyaAdiText)
        self.dosyaAdi = QtWidgets.QLabel(self.dosyaAdiBg)
        self.dosyaAdi.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.dosyaAdi.setFont(font)
        self.dosyaAdi.setStyleSheet("color: rgb(255, 255, 255);")
        self.dosyaAdi.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.dosyaAdi.setObjectName("dosyaAdi")
        self.horizontalLayout_4.addWidget(self.dosyaAdi)
        self.trash = QtWidgets.QLabel(self.dosyaAdiBg)
        self.trash.setMinimumSize(QtCore.QSize(25, 30))
        self.trash.setMaximumSize(QtCore.QSize(25, 30))
        self.trash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trash.setStyleSheet("color: rgb(255, 255, 255);")
        self.trash.setText("")
        self.trash.setPixmap(QtGui.QPixmap(":/logo/trashicon.png"))
        self.trash.setScaledContents(True)
        self.trash.setObjectName("trash")
        self.horizontalLayout_4.addWidget(self.trash)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_21.addWidget(self.dosyaAdiBg)
        self.secGonder = QtWidgets.QHBoxLayout()
        self.secGonder.setSpacing(2)
        self.secGonder.setObjectName("secGonder")
        self.secBtn = QtWidgets.QPushButton(self.dosyaSecimBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.secBtn.sizePolicy().hasHeightForWidth())
        self.secBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.secBtn.setFont(font)
        self.secBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.secBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "\n"
                                  "border-top-left-radius: 0px;\n"
                                  "border-top-right-radius: 0px;\n"
                                  "border-bottom-left-radius: 10px;\n"
                                  "border-bottom-right-radius: 0px;\n"
                                  "\n"
                                  "padding-top: 5px;\n"
                                  "padding-bottom: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {background-color: #331951;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "\n"
                                  "border-top-left-radius: 0px;\n"
                                  "border-top-right-radius: 0px;\n"
                                  "border-bottom-left-radius: 10px;\n"
                                  "border-bottom-right-radius: 0px;\n"
                                  "\n"
                                  "padding-top: 5px;\n"
                                  "padding-bottom: 5px;\n"
                                  "}\n"
                                  "")
        self.secBtn.setObjectName("secBtn")
        self.secGonder.addWidget(self.secBtn)
        self.gonderBtn = QtWidgets.QPushButton(self.dosyaSecimBg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gonderBtn.sizePolicy().hasHeightForWidth())
        self.gonderBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(24)
        self.gonderBtn.setFont(font)
        self.gonderBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gonderBtn.setStyleSheet("QPushButton{background-color: rgb(102, 51, 153);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "border-top-left-radius: 0px;\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 10px;\n"
                                     "\n"
                                     "padding-top: 5px;\n"
                                     "padding-bottom: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{background-color: #331951;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "border-top-left-radius: 0px;\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 10px;\n"
                                     "\n"
                                     "padding-top: 5px;\n"
                                     "padding-bottom: 5px;\n"
                                     "}")
        self.gonderBtn.setObjectName("gonderBtn")
        self.secGonder.addWidget(self.gonderBtn)
        self.verticalLayout_21.addLayout(self.secGonder)
        self.verticalLayout_9.addWidget(self.dosyaSecimBg)
        self.verticalLayout_9.setStretch(0, 5)
        self.verticalLayout_9.setStretch(1, 3)
        self.verticalLayout_9.setStretch(2, 4)
        self.verticalLayout_9.setStretch(3, 2)
        self.gridLayout_4.addWidget(self.gyroHatalarSaatDosya, 0, 1, 3, 1)
        self.verticalLayout_2.addWidget(self.interfaceWidget)
        self.gridLayout.addWidget(self.interfaceFrame, 0, 0, 1, 1)
        WesTech.setCentralWidget(self.centralwidget)

        self.retranslateUi(WesTech)
        QtCore.QMetaObject.connectSlotsByName(WesTech)

    def retranslateUi(self, WesTech):
        _translate = QtCore.QCoreApplication.translate
        WesTech.setWindowTitle(_translate("WesTech", "WesTech Model Uydu"))
        self.takimNo.setText(_translate("WesTech", "TAKIM NO: 202902"))
        self.textBp.setText(_translate("WesTech", "BAĞLANTI PANELİ"))
        self.ipText.setText(_translate("WesTech", "IP:"))
        self.portText.setText(_translate("WesTech", "PORT:"))
        self.baudrateText.setText(_translate("WesTech", "BAUD RATE:"))
        self.kameraText.setText(_translate("WesTech", "KAMERA"))
        self.gpsText.setText(_translate("WesTech", "GPS"))
        self.buzzerBtn.setText(_translate("WesTech", "BUZZER"))
        self.gyroBtn_2.setText(_translate("WesTech", "BASINÇ"))
        self.gpsBtn.setText(_translate("WesTech", "GPS"))
        self.kameraBtn.setText(_translate("WesTech", "KAMERA"))
        self.gyroBtn.setText(_translate("WesTech", "GYRO"))
        self.ayrilBtn.setText(_translate("WesTech", "AYRIL"))
        self.baslatBtn.setText(_translate("WesTech", "BAŞLAT"))
        self.terminalText.setText(_translate("WesTech", "TERMİNAL"))
        self.terminalBrowser.setHtml(_translate("WesTech", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</body></html>"))
        self.sicaklikText.setText(_translate("WesTech", "SICAKLIK"))
        self.basinc1Text.setText(_translate("WesTech", "BASINÇ_T"))
        self.nemText.setText(_translate("WesTech", "NEM"))
        self.hizText.setText(_translate("WesTech", "HIZ"))
        self.basinc2Text.setText(_translate("WesTech", "BASINÇ_GY"))
        self.label_24.setText(_translate("WesTech", "İVMEÖLÇER"))
        self.gyroText.setText(_translate("WesTech", "GYRO"))
        self.xText.setText(_translate("WesTech", "X:"))
        self.xInput.setText(_translate("WesTech", "123"))
        self.yText.setText(_translate("WesTech", "Y:"))
        self.yInput.setText(_translate("WesTech", "456"))
        self.zText.setText(_translate("WesTech", "Z:"))
        self.zInput.setText(_translate("WesTech", "789"))
        self.hatalarText.setText(_translate("WesTech", "HATALAR"))
        self.hatalarText1.setText(_translate("WesTech", "1"))
        self.hatalarText2.setText(_translate("WesTech", "2"))
        self.hatalarText4.setText(_translate("WesTech", "4"))
        self.hatalarText5.setText(_translate("WesTech", "5"))
        self.hatalarText3.setText(_translate("WesTech", "3"))
        self.saat.setText(_translate("WesTech", "SAAT:"))
        self.saatInput.setText(_translate("WesTech", "13:10"))
        self.baslangic.setText(_translate("WesTech", "BAŞLANĞIÇ:"))
        self.baslangicInput.setText(_translate("WesTech", "12:40"))
        self.ayrilma.setText(_translate("WesTech", "AYRILMA:"))
        self.ayrilmaInput.setText(_translate("WesTech", "12:50"))
        self.inis.setText(_translate("WesTech", "İNİŞ:"))
        self.inisInput.setText(_translate("WesTech", "13:00"))
        self.toplam.setText(_translate("WesTech", "TOPLAM:"))
        self.toplamInput.setText(_translate("WesTech", "1:30"))
        self.dosyaAdiText.setText(_translate("WesTech", "DOSYA ADI:"))
        self.dosyaAdi.setText(_translate("WesTech", ""))
        self.secBtn.setText(_translate("WesTech", "SEÇ"))
        self.gonderBtn.setText(_translate("WesTech", "GÖNDER"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WesTech = QtWidgets.QMainWindow()
    ui = Ui_WesTech()
    ui.setupUi(WesTech)
    WesTech.show()
    sys.exit(app.exec_())