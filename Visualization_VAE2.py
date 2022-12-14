import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

# load models
from SupportCode.datasets_support import preprocess_data
from SupportCode.Paths import CroppedWindow

encoder_1 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_encoder_1.h5', compile=False)
encoder_2 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_encoder_2.h5', compile=False)
encoder_3 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_encoder_3.h5', compile=False)
encoder_4 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_encoder_4.h5', compile=False)
encoder_5 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_encoder_5.h5', compile=False)
encoders = [encoder_1, encoder_2, encoder_3, encoder_4, encoder_5]

decoder_1 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_decoder_1.h5', compile=False)
decoder_2 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_decoder_2.h5', compile=False)
decoder_3 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_decoder_3.h5', compile=False)
decoder_4 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_decoder_4.h5', compile=False)
decoder_5 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_decoder_5.h5', compile=False)

vae_1 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_1.h5', compile=False)
vae_2 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_2.h5', compile=False)
vae_3 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_3.h5', compile=False)
vae_4 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_4.h5', compile=False)
vae_5 = tf.keras.models.load_model('./Output/VAE_2/Models/VAE_5.h5', compile=False)
VAEs = [vae_1, vae_2, vae_3, vae_4, vae_5]
# load names of test datasets for each model

test_dataset_1 = np.load("./Output/VAE_2/DatasetSplits/test_dataset_fold_1.npy")
test_dataset_2 = np.load("./Output/VAE_2/DatasetSplits/test_dataset_fold_2.npy")
test_dataset_3 = np.load("./Output/VAE_2/DatasetSplits/test_dataset_fold_3.npy")
test_dataset_4 = np.load("./Output/VAE_2/DatasetSplits/test_dataset_fold_4.npy")
test_dataset_5 = np.load("./Output/VAE_2/DatasetSplits/test_dataset_fold_5.npy")
test_datasets = [test_dataset_1, test_dataset_2, test_dataset_3, test_dataset_4, test_dataset_5]


for i in range(5):
    data = preprocess_data(CroppedWindow, test_datasets[i])
    image_counter = 0
    # iterate data and get features
    for item in data:
        temp = np.reshape(item, newshape=(1, item.shape[0], item.shape[1], 1))
        result = VAEs[i](temp)
        input_image = np.reshape(item, newshape=(item.shape[0], item.shape[1]))
        input_image = input_image * 255
        plt.imsave("./Output/VAE_2/Images/" + str(i) + "/" + str(image_counter) + 'a.jpeg', input_image)
        output_image = np.reshape(result[0], newshape=(result[0].shape[0], result[0].shape[1]))
        output_image = output_image * 255
        plt.imsave("./Output/VAE_2/Images/" + str(i) + "/" + str(image_counter) + 'b.jpeg', output_image)
        image_counter = image_counter + 1

print("Visualization finished!")