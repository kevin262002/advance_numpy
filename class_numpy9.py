import numpy

arr = numpy.array([[34,43,73], [82,22,12], [53,94,66]])

print(arr)

arr = numpy.delete(arr, 1, axis = 1)
print("Array after deleting column 2 on axis 1")
print(arr)

arr1 = numpy.array([10 ,10 ,10])

arr = numpy.insert(arr, 1, arr1, axis = 1)
print("Array after inserting column 2 on axis 1")
print(arr)