import numpy

arr = numpy.arange(10,34,1)
arr=arr.reshape(8,3)

print(arr)

ans = numpy.split(arr,4)

print(ans)