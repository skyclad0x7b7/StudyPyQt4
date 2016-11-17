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
		self.watcher = QtCore.QFileSystemWatcher(self)

		QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.file_dialog)
		QtCore.QObject.connect(self.ui.button_save, QtCore.SIGNAL("clicked()"), self.file_save)
		QtCore.QObject.connect(self.ui.textBrowser, QtCore.SIGNAL("textChanged()"), self.enable_save)
		QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.file_close)
		QtCore.QObject.connect(self.watcher, QtCore.SIGNAL("fileChanged(const QString&)"), self.file_changed)
		self.initalize()

	def initalize(self):
		self.ui.textBrowser.setPlainText("")
		self.ui.button_save.setEnabled(False)
		self.setWindowTitle("Final Text Editor")
		self.filename = ""

	def file_dialog(self):
		fd = QtGui.QFileDialog(self)
		newFile = fd.getOpenFileName()
		if isfile(newFile) and self.filename != newFile:
			s = codecs.open(newFile, 'r', 'utf-8').read()
			self.ui.textBrowser.setPlainText(s)
			self.setWindowTitle(newFile)
			self.ui.button_save.setEnabled(False)
			if self.filename != "":
				self.watcher.removePath(self.filename)
			self.watcher.addPath(newFile)
			self.filename = newFile

	def enable_save(self):
		self.ui.button_save.setEnabled(True)

	def file_save(self):
		if self.filename != "" and isfile(self.filename): # File Opened and exists
			file = codecs.open(self.filename, 'w', 'utf-8')
			file.write(unicode(self.ui.textBrowser.toPlainText()))
			file.close()
			self.ui.button_save.setEnabled(False)
		else: # File not opened or not exists
			fd = QtGui.QFileDialog(self)
			newFile = fd.getSaveFileName()
			if newFile:
				s = codecs.open(newFile, 'w', 'utf-8')
				s.write(unicode(self.ui.textBrowser.toPlainText()))
				s.close();
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

	def file_changed(self, path):
		response = False

		# Button texts
		SAVE 	= 'Save AS'
		RELOAD 	= 'Reload File'
		CANCEL 	= 'Cancel'
		message = QtGui.QMessageBox(self)
		message.setText('Opened file have been changed!')
		message.setWindowTitle('Final Text Editor')
		message.setIcon(QtGui.QMessageBox.Warning)
		message.addButton(SAVE, QtGui.QMessageBox.AcceptRole)
		message.addButton(RELOAD, QtGui.QMessageBox.DestructiveRole)
		message.addButton(CANCEL, QtGui.QMessageBox.RejectRole)
		message.setDetailedText('The File "{0}" have been changed or removed by other application. What do you want to do?'.format(self.filename))
		message.exec_()
		response = message.clickedButton().text()
		# Save Current File to new
		if response == SAVE:
			fd = QtGui.QFileDialog(self)
			newFile = fd.getSaveFileName()
			if newFile:
				s = codecs.open(newFile, 'w', 'utf-8')
				s.write(unicode(self.ui.textBrowser.toPlainText()))
				s.close()
				self.ui.button_save.setEnabled(False)
				# new file, remove old and add the new one to the watcher
				if self.filename and str(newFile) != str(self.filename):
					self.watcher.removePath(self.filename)
					self.watcher.addPath(newFile)
					self.filename = newFile
		# reload the text in the editor
		elif response == RELOAD:
			s = codecs.open(self.filename, 'r', 'utf-8').read()
			self.ui.textBrowser.setPlainText(s)
			self.ui.button_save.setEnabled(False)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())