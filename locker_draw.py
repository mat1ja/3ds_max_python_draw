import os
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QGroupBox

from PySide2.QtGui import QPixmap
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from pymxs import runtime as rt


class TestDialog(QDialog):
    def __init__(self, parent=QWidget.find(rt.windows.getMAXHWND())):
        QDialog.__init__(self, parent)
        loader = QUiLoader()
        ui_file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "ui\\test.ui"
        )
        # print(ui_file_path)
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        self.setWindowTitle("Pyside Qt  Dock Window")
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)
        self.resize(332, 463)
        label = self.ui.findChild(QLabel, "label")
        pixmap = QPixmap("ui\\type_1.jpg")
        label.setPixmap(pixmap)

        btn = self.ui.findChild(QPushButton, "pushButton")
        btn.clicked.connect(self.makeTeapot)

    def makeTeapot(self):
        lineEdit = self.ui.findChild(QLineEdit, "lineEdit").text()

        print(lineEdit)
        rt.teapot()
        rt.redrawViews()


def main():
    dlg = TestDialog()
    dlg.show()


if __name__ == "__main__":
    main()
