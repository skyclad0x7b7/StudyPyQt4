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

class Ui_QYolk(object):
    def setupUi(self, QYolk):
        QYolk.setObjectName(_fromUtf8("QYolk"))
        QYolk.resize(565, 321)
        self.centralwidget = QtGui.QWidget(QYolk)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeList = QtGui.QTreeWidget(self.centralwidget)
        self.treeList.setGeometry(QtCore.QRect(10, 10, 541, 271))
        self.treeList.setMaximumSize(QtCore.QSize(541, 16777215))
        self.treeList.setObjectName(_fromUtf8("treeList"))
        self.treeList.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.treeList.headerItem().setBackground(0, QtGui.QColor(230, 230, 230))
        self.treeList.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.treeList.headerItem().setBackground(1, QtGui.QColor(230, 230, 230))
        self.treeList.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.treeList.headerItem().setBackground(2, QtGui.QColor(230, 230, 230))
        self.treeList.header().setCascadingSectionResizes(True)
        self.treeList.header().setHighlightSections(True)
        self.treeList.header().setSortIndicatorShown(False)
        QYolk.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QYolk)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QYolk.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QYolk)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QYolk.setStatusBar(self.statusbar)

        self.retranslateUi(QYolk)
        QtCore.QMetaObject.connectSlotsByName(QYolk)

    def retranslateUi(self, QYolk):
        QYolk.setWindowTitle(_translate("QYolk", "QYolk", None))
        self.treeList.headerItem().setText(0, _translate("QYolk", "Package Name", None))
        self.treeList.headerItem().setText(1, _translate("QYolk", "Version", None))
        self.treeList.headerItem().setText(2, _translate("QYolk", "Status", None))

