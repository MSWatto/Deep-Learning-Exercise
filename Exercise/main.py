from pattern import Checker, Circle, Spectrum
from generator import ImageGenerator

checker=Checker(8,2)
circle = Circle(55, 15, (30, 15))
spectrum = Spectrum(100)


checker.show() 
circle.show() 
spectrum.show()
   
file_path = "./exercise_data"
label_path = "./Labels.json"
batch_size = 3
image_size = (32,32,2)

imgGen = ImageGenerator(file_path, label_path, batch_size, image_size)
imgGen.show()
