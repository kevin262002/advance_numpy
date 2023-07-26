import numpy

arr = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (arr)

ans1 = arr[:,arr[1,:].argsort()]
print("Sorting Original array by secoond row")
print(ans1)

print("Sorting Original array by secoond column")
ans2 = arr[arr[:,1].argsort()]
print(ans2)