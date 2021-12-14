

#import the math library for pi usage
import math


# define the CubicVolume class
class CubicVolume:

    def __init__(self,shape,length,width,height):
        self.shape=shape      
        self.length=length
        self.width=width
        self.height=height

		if shape == 'cube':
			self.surface_area=length * width * height


		if shape == 'sphere':
			radius=width/2
			self.surface_area=(4/3)*math.pi*(radius**3)

