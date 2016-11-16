import sys
from PyQt4 import QtCore, QtGui
from Main import Ui_QYolk
from yolk import yolklib

class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_QYolk()
		self.ui.setupUi(self)
		self.ui.info_label.setText("")

		# set Column Width
		self.ui.all_list.setColumnWidth(0, 200)
		self.ui.all_list.setColumnWidth(1, 200)
		self.ui.active_list.setColumnWidth(0, 200)
		self.ui.active_list.setColumnWidth(1, 200)
		self.ui.not_active_list.setColumnWidth(0, 200)
		self.ui.not_active_list.setColumnWidth(1, 200)

		QtCore.QObject.connect(self.ui.tab_widget, QtCore.SIGNAL("currentChanged(int)"), self.tab_changed)

		packages = yolklib.Distributions()
		for pkg in packages.get_distributions('all'):
			newItem = QtGui.QTreeWidgetItem(self.ui.all_list)
			pk = str(pkg[0]).split(' ')
			if pkg[1]:
				status = 'Active'
			else:
				status = 'Not Active'
				newItem.setTextColor(0, QtGui.QColor(128, 128, 128))
				newItem.setTextColor(1, QtGui.QColor(128, 128, 128))
				newItem.setTextColor(2, QtGui.QColor(128, 128, 128))
				
			newItem.setText(0, pk[0])
			newItem.setText(1, pk[1])
			newItem.setText(2, status)

		for pkg in packages.get_distributions('active'):
			newItem = QtGui.QTreeWidgetItem(self.ui.active_list)
			pk = str(pkg[0]).split(' ')
			newItem.setText(0, pk[0])
			newItem.setText(1, pk[1])
			newItem.setText(2, 'Active')

		for pkg in packages.get_distributions('nonactive'):
			newItem = QtGui.QTreeWidgetItem(self.ui.not_active_list)
			pk = str(pkg[0]).split(' ')
			newItem.setText(0, pk[0])
			newItem.setText(1, pk[1])
			newItem.setText(2, 'Not Active')

	def tab_changed(self, column):
		if column == 0:
			message = "<b>QYolk</b> : Browsing all installed cheeseshop packages"
		elif column == 1:
			message = "<b>QYolk</b> : Browsing active packages"
		elif column == 2:
			message = "<b>QYolk</b> : Browsing not active packages (older versions)"

		self.ui.info_label.setText(message)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())