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
        QYolk.resize(565, 345)
        self.centralwidget = QtGui.QWidget(QYolk)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tab_widget = QtGui.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(10, 0, 551, 291))
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.tab_all_packages = QtGui.QWidget()
        self.tab_all_packages.setObjectName(_fromUtf8("tab_all_packages"))
        self.all_list = QtGui.QTreeWidget(self.tab_all_packages)
        self.all_list.setGeometry(QtCore.QRect(0, 0, 541, 261))
        self.all_list.setObjectName(_fromUtf8("all_list"))
        self.tab_widget.addTab(self.tab_all_packages, _fromUtf8(""))
        self.tab_active = QtGui.QWidget()
        self.tab_active.setObjectName(_fromUtf8("tab_active"))
        self.active_list = QtGui.QTreeWidget(self.tab_active)
        self.active_list.setGeometry(QtCore.QRect(0, 0, 541, 261))
        self.active_list.setObjectName(_fromUtf8("active_list"))
        self.tab_widget.addTab(self.tab_active, _fromUtf8(""))
        self.tab_not_active = QtGui.QWidget()
        self.tab_not_active.setObjectName(_fromUtf8("tab_not_active"))
        self.not_active_list = QtGui.QTreeWidget(self.tab_not_active)
        self.not_active_list.setGeometry(QtCore.QRect(0, 0, 541, 261))
        self.not_active_list.setObjectName(_fromUtf8("not_active_list"))
        self.tab_widget.addTab(self.tab_not_active, _fromUtf8(""))
        self.tab_update = QtGui.QWidget()
        self.tab_update.setObjectName(_fromUtf8("tab_update"))
        self.update_list = QtGui.QTreeWidget(self.tab_update)
        self.update_list.setGeometry(QtCore.QRect(0, 0, 551, 271))
        self.update_list.setObjectName(_fromUtf8("update_list"))
        self.tab_widget.addTab(self.tab_update, _fromUtf8(""))
        self.info_label = QtGui.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(10, 285, 541, 31))
        self.info_label.setObjectName(_fromUtf8("info_label"))
        QYolk.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QYolk)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QYolk.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QYolk)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QYolk.setStatusBar(self.statusbar)

        self.retranslateUi(QYolk)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QYolk)

    def retranslateUi(self, QYolk):
        QYolk.setWindowTitle(_translate("QYolk", "QYolk III", None))
        self.all_list.headerItem().setText(0, _translate("QYolk", "Package Name", None))
        self.all_list.headerItem().setText(1, _translate("QYolk", "Version", None))
        self.all_list.headerItem().setText(2, _translate("QYolk", "Status", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_all_packages), _translate("QYolk", "All Packages", None))
        self.active_list.headerItem().setText(0, _translate("QYolk", "Package Name", None))
        self.active_list.headerItem().setText(1, _translate("QYolk", "Version", None))
        self.active_list.headerItem().setText(2, _translate("QYolk", "Status", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_active), _translate("QYolk", "Active", None))
        self.not_active_list.headerItem().setText(0, _translate("QYolk", "Package Name", None))
        self.not_active_list.headerItem().setText(1, _translate("QYolk", "Version", None))
        self.not_active_list.headerItem().setText(2, _translate("QYolk", "Status", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_not_active), _translate("QYolk", "Not Active", None))
        self.update_list.headerItem().setText(0, _translate("QYolk", "Package Name", None))
        self.update_list.headerItem().setText(1, _translate("QYolk", "Installed Version", None))
        self.update_list.headerItem().setText(2, _translate("QYolk", "Available Version", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_update), _translate("QYolk", "Updates", None))
        self.info_label.setText(_translate("QYolk", "TextLabel", None))

