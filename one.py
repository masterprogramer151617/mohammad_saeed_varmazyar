
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QPixmap

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# Load the image
pixmap = QPixmap("00000.jpg")

# Create a QLabel to display the image
label = QLabel()
label.setPixmap(pixmap)

layout.addWidget(label)
window.setLayout(layout)
window.show()
app.exec()


