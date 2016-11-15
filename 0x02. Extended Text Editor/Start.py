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
		self.filename = ""

		QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.file_dialog)
		QtCore.QObject.connect(self.ui.button_save, QtCore.SIGNAL("clicked()"), self.file_save)
		QtCore.QObject.connect(self.ui.textBrowser, QtCore.SIGNAL("textChanged()"), self.enable_save)
		QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.file_close)
		self.initalize()

	def initalize(self):
		self.ui.textBrowser.setPlainText("")
		self.ui.button_save.setEnabled(False)
		self.setWindowTitle("Extended Text Editor")

	def file_dialog(self):
		fd = QtGui.QFileDialog(self)
		self.filename = fd.getOpenFileName()
		if isfile(self.filename):
			s = codecs.open(self.filename, 'r', 'utf-8').read()
			self.ui.textBrowser.setPlainText(s)
			self.setWindowTitle(self.filename)
			self.ui.button_save.setEnabled(False)

	def enable_save(self):
		self.ui.button_save.setEnabled(True)

	def file_save(self):
		if isfile(self.filename):
			file = codecs.open(self.filename, 'w', 'utf-8')
			file.write(unicode(self.ui.textBrowser.toPlainText()))
			file.close()
			self.ui.button_save.setEnabled(False)

	def file_close(self):
		if isfile(self.filename):
			# not saved
			if self.ui.button_save.isEnabled():
				message = QtGui.QMessageBox(self)
				message.setText('Would you like to save the file before closing?')
				message.setWindowTitle("Warning")
				message.setIcon(QtGui.QMessageBox.Question)
				message.addButton('Save', QtGui.QMessageBox.AcceptRole)
				message.addButton('Discard', QtGui.QMessageBox.DestructiveRole)
				message.addButton('Cancel', QtGui.QMessageBox.RejectRole)
				message.setDetailedText('Unsaved changes in file: ' + str(self.filename))
				message.exec_()
				response = message.clickedButton().text()
				if response == 'Save':
					self.file_save()
					self.ui.button_save.setEnabled(False)
				elif response == 'Discard':
					self.initalize()
				else:
					pass
			else:
				self.initalize()
					
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())