import os
import sys
from skimage import data, io
from PIL import Image
dirs='SR_training_datasets/BSDS200'
files = []
file_names = []
count = 0


for f in os.listdir(dirs): 
    if f.endswith('.png'):
        im = Image.open(os.path.join(dirs,f)).convert("RGB")
        width, height = im.size
        print(width, height)
        im.show()


        
width, height = im.size

# for f in os.listdir(dirs): 
#     if f.endswith('.png'):
#         image = data.imread(os.path.join(dirs,f))
#         if len(image.shape) > 2:
#             files.append(image)
#             file_names.append(os.path.join(dirs,f))
#         count = count + 1
#         print(image.shape)
