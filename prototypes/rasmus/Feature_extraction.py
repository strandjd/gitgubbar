
#   https://www.mygreatlearning.com/blog/feature-extraction-in-image-processing/#sh8 Here are all the code and explinations that is needed.


"""How to use Feature Extraction technique for Image Data: Features as Grayscale Pixel Value
If we use  the same example as our image which we use above in the section– the dimension of the image is 28 x 28 right? But can you guess the number of features for this image?

The number of features is  same as the number of pixels so  that the number will be 784

So now I have one more important question –

how do we declare  these 784 pixels as features of this image? Do you ever think about that?

So the solution is, you just can simply append every pixel value one after the other to generate a feature vector for the image. Let’s visualize that,


Now let’s have a look at the coloured image,"""


"""image = imread('https://d1m75rqqgidzqn.cloudfront.net/content/pexels-photo-1108099.jpeg')
imshow(image)

1
print(image.shape)
(375, 500, 3)"""


image = imread('https://d1m75rqqgidzqn.cloudfront.net/content/pexels-photo-1108099.jpeg', as_gray=True) 
image.shape, imshow(image)

# (375, 500)
print(image.shape)

he image shape for this image is  375 x 500. So, the number of features will be  187500.

o now if you want to change the shape of the image that is also can be done by using the reshape function from NumPy where we specify the dimension of the image:

1
2
3
#Find the pixel features
feature = np.reshape(image, (375*500))
feature.shape

#check the image shape 
print(image.shape) 
 
print(image)
# Image shape: (1480, 1490)

"""How to use Feature Extraction technique for Image Data: Features as Grayscale Pixel Value
If we use  the same example as our image which we use above in the section– the dimension of the image is 28 x 28 right? But can you guess the number of features for this image?

The number of features is  same as the number of pixels so  that the number will be 784

So now I have one more important question –

how do we declare  these 784 pixels as features of this image? Do you ever think about that?

So the solution is, you just can simply append every pixel value one after the other to generate a feature vector for the image. Let’s visualize that,


Now let’s have a look at the coloured image,"""


image = imread('https://d1m75rqqgidzqn.cloudfront.net/content/pexels-photo-1108099.jpeg')
imshow(image)


print(image.shape)
 # (375, 500, 3)


 #The image shape for this image is  375 x 500. So, the number of features will be  187500.

# now if you want to change the shape of the image that is also can be done by using the reshape function from NumPy where we specify the dimension of the image:

1
2
3
#Find the pixel features
feature = np.reshape(image, (375*500))
feature.shape
(187500,)

# 1 features


"""How to extract features from Image Data: What is the Mean pixel value in channel?
So here we will start with reading our coloured image. Here we did not us the parameter “as_gray = True’

image = imread('https://d1m75rqqgidzqn.cloudfront.net/content/pexels-photo-1108099.jpeg')
imshow(image)
feature extraction in Image processing
1
print(image.shape)
(375, 500, 3)
"""


"""For this scenario the image has a dimension (375,500,3). This three represents the RGB value as well as the number of channels. Now we will use the previous method to create the features.

The total number of features will be for this case 375*500*3 = 562500


From the past, we are all aware that, the number of features remains the same. In this case, the pixel values from all three channels of the image will be multiplied.

Now we will implement this using Python:"""


image = imread('https://d1m75rqqgidzqn.cloudfront.net/content/pexels-photo-1108099.jpeg')
feature_matrix_image = np.zeros((375,500)) 
feature_matrix_image
array([[0., 0., 0., …, 0., 0., 0.], [0., 0., 0., …, 0., 0., 0.], [0., 0., 0., …, 0., 0., 0.], …, [0., 0., 0., …, 0., 0., 0.], [0., 0., 0., …, 0., 0., 0.], [0., 0., 0., …, 0., 0., 0.]])


# 1 feature_matrix_image.shape
(375, 500)

"""In this coloured image has a 3D matrix of dimension (375*500 * 3) where 375 denotes the height, 500 stands for the width and 3 is the number of channels. 
In order to  get the average pixel values for the image, we will use a for loop:"""


for i in range(0,image.shape[0]):
 
    for j in range(0,image.shape[1]):
 
        feature_matrix_image[i][j] = ((int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2]))/3)

feature_matrix_image


"""Now we will make a new matrix that will have the same height and width but only 1 channel.

To convert the matrix into a 1D array we will use the Numpy library,"""

eature_sample = np.reshape(feature_matrix_image, (375*500)) 
 
# feature_sample




"""Project Using Feature Extraction technique
Importing an Image
To import an image we can use Python pre-defined libraries"""


import pandas as pd
 
import numpy as np
 
import matplotlib.pyplot as plt
 
%matplotlib inline
 
from skimage.io import imread, imshow
 
image = imread("/content/pexels-photo-1108099.jpeg")
 
imshow(image)


# Image feature Detection using OpenCV:


import cv2
 
import numpy as np 
 
import cv2 
 
import matplotlib.pyplot as plt 
 
# %matplotlib inline
img_load = cv2.imread("/content/toppng.com-service-dogs-tv-pg-dog-pictures-white-background-628x669.png")
img_load

from google.colab.patches import cv2_imshow
 
cv2_imshow(img_load)


img_load1 = cv2.cvtColor(img_load, cv2.COLOR_BGR2RGB)  # Convert from cv's BRG default color order to RGB
img_load1




#converting image to Gray scale 
 
gray_image = cv2.cvtColor(img_load,cv2.COLOR_BGR2GRAY)
 
#plotting the grayscale image
 
cv2_imshow(gray_image)




#converting image to Gray scale 
 
gray_image = cv2.cvtColor(img_load,cv2.COLOR_BGR2GRAY)
 
#plotting the grayscale image
 
cv2_imshow(gray_image)



ret,thresh_binary = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
 
ret,thresh_binary_inv = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY_INV)
 
ret,thresh_trunc = cv2.threshold(gray_image,127,255,cv2.THRESH_TRUNC)
 
ret,thresh_tozero = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO)
 
ret,thresh_tozero_inv = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO_INV)
#DISPLAYING THE DIFFERENT THRESHOLDING STYLES using OpenCV
 
names = ['Oiriginal Image','BINARY','THRESH_BINARY','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
 
images = gray_image,thresh_binary,thresh_binary_inv,thresh_trunc,thresh_tozero,thresh_tozero_inv
 
for i in range(6):
 
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
 
    plt.title(names[i])
 
    plt.xticks([]),plt.yticks([])


    Edge detection:


#calculate the edges using Canny edge algorithm
 
edges_of_image = cv2.Canny(img_load,100,200) 
 
#plot the edges
 
cv2_imshow(edges_of_image)