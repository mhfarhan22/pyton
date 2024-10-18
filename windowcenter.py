#================ Window Management ===============================
from PyQt5.QtWidgets import Qapplication, QPushButton, QLabel, Qwidget, QAPPlication, QPushButton, QLabel, QDesktopwidget

class MyWindow(Qmainwindow)
    def __init__(self):
        super().__init__()
        self.label = QLabel(seft)
        self.label.setText("Label11")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setgeometry(0,0,400,400)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.framegeometry() # cek ukuran main window app kita
        cwc = QDesktopwidget().avaiblegeometry().center() # pada screen saya: (662,363)
        #print(cwc)
        cwa.movecenter(cwc)
        self.move(cwa.topleft())

app = Qapplication([])     
window = myWindow(
window.show()
app.exec()   
