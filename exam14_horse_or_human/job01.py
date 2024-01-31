from PIL import Image   #pip install pillow
import glob
import numpy as np
from sklearn.model_selection import train_test_split

horse_img_dir = '../datasets/horse_or_human/horses/'
categories = ['horse']
human_img_dir = '../datasets/horse_or_human/humans/'
categories.append('human')
image_w = 64
image_h = 64

pixel = image_h * image_w *3
X = []
Y = []
files =None

for idx,category in enumerate(categories):
    if idx == 0:
        files = glob.glob(horse_img_dir + category + '*.png')
    else:
        files = glob.glob(human_img_dir + category + '*.png')
    for i,f in enumerate(files):
        try:
            img = Image.open(f)
            img = img.convert('RGB')
            img = img.resize((image_w,image_h))
            data = np.asarray(img)
            X.append(data)
            Y.append(idx)
            if i % 300 ==0:                 #포문이 도는지 확인 구문
                print(category, ':' , f)
        except:
            print('error:', category, f)

X = np.array(X)
Y = np.array(Y)
X = X/255
print(X[0])
print(Y[0])
X_train, X_test , Y_train, Y_test = train_test_split(X,Y,test_size=0.2)
xy = (X_train, X_test , Y_train, Y_test)
np.save('../datasets/bi_image_data.npy',xy)

