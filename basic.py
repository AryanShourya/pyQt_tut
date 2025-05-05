import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

def on_button_click():
    label.setText("You clicked the button")

# we create an object of the application window
app = QApplication(sys.argv)

# now we create a window of the application
window = QWidget()
window.setWindowTitle("PtQt app first")
window.setGeometry(500,100,500,500)

# now we can add a label and a button to the window

label= QLabel("click the button below",window)
label.move(50,50) #position in the window

button = QPushButton("click me",window)
button.move(50,70)

button.clicked.connect(on_button_click)
window.show()

sys.exit(app.exec_())