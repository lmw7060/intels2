import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

form_window = uic.loadUiType('./cat_and_dog.ui')[0]

class Exam(QWidget,form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path = ('C:/Users/PC/work/python/AI_intel_S2/datasets/test_img/test02.jpg', 'Image File(*.jpg;*.png)')
        self.model = load_model('./cat_and_dog_0.834.h5')
        self.btn_open.clicked.connect(self.btn_clicked_slot)

    def btn_clicked_slot(self):
        old_path = self.path
        self.path = QFileDialog.getOpenFileName(self,'Open file',           #파일 선택
                                                '../datasets/cat_dog',
                                                'Image File(*.jpg;*.png);;''All Files(*.*)')
        print(self.path)
        if self.path[0] == '':
            self.path = old_path
        pixmap = QPixmap(self.path[0])      #pixmap에 경로를 받는다
        self.lbl_image.setPixmap(pixmap)    #image 출력

        img = Image.open(self.path[0])      #경로
        img = img.convert('RGB')
        img = img.resize((64, 64))
        data = np.asarray(img)
        data = data /255
        data = data.reshape(1,64,64,3)
        pred = self.model.predict(data)
        print(pred)

        if pred <0.5:
            self.lbl_result.setText('고양이이다.')
        else:
            self.lbl_result.setText('개다.')


if __name__ =='__main__':
    app =QApplication(sys.argv)
    mainWindow=Exam()
    mainWindow.show()
    sys.exit(app.exec_())
