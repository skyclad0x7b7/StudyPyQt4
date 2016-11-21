# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(593, 395)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(0, 40, 591, 331))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button_prev = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.button_prev.setObjectName(_fromUtf8("button_prev"))
        self.horizontalLayout.addWidget(self.button_prev)
        self.button_stop = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.button_stop.setObjectName(_fromUtf8("button_stop"))
        self.horizontalLayout.addWidget(self.button_stop)
        self.button_reload = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.button_reload.setObjectName(_fromUtf8("button_reload"))
        self.horizontalLayout.addWidget(self.button_reload)
        self.button_next = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.button_next.setObjectName(_fromUtf8("button_next"))
        self.horizontalLayout.addWidget(self.button_next)
        self.lineEdit_url = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.horizontalSlider_opacity = QtGui.QSlider(self.horizontalLayoutWidget)
        self.horizontalSlider_opacity.setMaximum(99)
        self.horizontalSlider_opacity.setSliderPosition(99)
        self.horizontalSlider_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_opacity.setObjectName(_fromUtf8("horizontalSlider_opacity"))
        self.horizontalLayout.addWidget(self.horizontalSlider_opacity)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "WebBrowser", None))
        self.button_prev.setText(_translate("MainWindow", "<", None))
        self.button_stop.setText(_translate("MainWindow", "Stop", None))
        self.button_reload.setText(_translate("MainWindow", "Reload", None))
        self.button_next.setText(_translate("MainWindow", ">", None))

from PyQt4 import QtWebKit
