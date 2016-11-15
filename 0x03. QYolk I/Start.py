import sys
from PyQt4 import QtCore, QtGui
from Main import Ui_QYolk
from yolk import yolklib

class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_QYolk()
		self.ui.setupUi(self)

		# set Column Width
		self.ui.treeList.setColumnWidth(0, 200)
		self.ui.treeList.setColumnWidth(1, 200)

		packages = yolklib.Distributions()
		for pkg in packages.get_distributions('all'):
			newItem = QtGui.QTreeWidgetItem(self.ui.treeList)
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

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())