import unittest
import numpy as np
import matplotlib.pyplot as plt
    
#Class Checker
class Checker():
    
   # definition for init method or constructor
   
   def __init__(self,resolution,tile_size):
        self.resolution = resolution
        self.tile_size =  tile_size
        self.output=self.draw()
        
        
   #definition for draw method
   
   def draw(self):
    # Create the black and white squares
    zero = np.zeros((self.tile_size, self.tile_size), dtype=int)
    one = np.ones((self.tile_size, self.tile_size), dtype=int)

    # Use np.block and np.tile to create the checkerboard pattern
    pattern = np.block([[zero, one], [one, zero]])
    output = np.tile(pattern, (self.resolution // (2 * self.tile_size), self.resolution // (2 * self.tile_size)))

    return output


      #indices
       #self.output=np.indices(self.resolution).sum(axis=0) % 2
       #return self.output
   
   #definition for show method
   
   def show(self):
        
        plt.imshow(self.output, cmap=plt.cm.gray)
        plt.show()
#Class Circle
class Circle():
    
    # definition for init method or constructor

   def __init__(self,resolution,radius,position):
           self.resolution = resolution
           self.radius = radius
           self.position=position
           self.output=self.draw()
   
   #definition for draw method

   def draw(self):
    x = np.arange(self.resolution)
    y = np.arange(self.resolution)

    xx, yy = np.meshgrid(x, y)

    # Use meshgrid to create the grid of points
    X, Y = xx - self.position[0], yy - self.position[1]

    # Compute the distance from each point to the center
    distance = np.sqrt(X**2 + Y**2)

    # Check if the distance is within the specified radius
    output = distance <= self.radius
    return output 

   #definition for show method
   
   def show(self):
       # Display the Circle
       plt.figure("Circle")
       plt.imshow(self.output, cmap=plt.cm.gray, interpolation='nearest')
       plt.show()

#Class Spectrum
class Spectrum():
    
      # definition for init method or constructor
    
      def __init__(self,resolution):
           self.resolution = resolution
           self.output=self.draw()
           
    
      #definition for draw method
    
      def draw(self):  
        first_array = np.arange(0, 1, 1/self.resolution)
        second_array = np.arange(1, 0, -1/self.resolution)

        # create 2D arrays for each color channel
        bottom_right1, bottom_right2= np.meshgrid(first_array,first_array)
        bottom_right= bottom_right1*bottom_right2

        top_left1, top_left2= np.meshgrid(second_array,second_array)
        top_left = top_left1*top_left2
        
        top_right1, top_right2 = np.meshgrid(first_array, second_array)
        top_right= top_right1*top_right2

        bottom_left1, bottom_left2 = np.meshgrid(second_array, first_array)
        bottom_left= bottom_left1*bottom_left2

        bottom=bottom_right2

        rgb = np.dstack((top_right+bottom_right, bottom , top_left+bottom_left)) 
        output= rgb
        return output
      #definition for show method
    
      def show(self):
        # Display the spectrum
        plt.figure("Spectrum")
        plt.imshow(self.output)
        plt.show()