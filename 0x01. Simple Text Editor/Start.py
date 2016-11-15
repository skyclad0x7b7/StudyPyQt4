import sys
import codecs
from os.path import isfile
from PyQt4 import QtCore, QtGui
from Main import Ui_notepad

class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_notepad()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.file_dialog)
		QtCore.QObject.connect(self.ui.button_save, QtCore.SIGNAL("clicked()"), self.file_save)
		self.filename = ""

	def file_dialog(self):
		fd = QtGui.QFileDialog(self)
		self.filename = fd.getOpenFileName()
		if isfile(self.filename):
			s = codecs.open(self.filename, 'r', 'utf-8').read()
			self.ui.textBrowser.setPlainText(s)
			self.setWindowTitle(self.filename)


	def file_save(self):
		if isfile(self.filename):
			file = codecs.open(self.filename, 'w', 'utf-8')
			file.write(unicode(self.ui.textBrowser.toPlainText()))
			file.close()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())