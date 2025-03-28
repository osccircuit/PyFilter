from PySide6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle('PySide6 Application')
window.resize(300, 250)

lbl = QtWidgets.QLabel('Hello World!')
btn = QtWidgets.QPushButton('Close')

box = QtWidgets.QVBoxLayout()
box.addWidget(lbl)
box.addWidget(btn)

window.setLayout(box)

btn.clicked.connect(app.quit)
window.show()

sys.exit(app.exec())