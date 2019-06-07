import os
import sys
from skimage import data, io
from skimage.transform import rescale, resize, downscale_local_mean
dirs='SR_training_datasets/DIV2K_valid_HR'
files = []
file_names = []
count = 0


for f in os.listdir(dirs): 
    if f.endswith('.png'):

        im = io.imread(os.path.join(dirs,f))
        # width, height = im.size
        print(im.shape[0])
        image_resized = resize(im, (96, 96),
                       anti_aliasing=True)

        # image_downscaled = downscale_local_mean(im, (64, 64))

        outpath=dirs+'_96/'+f
        io.imsave(outpath, image_resized) 



# width, height = im.size

# for f in os.listdir(dirs): 
#     if f.endswith('.png'):
#         image = data.imread(os.path.join(dirs,f))
#         if len(image.shape) > 2:
#             files.append(image)
#             file_names.append(os.path.join(dirs,f))
#         count = count + 1
#         print(image.shape)

