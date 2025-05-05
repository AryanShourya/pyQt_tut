import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setGeometry( 300,200,700,700)
window.setWindowTitle('layout example')


label = QLabel('example of layouts',window)
button = QPushButton("first button",window)

label2 = QLabel('second label',window)
button2 = QPushButton('second button',window)

label3 = QLabel('third label',window)
button3 = QPushButton('third button',window)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(label2)
layout.addWidget(button2)
layout.addWidget(label3)
layout.addWidget(button3)
layout.addStretch()
window.setLayout(layout)
window.show()

sys.exit(app.exec_())


