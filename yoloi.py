import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
#%config InlineBackend.figure_format = 'svg'
option = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 1200,
    'threshold': 0.1,
    'gpu': 0.8 
}
tfnet = TFNet(option)
img = cv2.imread('rev3.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result = tfnet.return_predict(img)
tl = (result[0]['topleft']['x'], result[0]['topleft']['y'])
br = (result[0]['bottomright']['x'], result[0]['bottomright']['y'])
label = result[0]['label']


img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
plt.imshow(img)
plt.show()

