import os.path
import json
import scipy.misc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import random

# In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding Labels.
class ImageGenerator:
    def __init__(self, file_path, Label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        # Define all members of your generator class object as global members here.
        # These need to include:
        # the batch size
        # the image size
        # flags for different augmentations and whether the data should be shuffled for each epoch
        # Also depending on the size of your data-set you can consider loading all images into memory here already.
        # The Labels are stored in json format and can be directly loaded as dictionary.
        # Note that the file names correspond to the dicts of the Label dictionary.

        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        #TODO: implement constructor
        # init variables
        self.file_path = file_path
        self.Label_path = Label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        
        self.epoch = -1
        self.current_iteration = 0
        self.end_epoch = False
        
        # read image Name and Label
        self.Image_name = np.array(os.listdir(self.file_path))
        self.Label = self.read_json(self.Label_path)
        assert len(self.Image_name) == len(self.Label.keys())

        self.total_instances = len(self.Label)
        #In case last iteration does not contain full batch size
        self.total_iterations = int(math.ceil(self.total_instances / self.batch_size))
        self.shuffle_images()
    
    def shuffle_images(self):
        if (self.shuffle):
            np.random.shuffle(self.Image_name)

    def read_json(self, path):
        with open(path, "r") as openfile:
            Label = json.load(openfile)
        return Label    
    
    
    def get_batch_indices(self):
        #Returns current batch indices
        start = self.current_iteration * self.batch_size
        stop = start + self.batch_size
        indices = np.arange(start, stop)
        return indices
    
    def read_batch_data(self, indices):
        #Reads images and labels of given indices, also performs augmentation
        images = []
        labels = []
        for idx in indices:
            image_path = os.path.join(self.file_path, self.Image_name[idx])
            img = np.load(image_path)
            img = Image.fromarray(img)
            img = img.resize(self.image_size[:2])
            label = self.Label[self.Image_name[idx].split(".")[0]]
            img = self.augment(img)
            images.append(img)
            labels.append(label)

        return np.array(images), np.array(labels)
    
    def next(self):
        # This function creates a batch of images and corresponding Labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        #TODO: implement next method
        if (self.current_iteration == 0):
            self.shuffle_images()
            self.epoch += 1

        indices = self.get_batch_indices()
        self.current_iteration += 1
        if (self.current_iteration == self.total_iterations):
            # indices greater than the last will start from 0
            indices = indices % self.total_instances
            self.current_iteration = 0

        images, labels = self.read_batch_data(indices)
        
        return images, labels

    def augment(self,img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function
        if (self.rotation):
            choices = [0, 90, 180, 270]
            angle = random.choice(choices)
            img = img.rotate(angle)

        if (self.mirroring):
            ax = random.choice([0, 1]) # randomly decide from these axes
            img = np.flip(img, axis = ax)
        
        img = np.array(img)
        

        return img

    def current_epoch(self):
        # return the current epoch number
        return self.epoch

    def class_name(self, x):
        # This function returns the class name for a specific input
        #TODO: implement class name function
        return self.class_dict[x]
   
    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and Labels and visualizes it.
        #TODO: implement show method
        n_rows, n_cols = 4, self.batch_size

        fig, rows = plt.subplots(n_rows, n_cols, figsize = self.image_size[:2])
        for i in range(n_rows):
            images, labels = self.next()
            k = 0
            for img, label in zip(images, labels):
                rows[i][k].imshow(img)
                rows[i][k].axis("off")
                rows[i][k].set_title(self.class_name(label))
                k+=1
            
        plt.show()

if __name__=="__main__":

    file_path = "./exercise_data/"
    label_path = "./Labels.json"
    batch_size = 4
    image_size = (32,32,3)
    img_generator = ImageGenerator(file_path, label_path, batch_size, image_size, 
                                rotation=True, mirroring=True, shuffle=True)
    
    res = img_generator.next()
    img_generator.show()