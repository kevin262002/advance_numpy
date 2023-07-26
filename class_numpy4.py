import numpy

arr = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]]) 

print(arr)

newarray = arr[::2, 1::2]

print(newarray)