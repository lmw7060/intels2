import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_window = uic.loadUiType('./poster.ui')[0]

class Exam(QWidget,form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_t.clicked.connect(self.btn_clicked_slot)
        self.btn_r.clicked.connect(self.btn_clicked_slot)
        self.btn_i.clicked.connect(self.btn_clicked_slot)
        self.btn_g.clicked.connect(self.btn_clicked_slot)

    def btn_clicked_slot(self):
        btn =self.sender()
        self.lbl_t.hide()
        self.lbl_r.hide()
        self.lbl_i.hide()
        self.lbl_g.hide()
        if btn.objectName() =='btn_t':
            self.lbl_t.show()
        elif btn.objectName() =='btn_r':
            self.lbl_r.show()
        elif btn.objectName() =='btn_i':
            self.lbl_i.show()
        elif btn.objectName() =='btn_g':
            self.lbl_g.show()

if __name__ =='__main__':
    app =QApplication(sys.argv)
    mainWindow=Exam()
    mainWindow.show()
    sys.exit(app.exec_())

