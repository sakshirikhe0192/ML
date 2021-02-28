import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16# to extract the feature of a given image.VGG takes in a 224x224 pixel RGB image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
from sklearn.cluster import KMeans
import os, shutil, glob, os.path
from PIL import Image as pil_image#python image library
import scipy.cluster.hierarchy as hcluster
image.LOAD_TRUNCATED_IMAGES = True
from sklearn.cluster import DBSCAN
import pylab as pl
import matplotlib.pyplot as plt
model = VGG16(weights='imagenet', include_top=False)#imagenet-It contains more than 14 million images which belong to more than 20,000 classes
                                                   #include_top-whether to include the 3 fully-connected layers at the top of the network.
#import imagehash

imdir =r'C:/Users/Dell/Desktop/testimg'
targetdir =r'C:/Users/Dell/Desktop/result/'
#number_clusters = 5
sumarray = []
# Loop over files and get features
filelist = glob.glob(os.path.join(imdir, '*.jpg'))#the glob module is used to retrieve files/pathnames matching a specified pattern

filelist.sort()
featurelist = []
sse=[]
for i, imagepath in enumerate(filelist):
    print("    Status: %s / %s" %(i+1, len(filelist)))
    img = image.load_img(imagepath, target_size=(224, 224))
    img_data = image.img_to_array(img)#it would ensure that the returned array is a 3D array
    #print(img_data)
    img_data = np.expand_dims(img_data, axis=0)#(1, 224, 224, 3)
    img_data = preprocess_input(img_data)#preprocess_input function is meant to adequate your image to the format the model requires
    #print(img_data)
    features = model.predict(img_data)#VGG16
    #print(features)
    #print(features.shape)#(1, 224, 224, 3)
    #features = imagehash.dhash(img)
    sumarray.append(sum(features.flatten()))
    featurelist.append(features.flatten())#list of 1D array
    #print(featurelist)

for i in range(3,7):
    kmeans = KMeans(n_clusters=i, random_state=0).fit(np.array(featurelist))
    sse.append(kmeans.inertia_)
    plt.scatter(sumarray,kmeans.labels_)
    plt.xlabel('Featurelist')
    plt.ylabel('labels')
    plt.show()
    
#thresh = 1.5
#clusters = hcluster.fclusterdata(np.array(featurelist), thresh, criterion="distance")
#print(clusters)
#clustering = DBSCAN(eps=3,min_samples=2,leaf_size=100).fit(np.array(featurelist))
#print(clustering.labels_)

#elbow graph
plt.figure(figsize=(6,6))
plt.plot(range(3,7),sse)
plt.xlabel("Number of clusters")
plt.ylabel("sum of squared error")
try:
    os.makedirs(targetdir)
except OSError:
   pass
#Copy images renamed by cluster
print("\n")
print(kmeans.labels_)
for i, m in enumerate(kmeans.labels_):
    print(i,m)
    print("Copy: %s / %s" %(i+1, len(kmeans.labels_)))
    shutil.copy(filelist[i], targetdir + "cluster"+ str(m) + "_" + str(i) + ".jpg")
    



