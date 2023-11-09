import numpy as np
import matplotlib.pyplot as plt

class checker:
    def __init__(self,resolution,tile_size):
        self.resolution=resolution
        self.tile_size=tile_size           
    def draw(self):
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
class circle:
    def __init__(self):
        pass
    def draw():
        pass
    def show():
        pass
