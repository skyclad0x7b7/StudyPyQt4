import sys
from Main import Ui_QYolk
from PyQt4 import QtCore, QtGui
from yolk import yolklib
from os.path import expanduser
from yolk.cli import get_pkglist
from yolk.yolklib import get_highest_version, get_distributions, get_highest_installed
from yolk.pypi import CheeseShop
import pkg_resources
from os.path import isfile
from datetime import timedelta
from datetime import datetime

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
		self.ui.update_list.setColumnWidth(0, 200)
		self.ui.update_list.setColumnWidth(1, 200)

		QtCore.QObject.connect(self.ui.tab_widget, QtCore.SIGNAL("currentChanged(int)"), self.tab_changed)

		packages = get_distributions('all')
		for pkg in packages:
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

		for pkg in get_distributions('active'):
			newItem = QtGui.QTreeWidgetItem(self.ui.active_list)
			pk = str(pkg[0]).split(' ')
			newItem.setText(0, pk[0])
			newItem.setText(1, pk[1])
			newItem.setText(2, 'Active')

		for pkg in get_distributions('nonactive'):
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
		elif column == 3:
			message = "<b>QYolk</b> : Browsing available updates"
			for pkg in get_fresh_updates():
				newItem = QtGui.QTreeWidgetItem(self.ui.update_list)
				newItem.setText(0, pkg[0])
				newItem.setText(1, pkg[1])
				newItem.setText(2, pkg[2])

		self.ui.info_label.setText(message)

		

def get_fresh_updates(package_name = "", version = ""):
	ret = []
	pypi = CheeseShop()
	for pkg in get_pkglist():
		for (dist, active) in get_distributions("all", pkg, get_highest_installed(pkg)):
			(project_name, versions) = pypi.query_versions_pypi(dist.project_name)
			if versions:
				newest = get_highest_version(versions)
				if newest != dist.version:
					if pkg_resources.parse_version(dist.version) < pkg_resources.parse_version(newest):
						ret.append([project_name, dist.version, newest])

	return ret


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())