# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/particleInstanceTool/particleinstancetool_01.ui'
#
# by alpha
#
# particleInstanceTool V0.9
#avarageNx
#



from PySide import QtCore, QtGui
import pymel.core as pm
import maya.cmds as cmds
import random ,math, os,json
import maya.OpenMaya as OpenMaya
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.setFontSize=8
        #setPointSize(self.setFontSize) = setPointSize(self.setFontSize +3)
        #setPointSize(10) = setPointSize(self.setFontSize +2)
        #setPointSize(self.setFontSize) = setPointSize(self.setFontSize) 
        #//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/
        #//art-1405260002/D/assets/scripts/maya_scripts///art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(689, 420)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 59, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 9, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_multiple = QtGui.QLabel(self.centralwidget)
        self.label_multiple.setGeometry(QtCore.QRect(430, 132, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_multiple.setFont(font)
        self.label_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.label_multiple.setObjectName("label_multiple")
        self.lineEdit_multiple = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_multiple.setGeometry(QtCore.QRect(630, 148, 50, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_multiple.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_multiple.setFont(font)
        self.lineEdit_multiple.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiple.setReadOnly(False)
        self.lineEdit_multiple.setObjectName("lineEdit_multiple")
        self.horizontalSlider_multiPly = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_multiPly.setGeometry(QtCore.QRect(380, 148, 241, 20))
        self.horizontalSlider_multiPly.setMinimum(-10)
        self.horizontalSlider_multiPly.setMaximum(10)
        self.horizontalSlider_multiPly.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_multiPly.setObjectName("horizontalSlider_multiPly")
        self.lineEdit_randomScale = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_randomScale.setGeometry(QtCore.QRect(630, 268, 50, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_randomScale.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomScale.setFont(font)
        self.lineEdit_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomScale.setReadOnly(False)
        self.lineEdit_randomScale.setObjectName("lineEdit_randomScale")
        self.horizontalSlider_randomScale = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_randomScale.setEnabled(True)
        self.horizontalSlider_randomScale.setGeometry(QtCore.QRect(380, 270, 241, 20))
        self.horizontalSlider_randomScale.setMinimum(-100)
        self.horizontalSlider_randomScale.setMaximum(100)
        self.horizontalSlider_randomScale.setSingleStep(0)
        self.horizontalSlider_randomScale.setPageStep(10)
        self.horizontalSlider_randomScale.setSliderPosition(1)
        self.horizontalSlider_randomScale.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomScale.setObjectName("horizontalSlider_randomScale")
        self.label_randomScale = QtGui.QLabel(self.centralwidget)
        self.label_randomScale.setGeometry(QtCore.QRect(430, 254, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomScale.setFont(font)
        self.label_randomScale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomScale.setObjectName("label_randomScale")
        self.lineEdit_randomPosition = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_randomPosition.setGeometry(QtCore.QRect(630, 179, 50, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_randomPosition.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomPosition.setFont(font)
        self.lineEdit_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomPosition.setReadOnly(False)
        self.lineEdit_randomPosition.setObjectName("lineEdit_randomPosition")
        self.horizontalSlider_randomPosition = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_randomPosition.setGeometry(QtCore.QRect(380, 180, 241, 20))
        self.horizontalSlider_randomPosition.setMinimum(0)
        self.horizontalSlider_randomPosition.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomPosition.setObjectName("horizontalSlider_randomPosition")
        self.label_randomPosition = QtGui.QLabel(self.centralwidget)
        self.label_randomPosition.setGeometry(QtCore.QRect(430, 164, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomPosition.setFont(font)
        self.label_randomPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomPosition.setObjectName("label_randomPosition")
        self.lineEdit_randomRotation = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_randomRotation.setGeometry(QtCore.QRect(630, 238, 50, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_randomRotation.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_randomRotation.setFont(font)
        self.lineEdit_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_randomRotation.setReadOnly(False)
        self.lineEdit_randomRotation.setObjectName("lineEdit_randomRotation")
        self.horizontalSlider_randomRotation = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_randomRotation.setGeometry(QtCore.QRect(380, 240, 241, 20))
        self.horizontalSlider_randomRotation.setMinimum(0)
        self.horizontalSlider_randomRotation.setMaximum(360)
        self.horizontalSlider_randomRotation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_randomRotation.setObjectName("horizontalSlider_randomRotation")
        self.label_randomRotation = QtGui.QLabel(self.centralwidget)
        self.label_randomRotation.setGeometry(QtCore.QRect(430, 224, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_randomRotation.setFont(font)
        self.label_randomRotation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_randomRotation.setObjectName("label_randomRotation")
        self.lineEdit_spread = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_spread.setEnabled(False)
        self.lineEdit_spread.setGeometry(QtCore.QRect(630, 208, 50, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_spread.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_spread.setFont(font)
        self.lineEdit_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_spread.setReadOnly(True)
        self.lineEdit_spread.setObjectName("lineEdit_spread")
        self.horizontalSlider_spread = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_spread.setEnabled(False)
        self.horizontalSlider_spread.setGeometry(QtCore.QRect(380, 210, 241, 20))
        self.horizontalSlider_spread.setMinimum(0)
        self.horizontalSlider_spread.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_spread.setObjectName("horizontalSlider_spread")
        self.label_spread = QtGui.QLabel(self.centralwidget)
        self.label_spread.setEnabled(False)
        self.label_spread.setGeometry(QtCore.QRect(430, 194, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_spread.setFont(font)
        self.label_spread.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spread.setObjectName("label_spread")
        self.label_offset = QtGui.QLabel(self.centralwidget)
        self.label_offset.setEnabled(True)
        self.label_offset.setGeometry(QtCore.QRect(430, 284, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_offset.setFont(font)
        self.label_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_offset.setObjectName("label_offset")
        self.lineEdit_offset = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_offset.setEnabled(True)
        self.lineEdit_offset.setGeometry(QtCore.QRect(630, 298, 50, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 61, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_offset.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_offset.setFont(font)
        self.lineEdit_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_offset.setReadOnly(False)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.horizontalSlider_offset = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_offset.setEnabled(True)
        self.horizontalSlider_offset.setGeometry(QtCore.QRect(380, 300, 241, 20))
        self.horizontalSlider_offset.setMinimum(0)
        self.horizontalSlider_offset.setMaximum(5)
        self.horizontalSlider_offset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_offset.setObjectName("horizontalSlider_offset")
        self.lineEdit_errorMessage = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_errorMessage.setGeometry(QtCore.QRect(380, 45, 301, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 59, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 59, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_errorMessage.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_errorMessage.setFont(font)
        self.lineEdit_errorMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_errorMessage.setReadOnly(True)
        self.lineEdit_errorMessage.setObjectName("lineEdit_errorMessage")
        self.listWidget_objList = QtGui.QListWidget(self.centralwidget)
        self.listWidget_objList.setGeometry(QtCore.QRect(50, 125, 151, 251))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.listWidget_objList.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(self.setFontSize)
        self.listWidget_objList.setFont(font)
        self.listWidget_objList.setAlternatingRowColors(True)
        self.listWidget_objList.setObjectName("listWidget_objList")
        QtGui.QListWidgetItem(self.listWidget_objList)
        QtGui.QListWidgetItem(self.listWidget_objList)
        self.lineEdit_getSurfaceMesh = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_getSurfaceMesh.setGeometry(QtCore.QRect(50, 44, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_getSurfaceMesh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_getSurfaceMesh.setFont(font)
        self.lineEdit_getSurfaceMesh.setObjectName("lineEdit_getSurfaceMesh")
        self.lineEdit_sourceParticle = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_sourceParticle.setGeometry(QtCore.QRect(50, 84, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_sourceParticle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_sourceParticle.setFont(font)
        self.lineEdit_sourceParticle.setObjectName("lineEdit_sourceParticle")
        self.lineEdit_exportFolder = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_exportFolder.setGeometry(QtCore.QRect(210, 220, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEdit_exportFolder.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.lineEdit_exportFolder.setFont(font)
        self.lineEdit_exportFolder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_exportFolder.setReadOnly(True)
        self.lineEdit_exportFolder.setObjectName("lineEdit_exportFolder")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(self.setFontSize)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget_fileList = QtGui.QListWidget(self.centralwidget)
        self.listWidget_fileList.setGeometry(QtCore.QRect(210, 244, 161, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 21, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.listWidget_fileList.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(self.setFontSize)
        self.listWidget_fileList.setFont(font)
        self.listWidget_fileList.setAlternatingRowColors(True)
        self.listWidget_fileList.setObjectName("listWidget_fileList")
        QtGui.QListWidgetItem(self.listWidget_fileList)
        QtGui.QListWidgetItem(self.listWidget_fileList)
        QtGui.QListWidgetItem(self.listWidget_fileList)
        QtGui.QListWidgetItem(self.listWidget_fileList)
        QtGui.QListWidgetItem(self.listWidget_fileList)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(380, 114, 241, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_aimMode = QtGui.QLabel(self.centralwidget)
        self.label_aimMode.setGeometry(QtCore.QRect(210, 175, 154, 14))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        font.setItalic(True)
        self.label_aimMode.setFont(font)
        self.label_aimMode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aimMode.setObjectName("label_aimMode")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 184, 151, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_normal = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_normal.setFont(font)
        self.radioButton_normal.setChecked(True)
        self.radioButton_normal.setObjectName("radioButton_normal")
        self.horizontalLayout_2.addWidget(self.radioButton_normal)
        self.radioButton_alwaysTop = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_alwaysTop.setFont(font)
        self.radioButton_alwaysTop.setObjectName("radioButton_alwaysTop")
        self.horizontalLayout_2.addWidget(self.radioButton_alwaysTop)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 144, 151, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_duplicate = QtGui.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_duplicate.setFont(font)
        self.radioButton_duplicate.setChecked(True)
        self.radioButton_duplicate.setObjectName("radioButton_duplicate")
        self.horizontalLayout.addWidget(self.radioButton_duplicate)
        self.radioButton_instance = QtGui.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.radioButton_instance.setFont(font)
        self.radioButton_instance.setObjectName("radioButton_instance")
        self.horizontalLayout.addWidget(self.radioButton_instance)
        self.label_copyMode = QtGui.QLabel(self.centralwidget)
        self.label_copyMode.setGeometry(QtCore.QRect(210, 124, 154, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        font.setItalic(True)
        self.label_copyMode.setFont(font)
        self.label_copyMode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_copyMode.setObjectName("label_copyMode")
        self.label_particlesCount = QtGui.QLabel(self.centralwidget)
        self.label_particlesCount.setGeometry(QtCore.QRect(460, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        font.setItalic(True)
        self.label_particlesCount.setFont(font)
        self.label_particlesCount.setAlignment(QtCore.Qt.AlignCenter)
        self.label_particlesCount.setObjectName("label_particlesCount")
        self.label_createMode = QtGui.QLabel(self.centralwidget)
        self.label_createMode.setGeometry(QtCore.QRect(216, 5, 101, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_createMode.setFont(font)
        self.label_createMode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_createMode.setObjectName("label_createMode")
        self.pushButton_getSurfaceMesh = QtGui.QPushButton(self.centralwidget)
        self.pushButton_getSurfaceMesh.setGeometry(QtCore.QRect(10, 50, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_getSurfaceMesh.setPalette(palette)
        self.pushButton_getSurfaceMesh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshB-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshA-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getMeshB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_getSurfaceMesh.setIcon(icon)
        self.pushButton_getSurfaceMesh.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_getSurfaceMesh.setCheckable(True)
        self.pushButton_getSurfaceMesh.setFlat(True)
        self.pushButton_getSurfaceMesh.setObjectName("pushButton_getSurfaceMesh")
        self.pushButton_getParticle = QtGui.QPushButton(self.centralwidget)
        self.pushButton_getParticle.setGeometry(QtCore.QRect(10, 90, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_getParticle.setPalette(palette)
        self.pushButton_getParticle.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesB-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesA-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_getParticle.setIcon(icon1)
        self.pushButton_getParticle.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_getParticle.setCheckable(True)
        self.pushButton_getParticle.setFlat(True)
        self.pushButton_getParticle.setObjectName("pushButton_getParticle")
        self.pushButton_addObbject = QtGui.QPushButton(self.centralwidget)
        self.pushButton_addObbject.setGeometry(QtCore.QRect(10, 130, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_addObbject.setPalette(palette)
        self.pushButton_addObbject.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoB-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoA-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getGeoB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_addObbject.setIcon(icon2)
        self.pushButton_addObbject.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_addObbject.setCheckable(True)
        self.pushButton_addObbject.setFlat(True)
        self.pushButton_addObbject.setObjectName("pushButton_addObbject")
        self.pushButton_clearList = QtGui.QPushButton(self.centralwidget)
        self.pushButton_clearList.setGeometry(QtCore.QRect(10, 170, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_clearList.setPalette(palette)
        self.pushButton_clearList.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearB-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearA-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/clearB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_clearList.setIcon(icon3)
        self.pushButton_clearList.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_clearList.setCheckable(True)
        self.pushButton_clearList.setFlat(True)
        self.pushButton_clearList.setObjectName("pushButton_clearList")
        self.pushButton_writeToCache = QtGui.QPushButton(self.centralwidget)
        self.pushButton_writeToCache.setGeometry(QtCore.QRect(210, 42, 140, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_writeToCache.setPalette(palette)
        self.pushButton_writeToCache.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC2.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC2.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheC2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_writeToCache.setIcon(icon4)
        self.pushButton_writeToCache.setIconSize(QtCore.QSize(140, 35))
        self.pushButton_writeToCache.setCheckable(True)
        self.pushButton_writeToCache.setFlat(True)
        self.pushButton_writeToCache.setObjectName("pushButton_writeToCache")
        self.pushButton_loadFromCache = QtGui.QPushButton(self.centralwidget)
        self.pushButton_loadFromCache.setGeometry(QtCore.QRect(210, 81, 140, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_loadFromCache.setPalette(palette)
        self.pushButton_loadFromCache.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC2.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC2.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/loadFromCacheC2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_loadFromCache.setIcon(icon5)
        self.pushButton_loadFromCache.setIconSize(QtCore.QSize(140, 35))
        self.pushButton_loadFromCache.setCheckable(True)
        self.pushButton_loadFromCache.setFlat(True)
        self.pushButton_loadFromCache.setObjectName("pushButton_loadFromCache")
        self.pushButton_reset = QtGui.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(650, 110, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_reset.setPalette(palette)
        self.pushButton_reset.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/resetB-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/resetB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/resetB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/resetA-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/resetB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/resetB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/resetB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_reset.setIcon(icon6)
        self.pushButton_reset.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_reset.setCheckable(True)
        self.pushButton_reset.setFlat(True)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_create = QtGui.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(500, 330, 180, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_create.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(self.setFontSize)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setAutoFillBackground(False)
        self.pushButton_create.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG2.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG2.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/createG2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_create.setIcon(icon7)
        self.pushButton_create.setIconSize(QtCore.QSize(180, 60))
        self.pushButton_create.setCheckable(True)
        self.pushButton_create.setDefault(False)
        self.pushButton_create.setFlat(True)
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_createMode_2 = QtGui.QLabel(self.centralwidget)
        self.label_createMode_2.setGeometry(QtCore.QRect(564, 353, 101, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(self.setFontSize)
        self.label_createMode_2.setFont(font)
        self.label_createMode_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_createMode_2.setObjectName("label_createMode_2")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(196, 40, 20, 341))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(365, 40, 20, 341))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_getInfo = QtGui.QPushButton(self.centralwidget)
        self.pushButton_getInfo.setGeometry(QtCore.QRect(390, 350, 30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_getInfo.setPalette(palette)
        self.pushButton_getInfo.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallB-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallA-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallB-512.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallB-512.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/smallB-512.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton_getInfo.setIcon(icon8)
        self.pushButton_getInfo.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_getInfo.setCheckable(True)
        self.pushButton_getInfo.setFlat(True)
        self.pushButton_getInfo.setObjectName("pushButton_getInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ParticleInstanceTool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "total particles Count", None, QtGui.QApplication.UnicodeUTF8))
        self.label_multiple.setText(QtGui.QApplication.translate("MainWindow", "multiply", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_multiple.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_randomScale.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_randomScale.setText(QtGui.QApplication.translate("MainWindow", "random Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_randomPosition.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_randomPosition.setText(QtGui.QApplication.translate("MainWindow", "random Position", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_randomRotation.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_randomRotation.setText(QtGui.QApplication.translate("MainWindow", "random Rotation", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_spread.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_spread.setText(QtGui.QApplication.translate("MainWindow", "spread", None, QtGui.QApplication.UnicodeUTF8))
        self.label_offset.setText(QtGui.QApplication.translate("MainWindow", "offset", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_offset.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_objList.isSortingEnabled()
        self.listWidget_objList.setSortingEnabled(False)
        self.listWidget_objList.item(0).setText(QtGui.QApplication.translate("MainWindow", "aaa", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_objList.item(1).setText(QtGui.QApplication.translate("MainWindow", "bbb", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_objList.setSortingEnabled(__sortingEnabled)
        self.label.setText(QtGui.QApplication.translate("MainWindow", " particle Instance ToolVer. 0.951", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_fileList.isSortingEnabled()
        self.listWidget_fileList.setSortingEnabled(False)
        self.listWidget_fileList.item(0).setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_fileList.item(1).setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_fileList.item(2).setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_fileList.item(3).setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_fileList.item(4).setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_fileList.setSortingEnabled(__sortingEnabled)
        self.label_aimMode.setText(QtGui.QApplication.translate("MainWindow", "aim Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_normal.setText(QtGui.QApplication.translate("MainWindow", "normal", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_alwaysTop.setText(QtGui.QApplication.translate("MainWindow", "always Top", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_duplicate.setText(QtGui.QApplication.translate("MainWindow", "duplicate", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_instance.setText(QtGui.QApplication.translate("MainWindow", "instance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_copyMode.setText(QtGui.QApplication.translate("MainWindow", "copy Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_particlesCount.setText(QtGui.QApplication.translate("MainWindow", "0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_createMode.setText(QtGui.QApplication.translate("MainWindow", "particle Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_createMode_2.setText(QtGui.QApplication.translate("MainWindow", "Create from Particles", None, QtGui.QApplication.UnicodeUTF8))





class mod_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtGui.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
        #self.check_ExportToFile() selectParticleStr
        
        self.listWidget_objList.clear()

        self.pushButton_getParticle.clicked.connect(self.clickButton_getParticle)
        self.pushButton_addObbject.clicked.connect(self.clickButtin_addObjIntoList)
        self.pushButton_create.clicked.connect(self.checkMode)
        self.pushButton_getSurfaceMesh.clicked.connect(self.clickButton_getSurfaceMesh)
        self.pushButton_clearList.clicked.connect(self.clickButton_clearList)
        
        self.pushButton_reset.clicked.connect(self.clickButton_reset)
        
        #slide_1
        self.horizontalSlider_multiPly.valueChanged.connect(self.change_Multiply)
        self.lineEdit_multiple.textChanged.connect(self.change_MultiplyText)
        #slide_2
        self.horizontalSlider_randomPosition.valueChanged.connect(self.change_randomPosition)
        self.lineEdit_randomPosition.textChanged.connect(self.change_randomPositionText)
        #slide_3
        self.horizontalSlider_spread.valueChanged.connect(self.change_spread)
        #slide_4
        self.horizontalSlider_randomRotation.valueChanged.connect(self.change_randomRotation)
        self.lineEdit_randomRotation.textChanged.connect(self.change_randomRotationText)
        #slide_5
        self.horizontalSlider_randomScale.valueChanged.connect(self.change_randomScale)
        self.lineEdit_randomScale.textChanged.connect(self.change_randomScaleText)

        #slide_6  pushButton_openCacheFolder
        self.horizontalSlider_offset.valueChanged.connect(self.change_offset)
        self.lineEdit_offset.textChanged.connect(self.change_offsetText)

        # export ,input from file
        #self.pushButton_openCacheFolder.clicked.connect(self.exportCacheFolderSelect)
        self.pushButton_loadFromCache.clicked.connect(self.click_importFromFile)


        self.pushButton_writeToCache.clicked.connect(self.clickButton_writeCache)
        self.listWidget_fileList.clicked.connect(self.clickListWidget_fileList)
        #self.pushButton_placeItemFromCache.clicked.connect(self.placeItemFromCache)
        #self.pushButton_placeItemFromCache.clicked.connect(self.loadPartOfParticlesCache)

        #self.pushButton_openCacheFolder.clicked.connect(self.exportCacheFolderSelect)

        self.radioButton_duplicate.setChecked(True)
        self.radioButton_normal.setChecked(True)
        self.errorInstanceObj= []

     
        
        # do test 
        self.pushButton_getInfo.clicked.connect(self.testAAA)

    def testAAA(self):
        errorMessage = u'Do not do it, Stop~~~~'
        self.lineEdit_errorMessage.setText('%s'%errorMessage)
        

    def clickListWidget_fileList(self):
        openFileName = self.listWidget_fileList.currentItem().text()
        self.oprnFileFullName =  self.exportFolder +'/' +openFileName
        
        
        dataName = open(self.oprnFileFullName,'r')
        self.particlePositionDict = json.load(dataName) 
        dataName.close  
        self.totalParticleCount = len(self.particlePositionDict.keys())
        textShow = '%s \\n particles count: %s'%(openFileName,str(self.totalParticleCount))

        print textShow
        #self.lineEdit_errorMessage.setText(('selected %s'%openFileName)+('\n')+('particles total count: %s'%(self.lineEdit_errorMessage.setText(self.totalParticleCount))))
        self.lineEdit_errorMessage.setText(textShow)
        
        
    def placeItemFromCache(self):
        
        
        
        if  len(self.lineEdit_sourceParticle.text()) == 0:
            self.lineEdit_errorMessage.setText("type name for instance object")
        else:
            pass

            self.instanceObjName = self.lineEdit_sourceParticle.text()
        
            #self.selectParticleStr = self.lineEdit_sourceParticle.text()
            dataName = open(self.oprnFileFullName,'r')
            self.particlePositionDict = json.load(dataName)   
            dataName.close
            self.totalParticleCount = len(self.particlePositionDict.keys())
            self.clickButtin_createInstanceFromCache()
            
    def exportCacheFolderSelect(self):

        print"export to file"
        self.exportFolder = cmds.fileDialog2(fm=3)[0]
        self.lineEdit_exportFolder.setText(self.exportFolder)
        
        self.searchParticleJsonFolder()

        jsonFilesCount = len(self.fileList)
        self.listWidget_fileList.clear()
        fileReverseStored = sorted(self.fileList, reverse = True )
        for i in range(0,jsonFilesCount):
     
            QtGui.QListWidgetItem(self.listWidget_fileList)

            itemName = fileReverseStored[i].split('(')[0]
            self.listWidget_fileList.item(i).setText(QtGui.QApplication.translate("MainWindow","tempName",None,  QtGui.QApplication.UnicodeUTF8))
            self.listWidget_fileList.item(i).setText(itemName)
 

  
            
            
            
            
            
        
    def searchParticleJsonFolder(self):
        self.fileList = []
        self.verNumCountList = []
        print self.exportFolder
        allFileInDir = os.listdir(self.exportFolder)
        for file in allFileInDir:
            if file.split('.')[-1] == "json":
                self.fileList.append(file)
                self.verNumCountList.append(file.split('.')[-2].split('_')[-1].split('v')[1])
                #print file.split('.')[-2].split('_')[-1].split('v')[1]
        print self.fileList
        self.verNumSortList = sorted(self.verNumCountList)
       # jsonFilesCount

        
    def click_importFromFile(self):
        if len(self.lineEdit_exportFolder.text()) == 0:
            self.lineEdit_errorMessage.setText('select export Cache folder')
            self.exportCacheFolderSelect()
            self.lineEdit_errorMessage.setText(('file will be load from %s'%self.exportFolder))
        else:
            pass
        if self.pushButton_loadFromCache.isChecked() == True:
            self.label_createMode.setText('cache Mode')
            self.label_createMode_2.setText('Create From Cache')

        else:
            self.label_createMode.setText('particle Mode')
            self.label_createMode_2.setText('Create From Particles')
            
            
            
    def reNewParticleDictByMultiply(self):
        # if multiply >= 1 ,pass
        # if multiply <0, how many percent that will be repplace instanced item
        #       replaced self.particlePositionDict 
        #  
        self.getMultiplyNum = int(self.lineEdit_multiple.text())
        if self.getMultiplyNum >=1:
            pass

        elif self.getMultiplyNum <= -2:
            self.getParticlesSplitByInsert()
            
            for i in self.numDict.keys():
                print self.numDict[i]
            
        print self.particlePositionDict.keys()
        print len(self.particlePositionDict.keys())
        #print self.particlePositionDict
       


        
        
    def clickButton_writeCache(self):
        if len(self.lineEdit_exportFolder.text()) == 0:
            self.lineEdit_errorMessage.setText('select export Cache folder')
            self.exportCacheFolderSelect()
            self.lineEdit_errorMessage.setText(('file will be save to %s'%self.exportFolder))
    
            
        else:

            data = json.dumps(self.particlePositionDict, sort_keys=True , indent =4)

            self.searchParticleJsonFolder()
            if len(self.fileList) == 0:
                frameNum = 'v001'
                newJsonFileName = self.selectParticleStr +'_'+ frameNum+'.json'
                self.exportDataFile = self.exportFolder + '/' + newJsonFileName
                #data = "self.particlePositionDict"
                exportParticleDate = open(self.exportDataFile,'w')
                exportParticleDate.write(data)
                exportParticleDate.close
                QtGui.QListWidgetItem(self.listWidget_fileList)
                self.listWidget_fileList.item(0).setText(QtGui.QApplication.translate("MainWindow","tempName",None,  QtGui.QApplication.UnicodeUTF8))
                self.listWidget_fileList.item(0).setText(newJsonFileName)
                self.searchParticleJsonFolder()
            else:
                print self.verNumSortList
                lastVerNum = int(self.verNumSortList[-1])
                newVer = lastVerNum +1
                frameNum = 'v'+'%03d'%newVer
                #print frameNum
                newJsonFileName = self.selectParticleStr +'_'+ frameNum+'.json'
                self.exportDataFile = self.exportFolder + '/' + newJsonFileName
                print self.exportDataFile
                #print dataB
                exportParticleDate = open(self.exportDataFile,'w')
                exportParticleDate.write(data)
                exportParticleDate.close
                self.fileList
                itemIndexAdd = int(len(self.fileList)+1)
                print itemIndexAdd
                #jsonFilesCount = len(self.fileList)
                self.listWidget_fileList.clear()
                #print jsonFilesCount
                self.fileList.append(newJsonFileName)
                fileReverseStored = sorted(self.fileList, reverse = True )   
                #print fileReverseStored
                for i in range(0,itemIndexAdd):

                    QtGui.QListWidgetItem(self.listWidget_fileList)

                 #   itemName = fileList[i].split('(')[0]
                    self.listWidget_fileList.item(i).setText(QtGui.QApplication.translate("MainWindow","tempName",None,  QtGui.QApplication.UnicodeUTF8))
                    self.listWidget_fileList.item(i).setText(fileReverseStored[i])

               # json.dumps(dataName, sort_keys=True , indent =4)
        self.pushButton_writeToCache.setChecked(False)


        
    def loadPartOfParticlesCache(self):
        self.placeItemFromCache() #get select cache
        print self.oprnFileFullName
        #start = 0
        #end = len(self.particlePositionDict.keys())
        #print self.particlePositionDict
        dataName = open(self.oprnFileFullName,'r')
        self.particlePositionDict = json.load(dataName)   
        #print self.particlePositionDict
        dataName.close
        self.totalParticleCount = len(self.particlePositionDict.keys())
        self.getParticlesSplitByInsert()
        
        
    def getParticlesSplitByOrder(self):
        particlePT_start = 0
        particlePT_end =len(self.particlePositionDict.keys())
        threadNum = 5
        block = particlePT_end/threadNum
        numListStart =[]
        numListEnd =[]
        self.numDict={}    #get particle list ,separate 5 arear by insert number
        for num in range(particlePT_start,particlePT_end+1):
            if num% block == 0:
                numListStart.append(num)
            if num% block == block-1:
                numListEnd.append(num)
        if len(numListStart) > len(numListEnd):
            numListEnd.append(particlePT_end)   
        listNum= len(numListStart)
        for listIndex in range(0,(listNum)):
            print listIndex
            tempNumList =[]
            for i in range(numListStart[listIndex],((numListEnd[listIndex])+1)):
                tempNumList.append(i)
            self.numDict.update({listIndex:tempNumList})
        print self.numDict
        print self.numDict[0]
        print self.numDict[1]
        print self.numDict[2]
        print self.numDict[3]
        print self.numDict[4]
        
        
    def getParticlesSplitByInsert(self):
        #get the newList ,from self.particlePositionDict, by insert number, getMultiplyNum
        print "reNew particlePositionDict"

            
        threadNum = 10
        #print self.particlePositionDict

        particlePT_start = 0
        particlePT_end =len(self.particlePositionDict.keys())
        #print particlePT_end
        #print self.particlePositionDict
        #print self.particlePositionDict.keys()[-1]
        
        block = int(particlePT_end/threadNum)
        
        
        print block

        numListStart =[]
        numListEnd =[]
        self.numDict={}    #get particle list ,separate 5 arear by insert number
        for num in range(particlePT_start,particlePT_end+1):
            if num% block == 0:
                numListStart.append(num)
            if num% block == block-1:
                numListEnd.append(num)
        if len(numListStart) > len(numListEnd):
            numListEnd.append(particlePT_end)   
        listNum= len(numListStart)
        #print numListStart
        #print listNum
    #def asdasdsf(self):
                
        for listIndex in range(0,(listNum-1)):
            tempNumList =[]
            for insertNum in range(0,(block+1)):
                sumNum = listIndex + insertNum*threadNum
                if sumNum > particlePT_end : 
                    pass
                else:
                    tempNumList.append(sumNum)
            self.numDict.update({listIndex:tempNumList})
            
        #self.particlePositionDict = self.numDict
            #print tempNumList
           # print self.numDict
       # print self.numDict

       # for i in self.numDict.keys():
       #     print self.numDict[i]
    
        
    def clickButton_reset(self):
        
        self.radioButton_duplicate.setChecked(True)
        self.radioButton_normal.setChecked(True)
        self.horizontalSlider_multiPly.setValue(1)
        self.horizontalSlider_randomPosition.setValue(0)
        self.horizontalSlider_spread.setValue(0)
        self.horizontalSlider_randomRotation.setValue(0)
        self.horizontalSlider_randomScale.setValue(0)
        self.horizontalSlider_offset.setValue(0)
        
        
        self.pushButton_reset.setCheckable(False)
        
    #slide_1    
    def change_Multiply(self):
        getMultiplyValue = self.horizontalSlider_multiPly.value()
        self.lineEdit_multiple.setText(str(getMultiplyValue))
        
    def change_MultiplyText(self):
        
        getMultiplyValue = int(self.lineEdit_multiple.text())

        self.horizontalSlider_multiPly.setValue(getMultiplyValue)






        
        
        
    #slide_2
    def change_randomPosition(self):
        getrandomPositionValue = float(self.horizontalSlider_randomPosition.value())/(100.0)
        self.lineEdit_randomPosition.setText(str(getrandomPositionValue))
        
    def change_randomPositionText(self):
        getrandomPositionValue = float(self.lineEdit_randomPosition.text())*(100.0)
        self.horizontalSlider_randomPosition.setValue(int(getrandomPositionValue))
        
    #slide_3

    def change_spread(self):
        getspreadValue = self.horizontalSlider_spread.value()
        self.lineEdit_spread.setText(str(getspreadValue))
    #slide_4
    def change_randomRotation(self):
        getrandomRotationValue = self.horizontalSlider_randomRotation.value()
        self.lineEdit_randomRotation.setText(str(getrandomRotationValue))
        
        
    def change_randomRotationText(self):
        getrandomRotationValue = float(self.lineEdit_randomRotation.text())
        self.horizontalSlider_randomRotation.setValue(getrandomRotationValue)
                
        
        
    #slide_5
    def change_randomScale(self):
        getrandomScaleValue = float(self.horizontalSlider_randomScale.value())/(100.0)
        print getrandomScaleValue
        self.lineEdit_randomScale.setText(str(getrandomScaleValue))
    
    def change_randomScaleText(self):
        getrandomScaleValue = int(float(self.lineEdit_randomScale.text())*(100.0))
        self.horizontalSlider_randomScale.setValue(getrandomScaleValue)
            
        
               
        
        
        
        
    #slide_6
    def change_offset(self):
        getoffsetValue = float(self.horizontalSlider_offset.value()/(100.0))
        self.lineEdit_offset.setText(str(getoffsetValue))
    
    def change_offsetText(self):
        getoffsetValue = int(float(self.lineEdit_offset.text())*(100.0))
        self.horizontalSlider_offset.setValue(getoffsetValue)
            



        
    def clickButton_getSurfaceMesh(self):
        print" get the surface,that take form other scenes"
        self.selectMesh = pm.ls(sl=True)[0].split('(')[0]
        self.lineEdit_getSurfaceMesh.setText(self.selectMesh)
        self.pushButton_getSurfaceMesh.setChecked(False)

        

    def clickButton_getParticle(self):
        print "get Particle from selected"
        
        getParticle = pm.ls(sl=True)
        self.selectParticleStr = getParticle[0] 
        self.selectParticleShapeStr = pm.ls(sl=True,dag=2)[1].split('(')[0]
        #print self.selectParticleShapeStr
        if pm.nodeType(self.selectParticleShapeStr)  == 'nParticle' :
        
            if len(getParticle) > 1:
                print "make sure select one particle"
            
            else:
                print self.selectParticleStr
                self.lineEdit_sourceParticle.setText("%s"%self.selectParticleStr)
        else:
            print "select particle source"
            pass
        
        self.totalParticleCount = pm.nParticle(getParticle, query=True, ct=True)
        self.label_particlesCount.setText('%s'%self.totalParticleCount)
        self.pushButton_getParticle.setChecked(False)
        print self.pushButton_getParticle.isChecked()
        
       # icon = QtGui.QIcon()
        
        #icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/getParticlesA-512.png"))
        #, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheB2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        #icon.addPixmap(QtGui.QPixmap("//art-1405260002/D/assets/scripts/maya_scripts/icons/particleInstanceToolIcons/writeToCacheB2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)  
        #self.pushButton_getParticle.setIcon(icon)
        #self.pushButton_clearList.setIconSize(QtCore.QSize(30, 30))
        #self.pushButton_clearList.setCheckable(True)
        #self.pushButton_clearList.setFlat(True)
        #self.pushButton_clearList.setObjectName("pushButton_clearList")
        #self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_create.setGeometry(QtCore.QRect(380, 50, 40, 40))     

            
    def clickButtin_addObjIntoList(self):
        print "add object into list"

        self.objList = []   #get objList in listWidger QtGui.QApplication.UnicodeUTF8
        self.selectObjList = []   #get list from selected
        objCount =  self.listWidget_objList.count()
        for n in range(0,objCount):
            
            object = self.listWidget_objList.item(n).text()
            self.objList.append(object)
        print self.objList
        
        selectObjs = pm.ls(sl=True)
        selectObjsCount = len(selectObjs)
        
        for i in range(0,selectObjsCount):
            addObj = selectObjs[i].split('(')[0]
           # if addObj in self.objList: #check if addObj in list
          #      pass
           # else:
            
            self.selectObjList.append(addObj)
            QtGui.QListWidgetItem(self.listWidget_objList)
            QtGui.QListWidgetItem(self.listWidget_objList)
            itemCount = i + objCount
            itemName = selectObjs[i].split('(')[0]
            self.listWidget_objList.item(itemCount).setText(QtGui.QApplication.translate("MainWindow","tempName", None,  QtGui.QApplication.UnicodeUTF8))
            self.listWidget_objList.item(itemCount).setText(itemName)
        print self.selectObjList
        
        self.pushButton_addObbject.setChecked(False)

        
       # QtWidgets.QListWidgetItem(self.listWidget_objList)

       # self.listWidget_objList.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "aaa",None,  QtGui.QApplication.UnicodeUTF8))
    
    def clickButton_clearList(self):
        self.listWidget_objList.clear()
        self.objList = []
        self.selectObjList = []
        self.pushButton_clearList.setChecked(False)

        

    def getVertexNormal(self):
        geo = pm.PyNode(self.selectMesh)
       # print geo
        pos = self.positionPP

        nodeDagPath = OpenMaya.MObject()
        

        try:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(geo.name())
            nodeDagPath = OpenMaya.MDagPath()
            selectionList.getDagPath(0, nodeDagPath)
        except:
            warning('OpenMaya.MDagPath() failed on %s' % geo.name())
            

   
        mfnMesh = OpenMaya.MFnMesh(nodeDagPath)

        pointA = OpenMaya.MPoint(pos[0], pos[1], pos[2])
        
        pointB = OpenMaya.MPoint()
        space = OpenMaya.MSpace.kWorld
        util = OpenMaya.MScriptUtil()
        util.createFromInt(0)
        idPointer = util.asIntPtr()

        mfnMesh.getClosestPoint(pointA, pointB, space, idPointer)  
        idx = OpenMaya.MScriptUtil(idPointer).asInt()

        faceVerts = [geo.vtx[i] for i in geo.f[idx].getVertices()]
        closestVertex = None
        minLength = None
        
   # def aaaaaa(self):
        
        for v in faceVerts:
            thisLength = (pos - v.getPosition(space='world')).length()
            if minLength is None or thisLength < minLength:
                minLength = thisLength
                closestVertex = v
        #pm.select('pPlaneShape1.vtx[1785]')
            #aa=pm.ls(sl=True,fl=True)[0].split('(')[0]
            #print cmds.polyListComponentConversion(aa,fv=True, tf=True)
            #print len(cmds.polyListComponentConversion(aa,fv=True, tf=True))
        closeVertexNormal = pm.polyNormalPerVertex(closestVertex,q=1,xyz=1)
        #print closestVertex,len(closeVertexNormal),closeVertexNormal


        if len(closeVertexNormal) == 12:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] + closeVertexNormal[6]  + closeVertexNormal[9] )/4.0
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] + closeVertexNormal[7]  + closeVertexNormal[10] )/4.0
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] + closeVertexNormal[8]  + closeVertexNormal[11] )/4.0
        elif len(closeVertexNormal) == 6:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] )/2.0
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] )/2.0
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] )/2.0
        elif len(closeVertexNormal) == 3:
            self.avarageNx =( closeVertexNormal[0] )
            self.avarageNy =( closeVertexNormal[1] )
            self.avarageNz =( closeVertexNormal[2] )
        elif len(closeVertexNormal) == 12:
            self.avarageNx =( closeVertexNormal[0] + closeVertexNormal[3] + closeVertexNormal[6]  + closeVertexNormal[9] + closeVertexNormal[12] )/5.0
            self.avarageNy =( closeVertexNormal[1] + closeVertexNormal[4] + closeVertexNormal[7]  + closeVertexNormal[10] + closeVertexNormal[13] )/5.0
            self.avarageNz =( closeVertexNormal[2] + closeVertexNormal[5] + closeVertexNormal[8]  + closeVertexNormal[11] + closeVertexNormal[14] )/5.0
        else:
            pass  
          
            
        #print self.avarageNx,self.avarageNy,self.avarageNz allInstanceList selectParticleStr

    def clickButtin_createInstanceFromCache(self):
        # get new particle position dictionary from self.getParticlesSplitByInsert(), store to self.numDict PercentCount
        self.getParticlesSplitByInsert()
        self.sourceObjCount = len(self.selectObjList)
        self.allInstanceList=[]
        self.instanceObjName = self.lineEdit_sourceParticle.text()

        self.emptyGrp = pm.createNode('transform', n='%s_instanceGrp'%self.instanceObjName )

        self.multiplyNum= int(self.lineEdit_multiple.text())
        
        
        self.scaleMultiPly = (float(self.lineEdit_randomScale.text())/(1.0))
        self.randomPosition = float(self.lineEdit_randomPosition.text())
        self.randomRotation = float(self.lineEdit_randomRotation.text())
        self.offsetValue = float(self.lineEdit_offset.text())
        print "multiply",self.multiplyNum
        print "spread",self.lineEdit_spread.text()
        print "scale", self.lineEdit_randomScale.text()
        print "position",self.lineEdit_randomPosition.text()
        print "rotation",self.lineEdit_randomRotation.text()
        print "offset",self.lineEdit_offset.text()
        


        print "get all data from particle"
        if self.multiplyNum >= 1:
            self.PercentCount = int(1)
  
            self.doReplaceItemsFromCache()
        elif self.multiplyNum <= -1:
            for self.PercentCount in range(0,abs(self.multiplyNum)):
                print self.PercentCount
                self.percentNumList = self.numDict[self.PercentCount]
               # self.particlePositionDict = self.numDict[str(self.PercentCount)]
                self.doReplaceItemsFromCachePercent() 
        self.pushButton_create.setChecked(False)
       
    def doReplaceItemsFromCache(self):
        countSetObj =0
        for n in range(0,self.totalParticleCount):
            countSetObj = countSetObj +1
            processPresentValue = int(((float(countSetObj)/float(self.totalParticleCount))/(2.0) + 0.5)*100.0)
           # print processPresentValue
           # self.progressBar.value(processPresentValue)
            self.progressBar.setValue(processPresentValue)

            for k in range(0,self.multiplyNum):
                #print n,k
                randMovement = random.uniform((-self.randomPosition),self.randomPosition)
                sourceObj = self.selectObjList[random.randint(0,(self.sourceObjCount-1))] #get random obj index
                newName = self.instanceObjName +'_instanceObj' +'_'+ str(self.PercentCount) +'_'+ str(n)+'_'+str(k)
                self.allInstanceList.append(newName)
                #print allInstanceList 
                #print newName
                #self.totalParticleCount
                #randomRotation = random.uniform(-randomRotation,randomRotation) 

                randomScale = 1 * (random.uniform( (1.0-self.scaleMultiPly),(1.0+self.scaleMultiPly)))
                if self.radioButton_duplicate.isChecked() == True:

                    newInstanceObj = cmds.duplicate( sourceObj, n=newName,rc=True,rr=True )
                else:

                    newInstanceObj = cmds.instance( sourceObj, n=newName )
                #random position
                pm.parent(newInstanceObj,self.emptyGrp)



                if self.lineEdit_randomPosition.text() == "0":
                    moveX = self.particlePositionDict[str(n)][0]                
                    moveY = self.particlePositionDict[str(n)][1]                 
                    moveZ = self.particlePositionDict[str(n)][2] 
                    cmds.setAttr( "%s.translateX"%newName,moveX)
                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,moveZ)
                   # cmds.setAttr( "%s.rotateY"%newName,randomRotation)
                    #print moveX,moveY,moveZ
                else:
                    #randMoveX = particlePositionDict[str(n)][0] + randMovement/bbMaxDistance
                                        
                    #if self.lineEdit_offset.text() == "0":
                       # randMoveY = particlePositionDict[str(n)][1] 
                    #else:                      
                       # randMoveY = particlePositionDict[str(n)][1] + float(self.lineEdit_offset.text())
                    moveY = self.particlePositionDict[str(n)][1]
                    #randMoveY = particlePositionDict[str(n)][1] 
                    #randMoveZ = particlePositionDict[str(n)][2] + randMovement/bbMaxDistance               
                    #print randMoveX,randMoveY,randMoveZ
                    cmds.setAttr( "%s.translateX"%newName,(self.particlePositionDict[str(n)][0] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))

                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,(self.particlePositionDict[str(n)][2] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))
                    
                    #cmds.setAttr( "%s.rotateY"%newName,randomRotation)

                    #(particlePositionDict[str(n)][0] +random.uniform(float(self.lineEdit_randomPosition.text())))

                if self.lineEdit_randomScale.text() == "0":
                    pass
                else:
                    cmds.setAttr( "%s.scaleX"%newName,randomScale)
                    cmds.setAttr( "%s.scaleZ"%newName,randomScale)
                    
                    
                #random rotate

                if self.radioButton_normal.isChecked() == True: 

                    rotateNormalx = self.particlePositionDict[str(n)][3]
                    rotateNormaly = self.particlePositionDict[str(n)][4]
                    rotateNormalz = self.particlePositionDict[str(n)][5]  
                    
                    
                    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
                   # rotX = numpy.deg2rad(numpy.arctan2(rotateNormaly,rotateNormalz))
                    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))
                   # rotY = numpy.deg2rad(numpy.arctan2(rotateNormalx,rotateNormalz))

                    #rotZ = math.degrees((math.pi/(2.0))-math.asin(rotateNormaly))
                    try:
                        rotZ = math.degrees(1.57-math.asin(rotateNormaly))
                        #print "correct",rotateNormaly
                    except:
                        #print "error",rotateNormaly
                       # print math.asin(rotateNormaly)
                        rotZ = math.degrees(1.57-abs(math.asin(1.0)))
                        #print "%s"%newName + "   rotZ error"
                        self.errorInstanceObj.append(newName)
                        pass
                    #print n,'rotX',rotX
                    #print n,'rotY',rotY
                    #print n,'rotZ',rotZ
                    math.asin(-0.5)
                    randRotValue = float(self.lineEdit_randomRotation.text())

 
                    cmds.setAttr( "%s.rotateX"%newName,(rotZ+random.uniform(-randRotValue,randRotValue)))
                    cmds.setAttr( "%s.rotateY"%newName,(rotY+random.uniform(-randRotValue,randRotValue)))

                   # cmds.setAttr( "%s.rotateY"%newName,randRotValue) 
                    #self.returnProcessPersent()
                else:
                    pass
                if self.lineEdit_offset.text() == "0":
                    pass
                else:
                    originalTranslateY = cmds.getAttr("%s.translateY"%newName)
                    moveY = originalTranslateY + self.offsetValue
                    cmds.setAttr( "%s.translateY"%newName,moveY)
            #print self.errorInstanceObj
            #self.lineEdit_errorMessage.setText(self.errorInstanceObj)

    def doReplaceItemsFromCachePercent(self):
        countSetObj =0
        emptySecGrp = pm.createNode('transform', n=('%s_Sec_InstanceGrp_%s'%(self.instanceObjName,str(countSetObj))))
        pm.parent(emptySecGrp, self.emptyGrp)

        for n in self.percentNumList:
            print n
            print type(n)
            
            
            
        
            countSetObj = countSetObj +1
            processPresentValue = int(((float(countSetObj)/float(len(self.percentNumList)))/(2.0) + 0.5)*100.0)
            print processPresentValue
            #self.progressBar.value(processPresentValue) k
            self.progressBar.setValue(processPresentValue)

            randMovement = random.uniform((-self.randomPosition),self.randomPosition)
            sourceObj = self.selectObjList[random.randint(0,(self.sourceObjCount-1))] #get random obj index
            newName = self.instanceObjName +'_instanceObj' +'_'+ str(self.PercentCount) +'_'+ str(n)
            self.allInstanceList.append(newName)
            #print allInstanceList 
            #print newName
            #self.totalParticleCount
            #randomRotation = random.uniform(-randomRotation,randomRotation) 

            randomScale = 1 * (random.uniform( (1.0-self.scaleMultiPly),(1.0+self.scaleMultiPly)))
            if self.radioButton_duplicate.isChecked() == True:

                newInstanceObj = cmds.duplicate( sourceObj, n=newName,rc=True,rr=True )
            else:

                newInstanceObj = cmds.instance( sourceObj, n=newName )
            #random position
            pm.parent(newInstanceObj, emptySecGrp)



            if self.lineEdit_randomPosition.text() == "0":
                moveX = self.particlePositionDict[str(n)][0]                
                moveY = self.particlePositionDict[str(n)][1]                 
                moveZ = self.particlePositionDict[str(n)][2] 
                cmds.setAttr( "%s.translateX"%newName,moveX)
                cmds.setAttr( "%s.translateY"%newName,moveY)
                cmds.setAttr( "%s.translateZ"%newName,moveZ)
               # cmds.setAttr( "%s.rotateY"%newName,randomRotation)
                #print moveX,moveY,moveZ
            else:
                #randMoveX = particlePositionDict[str(n)][0] + randMovement/bbMaxDistance
                                    
                #if self.lineEdit_offset.text() == "0":
                   # randMoveY = particlePositionDict[str(n)][1] 
                #else:                      
                   # randMoveY = particlePositionDict[str(n)][1] + float(self.lineEdit_offset.text())
                moveY = self.particlePositionDict[str(n)][1]
                #randMoveY = particlePositionDict[str(n)][1] 
                #randMoveZ = particlePositionDict[str(n)][2] + randMovement/bbMaxDistance               
                #print randMoveX,randMoveY,randMoveZ
                cmds.setAttr( "%s.translateX"%newName,(self.particlePositionDict[str(n)][0] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))

                cmds.setAttr( "%s.translateY"%newName,moveY)
                cmds.setAttr( "%s.translateZ"%newName,(self.particlePositionDict[str(n)][2] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))
                
                #cmds.setAttr( "%s.rotateY"%newName,randomRotation)

                #(particlePositionDict[str(n)][0] +random.uniform(float(self.lineEdit_randomPosition.text())))

            if self.lineEdit_randomScale.text() == "0":
                pass
            else:
                cmds.setAttr( "%s.scaleX"%newName,randomScale)
                cmds.setAttr( "%s.scaleZ"%newName,randomScale)
                
                
            #random rotate

            if self.radioButton_normal.isChecked() == True: 

                rotateNormalx = self.particlePositionDict[str(n)][3]
                rotateNormaly = self.particlePositionDict[str(n)][4]
                rotateNormalz = self.particlePositionDict[str(n)][5]  
                
                
                rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
               # rotX = numpy.deg2rad(numpy.arctan2(rotateNormaly,rotateNormalz))
                rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))
               # rotY = numpy.deg2rad(numpy.arctan2(rotateNormalx,rotateNormalz))

                #rotZ = math.degrees((math.pi/(2.0))-math.asin(rotateNormaly))
                try:
                    rotZ = math.degrees(1.57-math.asin(rotateNormaly))
                    #print "correct",rotateNormaly
                except:
                    #print "error",rotateNormaly
                   # print math.asin(rotateNormaly)
                    rotZ = math.degrees(1.57-abs(math.asin(1.0)))
                    #print "%s"%newName + "   rotZ error"
                    self.errorInstanceObj.append(newName)
                    pass
                #print n,'rotX',rotX
                #print n,'rotY',rotY
                #print n,'rotZ',rotZ
                math.asin(-0.5)
                randRotValue = float(self.lineEdit_randomRotation.text())


                cmds.setAttr( "%s.rotateX"%newName,(rotZ+random.uniform(-randRotValue,randRotValue)))
                cmds.setAttr( "%s.rotateY"%newName,(rotY+random.uniform(-randRotValue,randRotValue)))

               # cmds.setAttr( "%s.rotateY"%newName,randRotValue) 
                #self.returnProcessPersent()
            else:
                pass
            if self.lineEdit_offset.text() == "0":
                pass
            else:
                originalTranslateY = cmds.getAttr("%s.translateY"%newName)
                moveY = originalTranslateY + self.offsetValue
                cmds.setAttr( "%s.translateY"%newName,moveY)
        #print self.errorInstanceObj
        #self.lineEdit_errorMessage.setText(self.errorInstanceObj)




    def checkMode(self):
        if self.label_createMode.text() =='particle Mode': #selectParticleStr
            if int(self.lineEdit_multiple.text()) < 1:
                self.lineEdit_errorMessage.setText('multiply Number Should > = 1')
                pass
            else:
                self.clickButtin_createInstance()

        else:
            self.selectParticleStr = self.lineEdit_sourceParticle.text()
            print self.selectParticleStr
            self.clickButtin_createInstanceFromCache()
            
        self.pushButton_create.setChecked(False)

        


    def clickButtin_createInstance(self):
        sourceObjCount = len(self.selectObjList)
        self.particlePositionDict={}
        self.allInstanceList=[]
        #print "particle",self.selectParticleStr
        bb=cmds.xform('%s'%self.selectParticleStr,bb=True,q=True)
        bbMaxDistance = math.sqrt(((bb[3]-bb[0]) *(bb[3]-bb[0])) + ((bb[4]-bb[1]) *(bb[4]-bb[1])) +((bb[5]-bb[2]) *(bb[5]-bb[2])))
        #print bbMaxDistance
        emptyGrp = pm.createNode('transform', n='%s_instanceGrp'%self.selectParticleStr )
        self.totalParticleCount = pm.nParticle('%s'%self.selectParticleStr, query=True, ct=True)
        #print 'totalParticleCount',totalParticleCount
        # multiplyNum ,if it >= 1 or <0

        multiplyNum= int(self.lineEdit_multiple.text())
        

        
        scaleMultiPly = (float(self.lineEdit_randomScale.text())/(1.0))
        randomPosition = float(self.lineEdit_randomPosition.text())
        randomRotation = float(self.lineEdit_randomRotation.text())
        offsetValue = float(self.lineEdit_offset.text())
        print "multiply",multiplyNum
        print "spread",self.lineEdit_spread.text()
        print "scale", self.lineEdit_randomScale.text()
        print "position",self.lineEdit_randomPosition.text()
        print "rotation",self.lineEdit_randomRotation.text()
        print "offset",self.lineEdit_offset.text()
        

        countGetValue = 0
        for n in range(0,self.totalParticleCount):
            

            perParticle = self.selectParticleStr.pt[n]  
            #print perParticle


            self.positionPP = pm.getParticleAttr(perParticle, at='position',a=True)
            
          #  try:
            self.getVertexNormal()  

            self.positionPP.append(self.avarageNx)
                
            self.positionPP.append(self.avarageNy)
            
            self.positionPP.append(self.avarageNz)
           # except:
             #   self.positionPP.append(0.0)
             #   self.positionPP.append(0.0)
             #   self.positionPP.append(0.0)
            

            self.particlePositionDict.update({str(n):self.positionPP})
            countGetValue = countGetValue +1
            processPresentValue = int(((float(countGetValue)/float(self.totalParticleCount))/2.0)*100.0)
           # print processPresentValue
            self.progressBar.setValue(processPresentValue)
        print "get all data from particle"
            
       # print particlePositionDict
        countSetObj =0
        for n in range(0,self.totalParticleCount):
            countSetObj = countSetObj +1
            processPresentValue = int(((float(countSetObj)/float(self.totalParticleCount))/(2.0) + 0.5)*100.0)
           # print processPresentValue
           # self.progressBar.value(processPresentValue)
            self.progressBar.setValue(processPresentValue)

            for k in range(0,multiplyNum):
                #print n,k
                randMovement = random.uniform((-randomPosition),randomPosition)
                sourceObj = self.selectObjList[random.randint(0,(sourceObjCount-1))] #get random obj index
                newName = self.selectParticleStr+'_instanceObj' +'_'+ str(n)+'_'+str(k)
                self.allInstanceList.append(newName)
                #print allInstanceList 
                #print newName
                #self.totalParticleCount
                #randomRotation = random.uniform(-randomRotation,randomRotation)

                randomScale = 1 * (random.uniform( (1.0-scaleMultiPly),(1.0+scaleMultiPly)))
                if self.radioButton_duplicate.isChecked() == True:

                    newInstanceObj = cmds.duplicate( sourceObj, n=newName,rc=True,rr=True )
                else:

                    newInstanceObj = cmds.instance( sourceObj, n=newName )
                #random position
                pm.parent(newInstanceObj,emptyGrp)



                if self.lineEdit_randomPosition.text() == "0":
                    moveX = self.particlePositionDict[str(n)][0]                
                    moveY = self.particlePositionDict[str(n)][1]                 
                    moveZ = self.particlePositionDict[str(n)][2] 
                    cmds.setAttr( "%s.translateX"%newName,moveX)
                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,moveZ)
                   # cmds.setAttr( "%s.rotateY"%newName,randomRotation)
                    #print moveX,moveY,moveZ
                else:
                    #randMoveX = particlePositionDict[str(n)][0] + randMovement/bbMaxDistance
                                        
                    #if self.lineEdit_offset.text() == "0":
                       # randMoveY = particlePositionDict[str(n)][1] 
                    #else:                      
                       # randMoveY = particlePositionDict[str(n)][1] + float(self.lineEdit_offset.text())
                    moveY = self.particlePositionDict[str(n)][1]
                    #randMoveY = particlePositionDict[str(n)][1] 
                    #randMoveZ = particlePositionDict[str(n)][2] + randMovement/bbMaxDistance               
                    #print randMoveX,randMoveY,randMoveZ
                    cmds.setAttr( "%s.translateX"%newName,(self.particlePositionDict[str(n)][0] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))

                    cmds.setAttr( "%s.translateY"%newName,moveY)
                    cmds.setAttr( "%s.translateZ"%newName,(self.particlePositionDict[str(n)][2] +random.uniform(-float(self.lineEdit_randomPosition.text()),float(self.lineEdit_randomPosition.text()))))
                    
                    #cmds.setAttr( "%s.rotateY"%newName,randomRotation)

                    #(particlePositionDict[str(n)][0] +random.uniform(float(self.lineEdit_randomPosition.text())))

                if self.lineEdit_randomScale.text() == "0":
                    pass
                else:
                    cmds.setAttr( "%s.scaleX"%newName,randomScale)
                    cmds.setAttr( "%s.scaleZ"%newName,randomScale)
                    
                    
                #random rotate

                if self.radioButton_normal.isChecked() == True: 

                    rotateNormalx = self.particlePositionDict[str(n)][3]
                    rotateNormaly = self.particlePositionDict[str(n)][4]
                    rotateNormalz = self.particlePositionDict[str(n)][5]  
                    
                    
                    rotX = math.degrees(math.atan2(rotateNormaly,rotateNormalz))
                    rotY = math.degrees(math.atan2(rotateNormalx,rotateNormalz))

                    #rotZ = math.degrees((math.pi/(2.0))-math.asin(rotateNormaly))
                    try:
                        rotZ = math.degrees(1.57-math.asin(rotateNormaly))
                        #print "correct",rotateNormaly
                    except:
                        #print "error",rotateNormaly
                       # print math.asin(rotateNormaly)
                        rotZ = math.degrees(1.57-abs(math.asin(1.0)))
                        #print "%s"%newName + "   rotZ error"
                        self.errorInstanceObj.append(newName)
                        pass
                    #print n,'rotX',rotX
                    #print n,'rotY',rotY
                    #print n,'rotZ',rotZ
                    math.asin(-0.5)
                    randRotValue = float(self.lineEdit_randomRotation.text())

 
                    cmds.setAttr( "%s.rotateX"%newName,(rotZ+random.uniform(-randRotValue,randRotValue)))
                    cmds.setAttr( "%s.rotateY"%newName,(rotY+random.uniform(-randRotValue,randRotValue)))

                   # cmds.setAttr( "%s.rotateY"%newName,randRotValue) 
                    #self.returnProcessPersent()
                else:
                    pass
                if self.lineEdit_offset.text() == "0":
                    pass
                else:
                    originalTranslateY = cmds.getAttr("%s.translateY"%newName)
                    moveY = originalTranslateY + offsetValue
                    cmds.setAttr( "%s.translateY"%newName,moveY)
        print self.errorInstanceObj
        #self.lineEdit_errorMessage.setText(self.errorInstanceObj)
        self.pushButton_create.setChecked(False)


    def returnProcessPersent(self):
        self.processUnitValue = self.processUnitValue + self.processUnitValue

        
        self.progressBar.value(int(self.processUnitValue))
                

#def main():
def particleInstanceTool2016Main():     
    global ui
    app = QtGui.QApplication.instance()
    if app == None: app = QtGui.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
#if __name__ == '__main__':
#    main()


 