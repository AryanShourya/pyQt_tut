import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
screen = QWidget()
screen.setGeometry(400,400,500,500)
screen.setWindowTitle("Layout combinations")

main_label = QLabel("This is a layout combination example")

label1 = QLabel("This is a vertical layout example")
button1 = QPushButton("button 1")
button2 = QPushButton("button 2")

v_layout = QVBoxLayout()
v_layout.addWidget(label1)
v_layout.addWidget(button1)
v_layout.addWidget(button2)
v_layout.addStretch()

label2 = QLabel("This is horizontal layout")
button3 = QPushButton("button 3")
button4 = QPushButton("button 4")

h_layout = QHBoxLayout()
h_layout.addWidget(label2)
h_layout.addWidget(button3)
h_layout.addWidget(button4)
h_layout.addStretch()

main_layout = QHBoxLayout()
main_layout.addLayout(v_layout)
main_layout.addLayout(h_layout)
main_layout.addStretch()

window_layout = QVBoxLayout()
window_layout.addWidget(main_label,alignment= Qt.AlignCenter)
window_layout.addLayout(main_layout)
window_layout.addStretch()

main_label.setStyleSheet("""
    border:2px solid black;
    background-color : pink;
    padding : 10px;
    font-size : 25px;
    margin : 5px;
""")


screen.setLayout(window_layout)
screen.show()

sys.exit(app.exec_())

