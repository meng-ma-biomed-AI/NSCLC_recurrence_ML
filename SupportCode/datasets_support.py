import random
import SimpleITK as Sitk
import numpy as np
from keras_preprocessing.image import ImageDataGenerator

# _get_all_slices
# returns an array containing all slices of all the files in the file_list
# returned array shape => (number of all slices, slice_width, slice_height)
def _get_all_slices(filepath, file_list):
    results = []
    for filename in file_list:
        image_data = Sitk.GetArrayFromImage(Sitk.ReadImage(filepath+filename, Sitk.sitkUInt8))
        for i in range(image_data.shape[0]):
            results.append(image_data[i, :, :])
    random.shuffle(results)
    return np.array(results)


# preprocess_data
# 1. Converts all data to 0 - 1 range
# 2. Returns the data ready for our models shape=> (number of slides, slide width, slide height, 1)
def preprocess_data(path, filenames):
    selected_slices = _get_all_slices(path, filenames)
    selected_slices = selected_slices.astype("float32") / 255
    selected_slices = np.reshape(selected_slices,
                                 newshape=(selected_slices.shape[0],
                                           selected_slices.shape[1],
                                           selected_slices.shape[2],
                                           1)
                                 )
    return selected_slices


def create_image_augmentation_dir(slices, growth_factor=5):
    generator_batch_size = 32
    number_of_slices = slices.shape[0]
    slices=slices*255
    datagen = ImageDataGenerator(horizontal_flip=True, rotation_range=15)

    i = 0
    for batch in datagen.flow(slices,
                              shuffle=False,
                              seed=1,
                              batch_size=1,
                              save_to_dir="./Data/09_TrainingSet_VAE1",
                              save_format="png",
                              save_prefix="slice_"):
        batch
        i = i+1
        if i == (number_of_slices*growth_factor):
            break



## in case I upgrade my memory.
# # Data augmentation function for the training dataset
# def data_augmentation(data_array, data_augmentation_factor=10):
#     datagen = ImageDataGenerator(horizontal_flip=True, rotation_range=10)
#     results = []
#     it = datagen.flow(data_array, shuffle=True, seed=1,batch_size=1,class_mode="input")
#     for i in range(data_augmentation_factor*data_array.shape[0]):
#         results.append(it.next()[0])
#     return np.array(results)