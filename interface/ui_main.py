# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolBox, QVBoxLayout,
    QWidget)
from interface import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 641)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: rgb(191, 191, 189);\n"
"	background-color: rgb(38, 38, 38);\n"
"	font: 57 8pt \"Cy Grotesk Key Medium\";\n"
"	border: none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(0, 0))
        self.left_frame.setMaximumSize(QSize(0, 16777215))
        self.left_frame.setSizeIncrement(QSize(0, 0))
        self.left_frame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.left_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setStyleSheet(u"background-color: rgb(28, 28, 28);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.label_tituloprograma = QLabel(self.frame_2)
        self.label_tituloprograma.setObjectName(u"label_tituloprograma")
        self.label_tituloprograma.setMinimumSize(QSize(0, 0))
        self.label_tituloprograma.setStyleSheet(u"")
        self.label_tituloprograma.setAlignment(Qt.AlignCenter)
        self.label_tituloprograma.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_tituloprograma)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_tool = QFrame(self.left_frame)
        self.frame_tool.setObjectName(u"frame_tool")
        self.frame_tool.setStyleSheet(u"QToolBox{\n"
"	text-align: left;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(38, 38, 38);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	text-align: center;\n"
"	border-radius: 1px;\n"
"	background-color:rgb(13, 122, 217);\n"
"	font: 57 12pt \"Cy Grotesk Key Medium\";	\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QToolBox::tab:pressed {\n"
"    background-color: rgb(5, 175, 242);\n"
"}")
        self.frame_tool.setFrameShape(QFrame.StyledPanel)
        self.frame_tool.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_tool)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolBox_menu = QToolBox(self.frame_tool)
        self.toolBox_menu.setObjectName(u"toolBox_menu")
        self.toolBox_menu.setMinimumSize(QSize(0, 0))
        self.toolBox_menu.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Cy Grotesk Key Medium"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.toolBox_menu.setFont(font)
        self.toolBox_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBox_menu.setLayoutDirection(Qt.LeftToRight)
        self.toolBox_menu.setStyleSheet(u"QPushButton {\n"
"	font: 25 10pt \"Cy Grotesk Key Light\";\n"
"	background-color:rgb(23, 23, 23);\n"
"	border: 1.5px solid rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font: 57 10.5pt \"Cy Grotesk Key Medium\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(12, 135, 242);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(5, 175, 242);\n"
"}\n"
"\n"
"")
        self.toolBox_menu.setLineWidth(1)
        self.page_menu = QWidget()
        self.page_menu.setObjectName(u"page_menu")
        self.page_menu.setGeometry(QRect(0, 0, 117, 508))
        self.verticalLayout_4 = QVBoxLayout(self.page_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_gerar = QPushButton(self.page_menu)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(0, 40))
        self.btn_gerar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_gerar)

        self.btn_cadastrar = QPushButton(self.page_menu)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 40))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox_menu.addItem(self.page_menu, u"Menu")
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.page_sobre.setGeometry(QRect(0, 0, 186, 508))
        self.verticalLayout_5 = QVBoxLayout(self.page_sobre)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_sobre = QLabel(self.page_sobre)
        self.label_sobre.setObjectName(u"label_sobre")
        self.label_sobre.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_sobre)

        self.toolBox_menu.addItem(self.page_sobre, u"Sobre")

        self.verticalLayout_3.addWidget(self.toolBox_menu)


        self.verticalLayout_2.addWidget(self.frame_tool)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_main_frame = QFrame(self.main_frame)
        self.top_main_frame.setObjectName(u"top_main_frame")
        self.top_main_frame.setMinimumSize(QSize(0, 70))
        self.top_main_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(28, 28, 28);\n"
