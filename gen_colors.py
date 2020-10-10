import cv2
import os
import numpy as np

save_path = 'colors_png/'
colors = [i for i in range(255)]
width = 30
for c in colors:
    c_png = str(c) + '.png'
    img = np.zeros((width, width), np.uint8)
    c_path = os.path.join(save_path, c_png)
    cv2.circle(img, (width // 2, width // 2), width // 2, c, -1)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # print(img_bgr.shape)
    cv2.imwrite(c_path, img_bgr)

# img_test = cv2.imread('./colors_png/220.png')
# print(img_test.shape)
