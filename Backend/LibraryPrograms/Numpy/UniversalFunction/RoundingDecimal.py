
#!trunc()
#^===================================================================================================
#* rounding decimal 
import numpy as np

# arr = np.array([-3.1666,3.6667])
# print(arr)
# print(np.trunc(arr))


# import numpy as np
# arr = np.trunc([-3.1666,3.6667])
# print(arr)

#^===================================================================================================
# import numpy as np
# arr = np.array([-3.1666,3.6667])
# # print(arr)
# print("value after rounding decimal ")
# a = np.trunc(arr)
# print(a,type(a))

#^===================================================================================================

# import numpy as np
# arr = np.trunc([0.4455])
# print(arr)

#^===================================================================================================
#! fix() 
#* 
# arr = np.fix([-3.1666,3.6667])
# print(arr,type(arr))


#^===================================================================================================
# import numpy as np
# arr = np.fix([0.4455])
# print(arr)

#^===================================================================================================
#! around() 
#* Round of 3.1666 to 2 decimal places:
# import numpy as np
#! arr = np.round(3.1666,2) #* both are same Answer
# arr1 = np.around(3.1666,2)
# print(arr)
# print(arr1)

#^===================================================================================================
# arr = np.around(3.166545, 2)
# print(arr)

#^===================================================================================================
# arr = np.around(3.164445, 2)
# print(arr)
# arr = np.around(3.164445,3)
# print(arr)

#^===================================================================================================

#!  floor()
#* floor the element of following array 
# import numpy as np
# arr = np.floor([-3.1666, 3.6667]) #* floor() is decrease /down the value 
# print(arr)

# import numpy as np
# arr = np.floor([5.9911,-3.999]) #* down the vlaue 
# print(arr)
#^===================================================================================================

#!ceil()
# import numpy as np
# arr = np.ceil([-3.1666,3.6667])
# print(arr)

# import numpy as np
# arr = np.ceil([-3,4.2])
# print(arr)

# import numpy as np
# arr = np.ceil([-3.99,4.0])
# print(arr)

# import numpy as np
# arr = np.ceil([-3.99,4.01])
# print(arr)

#^===================================================================================================
# import numpy as np
# arr = np.ceil([-1.111,1.1111])
# print(arr)


# import numpy as np
# print(np.trunc([-1.222222,4.0111111111]))
# print(np.fix([-1.122222,4.0111111]))
# print(np.floor([-1.122222,4.0111111111])) #![-2.  4.] value is go to down or decrease
# print(np.ceil([-1.122222,4.0111111111111])) #![-1.  5.] value is go to up or increase






