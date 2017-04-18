from PIL import Image
import numpy as np
a = np.array(Image.open("C:/Users/wztxy/Pictures/1.jpg"))
print(a.shape,a.dtype)
b = [-100,-100,-100] + a #修改次行代码可做任意变换
im = Image.fromarray(b.astype('uint8'))
im.save("C:/Users/wztxy/Pictures/2.jpg")