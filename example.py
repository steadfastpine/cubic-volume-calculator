# This example demonstrates usage of the cubic volume calculator.
# Format: CubicVolume(shape,length,width,height)

# Import the surfacearea.py file
from cubicvolume import *


# Create an object with a value equal to the cubic volume of a cube
test1 = CubicVolume('cube',50,50,100)


# Print the cube cubic volume
print(test1.surface_area)


# Create an object with a value equal to the cubic volume of a sphere
test2 = CubicVolume('sphere',100,100,100)


# Print the sphere cubic volume
print(test2.surface_area)
