import numpy

arr = numpy.array([1,2,3,4,5,6,7,8], ndmin=4)

arr = arr.reshape(4,2)

print(arr)

print(" The shape of an array : ",arr.shape)

print("Number of Dimensions : ",arr.ndim)