"}\n"
"\n"
"QLabel#label_top{\n"
"	font: 25 11pt \"Cy Grotesk Key Light\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:  rgb(28, 28, 28);\n"
"	image: url(:/icons/icons/Toggle.png);\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(13, 122, 217);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(5, 175, 242);\n"
"}\n"
"")
        self.top_main_frame.setFrameShape(QFrame.StyledPanel)
        self.top_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_main_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.btn_toggle = QPushButton(self.top_main_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(50, 50))
        self.btn_toggle.setMaximumSize(QSize(40, 40))
        self.btn_toggle.setStyleSheet(u"margin:0px;\n"
"padding:0px;")
        self.btn_toggle.setIconSize(QSize(50, 50))
        self.btn_toggle.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_toggle)

        self.label_top = QLabel(self.top_main_frame)
        self.label_top.setObjectName(u"label_top")
        self.label_top.setMinimumSize(QSize(0, 0))
        self.label_top.setStyleSheet(u"")
        self.label_top.setAlignment(Qt.AlignCenter)
        self.label_top.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_top)


        self.verticalLayout.addWidget(self.top_main_frame)

        self.mid_main_frame = QFrame(self.main_frame)
        self.mid_main_frame.setObjectName(u"mid_main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mid_main_frame.sizePolicy().hasHeightForWidth())
        self.mid_main_frame.setSizePolicy(sizePolicy)
        self.mid_main_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.mid_main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.mid_main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout = QGridLayout(self.page_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_logo = QLabel(self.page_home)
        self.label_logo.setObjectName(u"label_logo")

        self.gridLayout.addWidget(self.label_logo, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_gerar = QWidget()
        self.page_gerar.setObjectName(u"page_gerar")
        self.gridLayout_5 = QGridLayout(self.page_gerar)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_titulo_gerarsenha = QLabel(self.page_gerar)
        self.label_titulo_gerarsenha.setObjectName(u"label_titulo_gerarsenha")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_titulo_gerarsenha.sizePolicy().hasHeightForWidth())
        self.label_titulo_gerarsenha.setSizePolicy(sizePolicy1)
        self.label_titulo_gerarsenha.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_titulo_gerarsenha, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_selecionar_gerar = QFrame(self.page_gerar)
        self.frame_selecionar_gerar.setObjectName(u"frame_selecionar_gerar")
        self.frame_selecionar_gerar.setMinimumSize(QSize(0, 80))
        self.frame_selecionar_gerar.setStyleSheet(u"QSpinBox {\n"
"    border-width: 3;\n"
"	border: 2px solid rgb(12, 135, 242);\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"}\n"
"\n"
"QRadioButton{\n"
"	font: 10pt \"Cy Grotesk Key Regular\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_selecionar_gerar.setFrameShape(QFrame.StyledPanel)
        self.frame_selecionar_gerar.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_selecionar_gerar)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.spinBox = QSpinBox(self.frame_selecionar_gerar)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy2)
        self.spinBox.setMinimumSize(QSize(50, 40))
        self.spinBox.setMaximumSize(QSize(0, 16777215))
        self.spinBox.setFont(font)
        self.spinBox.setWrapping(True)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(32)

        self.gridLayout_4.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_qtd_char = QLabel(self.frame_selecionar_gerar)
        self.label_qtd_char.setObjectName(u"label_qtd_char")

        self.gridLayout_4.addWidget(self.label_qtd_char, 0, 0, 1, 1)

        self.btn_radio = QRadioButton(self.frame_selecionar_gerar)
        self.btn_radio.setObjectName(u"btn_radio")
        font1 = QFont()
        font1.setFamilies([u"Cy Grotesk Key Regular"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_radio.setFont(font1)

        self.gridLayout_4.addWidget(self.btn_radio, 2, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_selecionar_gerar)

        self.frame_gerar = QFrame(self.page_gerar)
        self.frame_gerar.setObjectName(u"frame_gerar")
        sizePolicy.setHeightForWidth(self.frame_gerar.sizePolicy().hasHeightForWidth())
        self.frame_gerar.setSizePolicy(sizePolicy)
        self.frame_gerar.setStyleSheet(u"QLabel#label_resultado_gerar {\n"
"	border: 2px solid rgb(12, 135, 242);\n"
"	border-radius: 5px;\n"
"	font: 10pt \"Cy Grotesk Key Regular\";\n"
"	text-align: center;\n"
"}\n"
"\n"
"QLabel#label_resultado_gerar{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_gerar.setFrameShape(QFrame.StyledPanel)
        self.frame_gerar.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_gerar)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.label_resultado_gerar = QLabel(self.frame_gerar)
        self.label_resultado_gerar.setObjectName(u"label_resultado_gerar")
        sizePolicy.setHeightForWidth(self.label_resultado_gerar.sizePolicy().hasHeightForWidth())
        self.label_resultado_gerar.setSizePolicy(sizePolicy)
        self.label_resultado_gerar.setAlignment(Qt.AlignCenter)
        self.label_resultado_gerar.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_resultado_gerar, 1, 0, 1, 1)

        self.label_titulo_resultado = QLabel(self.frame_gerar)
        self.label_titulo_resultado.setObjectName(u"label_titulo_resultado")
        self.label_titulo_resultado.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_titulo_resultado.setWordWrap(False)
        self.label_titulo_resultado.setMargin(0)

        self.gridLayout_3.addWidget(self.label_titulo_resultado, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_gerar)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.frame_btn_gerar = QFrame(self.page_gerar)
        self.frame_btn_gerar.setObjectName(u"frame_btn_gerar")
        self.frame_btn_gerar.setMinimumSize(QSize(0, 0))
        self.frame_btn_gerar.setStyleSheet(u"QPushButton {\n"
"	font: 25 10pt \"Cy Grotesk Key Light\";\n"
"	background-color:rgb(38, 38, 38);\n"
"	border: 2px solid rgb(13, 122, 217);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font: 57 10.5pt \"Cy Grotesk Key Medium\";	\n"
"	background-color: rgb(12, 135, 242);\n"
"	border: 2px solid rgb(59, 61, 64);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(5, 175, 242);\n"
"}")
        self.frame_btn_gerar.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_gerar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_btn_gerar)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 0, 3, 0)
        self.pushButton_8 = QPushButton(self.frame_btn_gerar)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_btn_gerar)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_6.addWidget(self.pushButton_7)


        self.verticalLayout_13.addWidget(self.frame_btn_gerar)


        self.gridLayout_5.addLayout(self.verticalLayout_13, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_gerar)
        self.page_cadastrar = QWidget()
        self.page_cadastrar.setObjectName(u"page_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.page_cadastrar)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.page_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 1px solid rgb(12, 135, 242)\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	\n"
"	font: 8pt \"Cy Grotesk Key Regular\";\n"
"	background-color: rgb(38, 38, 38);\n"
"	border: 1px  solid rgb(13, 122, 217);\n"
"	border-bottom: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	min-width: 28ex;\n"
"	min-height: 7ex; \n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	background-color: rgb(13, 122, 217);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(12, 135, 242);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_titulo_cadastronovasenha = QLabel(self.tab)
        self.label_titulo_cadastronovasenha.setObjectName(u"label_titulo_cadastronovasenha")
        sizePolicy1.setHeightForWidth(self.label_titulo_cadastronovasenha.sizePolicy().hasHeightForWidth())
        self.label_titulo_cadastronovasenha.setSizePolicy(sizePolicy1)
        self.label_titulo_cadastronovasenha.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_titulo_cadastronovasenha)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_cadastro = QFrame(self.tab)
        self.frame_cadastro.setObjectName(u"frame_cadastro")
        sizePolicy.setHeightForWidth(self.frame_cadastro.sizePolicy().hasHeightForWidth())
        self.frame_cadastro.setSizePolicy(sizePolicy)
        self.frame_cadastro.setStyleSheet(u"QLabel{\n"
"	font: 57 10pt \"Cy Grotesk Key Medium\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-bottom: 1px solid rgb(13, 122, 217);\n"
"	font: 9pt \"Cy Grotesk Key Regular\";\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 25 10pt \"Cy Grotesk Key Light\";\n"
"	background-color:rgb(38, 38, 38);\n"
"	border: 1px solid rgb(13, 122, 217);\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font: 57 10.5pt \"Cy Grotesk Key Medium\";	\n"
"	background-color: rgb(12, 135, 242);\n"
"	border: 1px solid rgb(13, 122, 217);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(5, 175, 242);\n"
"}")
        self.frame_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_cadastro)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setContentsMargins(0, 20, -1, -1)
        self.lineEdit_3 = QLineEdit(self.frame_cadastro)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAcceptDrops(False)

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_senha = QLabel(self.frame_cadastro)
        self.label_senha.setObjectName(u"label_senha")

        self.gridLayout_2.addWidget(self.label_senha, 2, 0, 1, 1)

        self.label_email_user = QLabel(self.frame_cadastro)
        self.label_email_user.setObjectName(u"label_email_user")

        self.gridLayout_2.addWidget(self.label_email_user, 1, 0, 1, 1)

        self.label_titulo_novocadastro = QLabel(self.frame_cadastro)
        self.label_titulo_novocadastro.setObjectName(u"label_titulo_novocadastro")

        self.gridLayout_2.addWidget(self.label_titulo_novocadastro, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.btn_colarsenha = QPushButton(self.frame_cadastro)
        self.btn_colarsenha.setObjectName(u"btn_colarsenha")
        self.btn_colarsenha.setMinimumSize(QSize(50, 20))
        self.btn_colarsenha.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.btn_colarsenha, 2, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_cadastro)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 2)

        self.lineEdit = QLineEdit(self.frame_cadastro)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 2)


        self.verticalLayout_10.addWidget(self.frame_cadastro)

        self.frame_btn_cadastro = QFrame(self.tab)
        self.frame_btn_cadastro.setObjectName(u"frame_btn_cadastro")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_btn_cadastro.sizePolicy().hasHeightForWidth())
        self.frame_btn_cadastro.setSizePolicy(sizePolicy3)
        self.frame_btn_cadastro.setStyleSheet(u"QPushButton {\n"
"	font: 25 10pt \"Cy Grotesk Key Light\";\n"
"	background-color:rgb(38, 38, 38);\n"
"	border: 2px solid rgb(13, 122, 217);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font: 57 10.5pt \"Cy Grotesk Key Medium\";	\n"
"	background-color: rgb(12, 135, 242);\n"
"	border: 2px solid rgb(59, 61, 64);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(5, 175, 242);\n"
"}")
        self.frame_btn_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_cadastro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btn_cadastro)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_cadastrarsenha = QPushButton(self.frame_btn_cadastro)
        self.btn_cadastrarsenha.setObjectName(u"btn_cadastrarsenha")
        self.btn_cadastrarsenha.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_5.addWidget(self.btn_cadastrarsenha)

        self.btn_limpardados = QPushButton(self.frame_btn_cadastro)
        self.btn_limpardados.setObjectName(u"btn_limpardados")
        self.btn_limpardados.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_5.addWidget(self.btn_limpardados)


        self.verticalLayout_10.addWidget(self.frame_btn_cadastro)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"	font: 25 10pt \"Cy Grotesk Key Light\";\n"
