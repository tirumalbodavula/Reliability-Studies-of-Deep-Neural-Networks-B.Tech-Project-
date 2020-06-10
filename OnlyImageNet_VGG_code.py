import time
start = time.time()
import keras
import numpy as np
import os
from keras.applications import vgg16, inception_v3, resnet50, mobilenet

#Load the VGG model
vgg_model = vgg16.VGG16(weights='imagenet')
##print(vgg_model.summary())

############ ACTUAL CODE ################
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
import numpy as np
##%matplotlib inline

tot_images=0
correct_classified=0
wrong_classified=0


def preprocessing_image_for_VGG16(fin_path,original_class):
#filename = 'C:\\Users\\Tirumal\\Desktop\\BTP\\imagenet-o\\imagenet-o\\n03724870\\baby_0.9982553.JPEG'
    #filename = 'C:\\Users\\Tirumal\\Pictures\\IMG_20170725_211444.jpg'
    # load an image in PIL format
    filename = fin_path
    original_image = load_img(filename, target_size=(224, 224))
    # convert the PIL image (width, height) to a NumPy array (height, width, channel)
    numpy_image = img_to_array(original_image)
    # Convert the image into 4D Tensor (samples, height, width, channels) by adding an extra dimension to the axis 0.
    input_image = np.expand_dims(numpy_image, axis=0)
    #print("PIL image size = ", original_image.size)
    #print("NumPy image size = ", numpy_image.shape)
    #print("Input image size = ", input_image.shape)
    plt.imshow(np.uint8(input_image[0]))

    ############## END ACTUAl CODE ###############

    #preprocess for vgg16
    processed_image_vgg16 = vgg16.preprocess_input(input_image.copy())

    # vgg16
    predictions_vgg16 = vgg_model.predict(processed_image_vgg16)
    label_vgg16 = decode_predictions(predictions_vgg16)
    #print ("label_vgg16 = ", label_vgg16)
    for i in range(5):
        if(label_vgg16[0][i][0]==original_class):
            global correct_classified
            correct_classified+=1
            return
    global wrong_classified
    wrong_classified+=1
    return


basepath = 'C:\\Users\\Tirumal\\Desktop\\BTP\\imagenet-a\\imagenet-a'

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            #print(entry.name)
            new_path = basepath+"\\"+entry.name
            #print(new_path)
            with os.scandir(new_path) as images:
                for f in images:
                    final_path = new_path+"\\"+f.name
                    tot_images+=1
                    #print("Image = ",final_path)
                    preprocessing_image_for_VGG16(final_path,entry.name)


print(tot_images)
print(correct_classified)
print(wrong_classified)
final_time = time.time()- start
print("Total time taken = ",final_time)

"""
#preprocess for inception_v3
processed_image_inception_v3 = inception_v3.preprocess_input(input_image.copy())

# inception_v3
predictions_inception_v3 = inception_model.predict(processed_image_inception_v3)
label_inception_v3 = decode_predictions(predictions_inception_v3)
print ("label_inception_v3 = ", label_inception_v3)
"""
#############################################################################################
"""
# prepare the image for the VGG model
VGG_processed_image = vgg16.preprocess_input(image_batch.copy())
# get the predicted probabilities for each class
VGG_predictions = vgg_model.predict(VGG_processed_image)
# print predictions
# convert the probabilities to class labels
# We will get top 5 predictions which is the default
VGG_label = decode_predictions(VGG_predictions)
print(VGG_label)

######################################################################################

# prepare the image for the INCEPTION_V3 model
INCEPTION_processed_image = inception_v3.preprocess_input(image_batch.copy())
# get the predicted probabilities for each class
INCEPTION_predictions = inception_model.predict(INCEPTION_processed_image)
# print predictions
# convert the probabilities to class labels
# We will get top 5 predictions which is the default
INCEPTION_label = decode_predictions(INCEPTION_predictions)
print(INCEPTION_label)

#####################################################################################

# prepare the image for the RESNET50 model
RESNET_processed_image = resnet50.preprocess_input(image_batch.copy())
# get the predicted probabilities for each class
RESNET_predictions = resnet_model.predict(RESNET_processed_image)
# print predictions
# convert the probabilities to class labels
# We will get top 5 predictions which is the default
RESNET_label = decode_predictions(RESNET_predictions)
print(RESNET_label)

####################################################################################

# prepare the image for the MOBILENET model
MOBILENET_processed_image = mobilenet.preprocess_input(image_batch.copy())
# get the predicted probabilities for each class
MOBILENET_predictions = mobilenet_model.predict(MOBILENET_processed_image)
# print predictions
# convert the probabilities to class labels
# We will get top 5 predictions which is the default
MOBILENET_label = decode_predictions(MOBILENET_predictions)
print(MOBILENET_label)
"""