# import array
# new_object=array.array('i',[1,2,3,4,5,6,7])
# print(new_object.itemsize)
# print(new_object.typecode)
# new_object.append(8);
# print(new_object)

# print(new_object.insert(2,12));  
# #for append the value:
# print();
# new_object.append(9)
# print(new_object)


# #todo using extend method
# y=[1,2,3,4];
# new_object.extend(y)
# print(new_object)

# #?REMOVE ELEMENT FROM ARRAY
# new_object=array.array('i',[1,2,3,4,5,6,7])
# new_object.remove(3)
# print(new_object)
# #*using reverese method
# new_object=array.array('i',[1,2,3,4,5,6,7])
# new_object.reverse()
# print(new_object)

# #NOTE: using pop method
# new_object=array.array('i',[1,2,3,4,5,6,7])
# print(new_object.pop())
# print(new_object)

# #FIXME: using index method
# new_object.sort() 
# #! sort method can not be used on array 
# new_object=array.array('i',[1,2,8,4,5,6,7])
# print(new_object)

# # todo  using numerical python numpy library

# new_object=np.array([1,2,3,4,5,6,7])
# print(new_object)
# print(np.__version__)
# print(pd.__version__)

# int_array=np.array([1,2,3,4,5,6,7])
# print(int_array.dtype) #todo it give the data type 
# print(int_array.ndim) #! it give the dimension
# print(int_array.shape) #* it give the shape of the array in form column and row form
# print(int_array.size)  #? it give the size of the array
# myntarr=np.array([1,2,3,4,5,6,7],int)

# myfloatarr=np.array([1,2,3,4,5,6,7],float)

# mycomplexarr=np.array([1,2,3,4,5,6,7],complex)
# # ! creating a filter arrays
# a1=np.empty((3,4))
# a2=np.zeros((3,4))
# a3=np.ones((3,4))
# a4=np.full((3,4),5)
import numpy as np
import pandas as pd
print(np.__version__)
# a1=np.random.random((3,4))
# a2=np.arange(5)
# a3=np.arange(0,20,5)
# a4=np.linspace(0,10,5)

# print(a1)
# print(a2)
# print(a3)
# print(a4)


a1=np.eye(3);
a2=np.identity(3)
print(a1)
print(a2)