"	background-color:rgb(38, 38, 38);\n"
"	border: 2px solid rgb(13, 122, 217);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font: 57 10.5pt \"Cy Grotesk Key Medium\";	\n"
"	background-color: rgb(12, 135, 242);\n"
"	border: 2px solid rgb(59, 61, 64);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(5, 175, 242);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(90, 30))

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(90, 30))

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.gridLayout_7.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font2 = QFont()
        font2.setFamilies([u"Cy Grotesk Key Medium"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(13, 122, 217);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 57 9pt \"Cy Grotesk Key Medium\";\n"
"	border-top: 0px;\n"
"	border-bottom: 0px;\n"
"	border-left: 1px solid rgb(38, 38, 38);\n"
"	border-right: 1px solid rgb(38, 38, 38);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	gridline-color: rgb(38, 38, 38);\n"
"	background-color: rgb(245, 245, 245);\n"
"	border: 2px solid rgb(13, 122, 217);\n"
"	border-radius: 2px;\n"
"	color: rgb(38, 38, 38);\n"
"}\n"
"\n"
"QTableView {\n"
"	selection-background-color: rgba(12, 135, 242, 180);\n"
"	selection-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 57 8pt \"Cy Grotesk Key Medium\";\n"
"	color: rgb(22, 22, 22);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_7.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.label_titulo_listasenha = QLabel(self.tab_2)
        self.label_titulo_listasenha.setObjectName(u"label_titulo_listasenha")
        self.label_titulo_listasenha.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_titulo_listasenha, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_cadastrar)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.mid_main_frame)

        self.foot_main_frame = QFrame(self.main_frame)
        self.foot_main_frame.setObjectName(u"foot_main_frame")
        self.foot_main_frame.setMinimumSize(QSize(0, 23))
        self.foot_main_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(28, 28, 28);\n"
