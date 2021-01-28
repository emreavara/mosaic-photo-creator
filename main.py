import numpy as np
import cv2
from PIL import Image

def combine_images(imageList):
    return cv2.vconcat([cv2.hconcat(imageList_hor) for imageList_hor in imageList])

def dot_product(image1,image2):
    x,y,z = image1.shape
    for i in range(x):
        for j in range(y):
            for k in range(z):
                image1[i][j][k]= (image1[i][j][k]*100)*(image2[i][j][k]/100)
    return image1


source_dir = "source_photos\\"
target_dir = "target_photos\\"
target_photo = "OWKI6758.JPG"

target_image = cv2.imread(target_dir + target_photo ,1)
target_image_gray = cv2.imread(target_dir + target_photo,0)
print(target_image.shape)
print(target_image_gray.shape)

# target_image_resized = cv2.resize(target_image,(60*12,45*25), interpolation = cv2.INTER_AREA)
# target_image_ratio = target_image_resized/255
target_image_resized = cv2.resize(target_image,(60*25,45*12), interpolation = cv2.INTER_AREA)
target_image_ratio = target_image_resized/255



dim = (60,45)
image_list =[]
for image in range(300):
    image_name = "{}.JPG".format(image)
    image_list.append(source_dir + image_name)
    image_list[image] =  cv2.resize((cv2.imread(image_list[image],1)),dim, interpolation = cv2.INTER_AREA)
    image_list[image] = cv2.add(image_list[image], np.array([125.0]))

print(image_list)
cv2.imshow("img",image_list[1])
"""
for image in range(len(image_list)):
    image_list[image] = cv2.resize(image_list[image],
"""


image_list_hor = []
for i in range(12):
    image_list_hor.append([])
    for j in range(25):
        counter = i*6+j
        image_list_hor[i].append(image_list[counter])

combined_image = combine_images(image_list_hor)


mosaic_photo = dot_product(target_image_ratio,combined_image)

cv2.imshow("img",mosaic_photo)
cv2.imwrite('out.png', mosaic_photo)
cv2.waitKey(0)

