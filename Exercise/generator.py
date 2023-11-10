import os.path
import json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import random

class ImageGenerator:
    def __init__(self, file_path, Label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
       
        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        #TODO: implement constructor
        # init variables
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.image_size = image_size
        self.file_path = file_path
        self.Label_path = Label_path
        
        self.epoch = -1
        self.end_epoch = False
        self.current_iteration = 0

        self.Image_name = np.array(os.listdir(self.file_path))
        self.Label = self.read_json(self.Label_path)
        assert len(self.Image_name) == len(self.Label.keys())

        self.total_instances = len(self.Label)

        self.total_iterations = int(math.ceil(self.total_instances / self.batch_size))
        self.shuffle_images()
        
    def get_batch_indices(self):

        start = self.current_iteration * self.batch_size
        stop = start + self.batch_size
        indices = np.arange(start, stop)
        return indices
    
    def read_json(self, path):
        with open(path, "r") as file:
            Label = json.load(file)
        return Label    
    

    def read_batch_data(self, indices):
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
    
    def shuffle_images(self):
        if (self.shuffle):
            np.random.shuffle(self.Image_name)
            
    def next(self):
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

        if (self.mirroring):
            ax = random.choice([0, 1]) # randomly decide from these axes
            img = np.flip(img, axis = ax)
        
        if (self.rotation):
            choices = [0, 90, 180, 270]
            angle = random.choice(choices)
            img = img.rotate(angle)
        img = np.array(img)
        

        return img

    def current_epoch(self):
        return self.epoch

    def class_name(self, x):
        return self.class_dict[x]
   
    def show(self):
        n_rows, n_cols = 4, self.batch_size

        _, rows = plt.subplots(n_rows, n_cols, figsize = self.image_size[:2])
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