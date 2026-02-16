 #todo -


import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35])
# print(a)
# print(a[0:4])
# print(a[4:0]) # ----> []
# print(a[3:7])
# print(-len(a)) # ----> for checking
# print(a[-12:-8])
# print(a[-4:])
# print(a[::])
# print(a[::2])
# print(a[-100::2])
# print(a[:100:2])
# print(a[-100:1000:2])
# print(a[-12:4])
# print(a[2:-3])
# print(a[4:-10])
# print(a[::])
# print(a[::1])
# print(a[::-1])
# print(a[::-2])
#^---------------------------------------------------------------------------------------------------

# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35]).reshape(3,4)
# print(a)
# print("--------------------------------------")
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)

# print(a[0:4])
# print(a[:,0:1:1])
# print(a[::,0:1])
# print(a[0:3,0:1])
# print(a[::,0:1])
# print(a[:,:1])
# print(a[:,:1:1])
# print(a[:,0:1:1])

# print(a[1:,::1])
# print(a[1:3,0:4:1])
# print(a[1:3,0:4:])
# print(a[1:,:4])
# print(a[1::,0::])
# print(a[1::,0::1])
# print(a[1::,0:])
# print(a[1::,:4:])
# print(a[-2::-1,::])

# print(a[0::2,0::2])
# print(a[0:3:2,0::2])
# print(a[0::2,:3:2])
# print(a[0::2,::2])

#todo -output: 
# [[10 30]
#  [90 25]]

#todo - Negative indexing
# print(a[-3::2])
# print(a[-3::2,-4::2])
# print(a[-3::2,-4:-1:2])
# print(a[:3:2,:4:2])
# # print(a[-3::-2])

#todo -column 
# print(a[0::2,::])
# print(a[::2,:])
# print(a[::2,0:4])
# print(a[0:2,2::])
# print(a[:2:1,2:])
# print(a[0:2,2:4:])
# print(a[:2,2:4])
# print(a[:2,2:])


#! Basic Slicing on 1-D
#* Syntax-1:   1DNdaaray[Start:Stop:Step]
a = np.array([10,20,30,40,50,60,70,80,90,15,25,35])
# print(a[0:4])
# print(a[0:-8])
# print(a[:4:1])
# print(a[:4])
# print(a[4:0]) #[]

# print(a[8:])
# print(a[-100:100])

#^----------------------------------------------------------------------------------------
#! Basic Slicing on 2-D 
#* Syntax-2:   1DNdaaray[RowStart:RowStop:RowStep,ColStrt:ColStop:ColStep]
# import numpy as np
# a =np.array([10,20,30,40,50,60,70,80,90,15,25,35]).reshape(3,4)
# print(a)
# print("------------------------------------")

#*Get the 0th column [10,50,90]
# print(a[0:3,0:1])
# print(a[0:,:1:])
# print(a[0::,:1])
# print(a[0::,:1:])
# print(a[:3,:1])
# print(a[0::1,:1:1])
# print(a[::,0:1])

#* Get 1 Row to last ROW with all Cols
# print(a[0::2,::])
# print(a[0:3:2,::1])
# print(a[:3:2,0::1])
# print(a[:3:2,0::])

#*Get 1 Row and with all cols
# print(a[0:1,0:4])
# print(a[:1,::])
# print(a[0:1:1,0:4])
# print(a[:1:1,0:4])
# print(a[:1:,:4])
# print(a[:1:1,:])
# print(a[-3::-1,-1:-5:-1])
# print(a[-3:-4:-1,-1:-5:-1])

# print(a[:3:2,:4:3])
# print(a[:3:2,:4:4])

# print(a[::2,::])

#^----------------------------------------------------------------------------------------
# import numpy as np
# a  = np.array([10,20,30,40,50,60,70,80,90,15,25,35,55,65,75,12]).reshape(4,4)
# print(a)

#*get Last Two Cols
# print(a[0:4,2:4])
# print(a[:,2:])
# print(a[::1,-2::])
# print(a[::,2::])
# print(a[:4,2:])
# print(a[::1,2::])


#* get corener elements 10 40 55 12
# print(a[0:4:3,0::3])
# print(a[::3,::3])
# print(a[::3,0:4:3])
# print(a[::3,:4:3])

#* get 50 80 90 35
# print(a[1:3:,::3])
# print(a[1:3,::3])
# print(a[1:3:1,:4:3])
# print(a[1:3:1,0::3])

#*get 20 65
# print(a[0:4:3,1:2:])
# print(a[0:4:3,1:2])
# print(a[::3,1:2])

#^----------------------------------------------------------------------------------------
#! N-D Array Slicing
#* Syntax:NDarrayobj[MatRowBeg:MatRowEnd:MatStep,RowBegin:RowEnd:RowStep, ColBegin:ColEnd:ColStep]  

# import numpy as np
# a=np.array([10,20,30,40,50,60,70,80,90,15,25,35,55,65,75,12]).reshape(2,4,2)
# print("Content of a")
# print(a)
# print("-----------------------------")


#* get 30 40 50 60
# print(a[0:1,1:3,:])
# print(a[:1,1:3,::])
# print(a[:1,1:3:1,0:2])

#*get 10 70
# print(a[0:1,0::3,0:1:1])
# print(a[:1,0:4:3,:1:])
# print(a[:1:1,::3,:1:])


#*get 10 20 90 15
# print(a[::,0:1:1,::])
# print(a[:2,0:1:1,::1])
# print(a[::,0:1,::])
# print(a[:,0:1,:])

#* get 30 40 50 60 and 25 35 55 65
# print(a[::,1:3:1,::])
# print(a[:,1:3:1,:])
# print(a[0:2:,1:3:,::1])

#^----------------------------------------------------------------------------------------
import numpy as np
a=np.array([10,20,30,40,50,60,70,80,90,15,25,35,55,65,75,12]).reshape(2,2,2,2)
print("Content of a")
print(a)
print("------------------------")

#* get 10 20 30 40 and 90 15 25 35
# print(a[0:2,0:1,:,:])
# print(a[0:2:1,0:1,0::,0::])
# print(a[0:2:1,0:1:,::,::])

#* get 10 20 50 60 and 90 15 55 65
# print(a[0:1,0:2,0:1,::])
# print(a[0:1,0:2,0:1,:])

# print(a[1:,0:2,:1,::])
    