"}\n"
"\n"
"QLabel#label_top{\n"
"	font: 12pt \"Cy Grotesk Key Regular\";\n"
"}")
        self.foot_main_frame.setFrameShape(QFrame.StyledPanel)
        self.foot_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.foot_main_frame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, 0, 0)

        self.verticalLayout.addWidget(self.foot_main_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_toggle, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_gerar)
        QWidget.setTabOrder(self.btn_gerar, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.btn_radio)
        QWidget.setTabOrder(self.btn_radio, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.btn_colarsenha)
        QWidget.setTabOrder(self.btn_colarsenha, self.btn_cadastrarsenha)
        QWidget.setTabOrder(self.btn_cadastrarsenha, self.btn_limpardados)
        QWidget.setTabOrder(self.btn_limpardados, self.btn_alterar)
        QWidget.setTabOrder(self.btn_alterar, self.btn_excluir)
        QWidget.setTabOrder(self.btn_excluir, self.tableWidget)

        self.retranslateUi(MainWindow)
        self.btn_limpardados.clicked.connect(self.lineEdit_3.clear)
        self.btn_limpardados.clicked.connect(self.lineEdit_2.clear)
        self.btn_limpardados.clicked.connect(self.lineEdit.clear)
        self.btn_colarsenha.clicked.connect(self.lineEdit_3.paste)

        self.toolBox_menu.setCurrentIndex(0)
        self.toolBox_menu.layout().setSpacing(0)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_tituloprograma.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#fcfcfc;\">KeyFortress</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar Senha", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Senha", None))
        self.toolBox_menu.setItemText(self.toolBox_menu.indexOf(self.page_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Criado por:</span> Guridolofi | Marthius Redler</p><p align=\"center\"><span style=\" font-weight:600;\">GitHub:</span> https://github.com/guridolofi</p><p align=\"center\"><span style=\" font-weight:600;\">Instagram:</span> https://www.instagram.com/guridolofi/</p><p align=\"center\"><span style=\" font-weight:600;\">Contato:</span> marthiusredler@hotmail.com</p></body></html>", None))
        self.toolBox_menu.setItemText(self.toolBox_menu.indexOf(self.page_sobre), QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_toggle.setText("")
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sistema de Cria\u00e7\u00e3o e Gerenciamento de Senhas</p></body></html>", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/KeyGenerator_Logo.png\"/></p></body></html>", None))
        self.label_titulo_gerarsenha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Gerar Nova Senha:</span></p></body></html>", None))
        self.label_qtd_char.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Quantidade de Caracteres:</span></p></body></html>", None))
        self.btn_radio.setText(QCoreApplication.translate("MainWindow", u"Usar Simbolos", None))
        self.label_resultado_gerar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_titulo_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Senha Gerada:</span></p></body></html>", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Gerar Senha", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Copiar Senha", None))
        self.label_titulo_cadastronovasenha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cadastro de Nova Senha:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip(QCoreApplication.translate("MainWindow", u"Deve possuir no minimo oito caracterres e conter letras mai\u00fasculas e min\u00fasculas, n\u00fameros e s\u00edmbolos.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*Su4S3nh@_AQu1", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_email_user.setText(QCoreApplication.translate("MainWindow", u"Email/Usu\u00e1rio:", None))
        self.label_titulo_novocadastro.setText(QCoreApplication.translate("MainWindow", u"Titulo:", None))
        self.btn_colarsenha.setText(QCoreApplication.translate("MainWindow", u"Colar", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nome@exemplo.com, cadastro@faculdade.com, suanick, SeuUsuario", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha do Pinterest, Senha do Fortinite...", None))
        self.btn_cadastrarsenha.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Senha", None))
        self.btn_limpardados.setText(QCoreApplication.translate("MainWindow", u"Limpar Dados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"TITULO", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"EMAIL/USUARIO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"SENHA", None));
        self.label_titulo_listasenha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Lista de Senhas Cadastradas:</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Senhas", None))
    # retranslateUi

