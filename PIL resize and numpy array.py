import os
import numpy as np
from PIL import Image


size=(200,200,3)
# photos=np.ones(200,200,3)
rootDir = 'Image_folder'

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:    
        print('-------------------\t%s' % fname)
        img=Image.open(f"{rootDir}/{fname}")
        arr=np.array(img)
        print(arr)
        img=Image.fromarray(arr)
        img.thumbnail(size)
        print(img)
        img.show()

