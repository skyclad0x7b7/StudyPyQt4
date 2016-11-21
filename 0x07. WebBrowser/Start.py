import sys
from Main import Ui_MainWindow
from PyQt4 import QtCore, QtGui, QtWebKit

class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.start_page = "about:blank"
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.initialize()
		self.ui.webView.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)

		QtCore.QObject.connect(self.ui.lineEdit_url, QtCore.SIGNAL("returnPressed()"), self.url_changed)
		QtCore.QObject.connect(self.ui.button_reload, QtCore.SIGNAL("clicked()"), self.reload_clicked)
		QtCore.QObject.connect(self.ui.button_prev, QtCore.SIGNAL("clicked()"), self.prev_clicked)
		QtCore.QObject.connect(self.ui.button_next, QtCore.SIGNAL("clicked()"), self.next_clicked)
		QtCore.QObject.connect(self.ui.button_stop, QtCore.SIGNAL("clicked()"), self.stop_clicked)
		QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("linkClicked (const QUrl&)"), self.link_clicked)
		QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("loadProgress (int)"), self.load_progress)
		QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("titleChanged (const QString&)"), self.title_changed)
		QtCore.QObject.connect(self.ui.horizontalSlider_opacity, QtCore.SIGNAL("sliderMoved(int)"), self.opacity_changed)

	def stop_clicked(self):
		self.ui.webView.stop()

	def reload_clicked(self):
		self.ui.webView.setUrl(QtCore.QUrl(self.ui.lineEdit_url.text()))

	def prev_clicked(self):
		page = self.ui.webView.page()
		history = page.history()
		history.back()
		if history.canGoBack():
			self.ui.button_prev.setEnabled(True)
		else:
			self.ui.button_prev.setEnabled(False)

		self.ui.button_next.setEnabled(True)


	def next_clicked(self):
		page = self.ui.webView.page()
		history = page.history()
		history.forward()
		if history.canGoForward():
			self.ui.button_next.setEnabled(True)
		else:
			self.ui.button_next.setEnabled(False)

		self.ui.button_prev.setEnabled(True)

	def url_changed(self):
		# url changed by user
		curr_page = self.ui.webView.page()
		history = curr_page.history()
		if history.canGoBack():
			self.ui.button_prev.setEnabled(True)
		else:
			self.ui.button_prev.setEnabled(False)

		if history.canGoForward():
			self.ui.button_next.setEnabled(True)
		else:
			self.ui.button_next.setEnabled(False)

		self.ui.button_reload.setEnabled(True)
		url = self.ui.lineEdit_url.text()
		self.ui.webView.setUrl(QtCore.QUrl(url))

	def link_clicked(self, url):
		# link clicked
		curr_page = self.ui.webView.page()
		history = curr_page.history()
		if history.canGoBack():
			self.ui.button_prev.setEnabled(True)
		else:
			self.ui.button_prev.setEnabled(False)

		if history.canGoForward():
			self.ui.button_next.setEnabled(True)
		else:
			self.ui.button_next.setEnabled(False)

		self.ui.button_reload.setEnabled(True)
		self.ui.lineEdit_url.setText(url.toString())
		self.reload_clicked()

	def load_progress(self, load):
		if load == 100:
			self.ui.button_stop.setEnabled(False)
		else:
			self.ui.button_stop.setEnabled(True)

	def title_changed(self, title):
		self.setWindowTitle(title)

	def opacity_changed(self, value):
		self.setWindowOpacity((value + 1)/100.0)


	def initialize(self):
		self.ui.button_prev.setEnabled(False)
		self.ui.button_next.setEnabled(False)
		self.ui.button_stop.setEnabled(False)
		self.ui.button_reload.setEnabled(False)
		self.ui.lineEdit_url.setText(self.start_page)
		self.ui.webView.setUrl(QtCore.QUrl(self.start_page))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())