import numpy

arr = numpy.array([[34,43,73], [82,22,12], [53,94,66]])

print(arr)

ans1 = numpy.amin(arr,1)
print("Printing amin Of Axis 1")
print(ans1)

ans2 = numpy.amax(arr,0)
print("Printing amax Of Axis 0")
print(ans2)