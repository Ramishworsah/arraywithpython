import array
new_object=array.array('i',[1,2,3,4,5,6,7])
# print(new_object.itemsize)
# print(new_object.typecode)
# new_object.append(8);
# print(new_object)

# print(new_object.insert(2,12));  
# for append the value:
# print();
# new_object.append(9)
# print(new_object)


#todo using extend method
# y=[1,2,3,4];
# new_object.extend(y)
# print(new_object)

#?REMOVE ELEMENT FROM ARRAY
# new_object=array.array('i',[1,2,3,4,5,6,7])
# new_object.remove(3)
# print(new_object)
#*using reverese method
# new_object=array.array('i',[1,2,3,4,5,6,7])
# new_object.reverse()
# print(new_object)

# NOTE: using pop method
# new_object=array.array('i',[1,2,3,4,5,6,7])
# print(new_object.pop())
# print(new_object)

# FIXME: using index method
# new_object.sort() 
#! sort method can not be used on array 
# new_object=array.array('i',[1,2,8,4,5,6,7])
# print(new_object)

# todo  using numerical python numpy library
import numpy as np
import pandas as pd
new_object=np.array([1,2,3,4,5,6,7])
print(new_object)
print(np.__version__)
print(pd.__version__)

inrohan