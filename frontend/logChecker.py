import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets, QtGui
from ui_logchecker import Ui_MainWindow
sys.path.append('../core/')
from service import getresponse

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.logContents.setReadOnly(True)
        appservers=[]
        try:
            appservers = getresponse("http://127.0.0.1:5001/machines")
        except:
            appservers=[]
            pass
        list = []
        list.append("Select a machine")
        for server in appservers:
            list.append(server)
        self.ui.machinesCombo.addItems(list)

        self.ui.numLines.setValue(3)
        self.ui.numLines.setMinimum(1)
        self.ui.show.setVisible(False)        
        self.ui.show.clicked.connect(self.showContents)
        self.ui.quit.clicked.connect(self.quitApp)
        self.ui.machinesCombo.activated.connect(self.machineSelected)
        self.ui.numLines.valueChanged.connect(self.numLinesChanged)
        self.ui.search.textEdited.connect(self.searchChanged)
        self.ui.logsList.itemClicked.connect(self.logSelected)

    @QtCore.Slot()
    def logSelected(self, item):
        self.showContents()

    @QtCore.Slot()
    def searchChanged(self, text):
        self.showContents()

    @QtCore.Slot()
    def numLinesChanged(self, value):
        self.showContents()    

    @QtCore.Slot()
    def showContents(self):
        item = self.ui.logsList.currentItem()
        if item is None:
            return
        log = item.text()
        path = "http://127.0.0.1:5001/" + "machines/"
        path += self.ui.machinesCombo.currentText() + "/"
        path += log + "?"
        lines = self.ui.numLines.value()
        if lines != 0:
            path += "n=" + str(lines) + "&"
        s = self.ui.search.text()
        if s != "":
            path += "search=" + s
        list = getresponse(path)
        text = ''.join(list)
        self.ui.logContents.setText(text)
        
    @QtCore.Slot()
    def quitApp(self):
        sys.exit()
        
    @QtCore.Slot()
    def machineSelected(self, index):
        self.ui.logsList.clear()
        if index == 0:
            return
        m = self.ui.machinesCombo.itemText(index)
        path = "http://127.0.0.1:5001/" + "machines/" + m
        list = getresponse(path)
        self.ui.logsList.addItems(list)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Log Viewer")
    window.show()

    sys.exit(app.exec())
