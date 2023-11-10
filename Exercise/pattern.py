import numpy as np
import matplotlib.pyplot as plt

class checker:
    def __init__(self,resolution,tile_size):
        self.resolution=resolution
        self.tile_size=tile_size           
    def draw(self):
        #This is for making the array zero
        black=np.zeros((self.resolution,self.resolution), dtype=np.uint8)
        y=np.ones((self.tile_size,self.tile_size), dtype=np.uint8)
        black[0:self.tile_size,0:self.tile_size]=y
        black[self.tile_size:self.tile_size*2,self.tile_size:self.tile_size*2]=y
        array=black[0:self.tile_size*2,0:self.tile_size*2]
        return array         
    def show(self):
        square=self.draw()
        board=np.tile(square,(4,4))
        plt.xticks([])
        plt.yticks([])
        plt.imshow(board, cmap='gray')
        plt.show()
class Circle:
    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position

    def draw(self):
        x, y = np.meshgrid(np.arange(self.resolution), np.arange(self.resolution))
        #print(x)
        #print(y)
        distance = np.sqrt((x - self.position[0]) ** 2 + (y - self.position[1]) ** 2) #main logic of circle
        #print(distance)
        output = (distance <= self.radius).astype(np.uint8)
        #print(output)
        return output

    def show(self):
        output = self.draw()
        plt.imshow(output, cmap='gray')
        plt.xticks([])
        plt.yticks([])
        plt.show()
