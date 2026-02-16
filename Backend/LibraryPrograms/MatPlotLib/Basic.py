
#?====================================================================================================
# import matplotlib as m
# print(m.__version__)   #* Golbal varible in matplotlib

#?====================================================================================================

# import matplotlib.pyplot as plt
# plt.plot()
# plt.show()

#?====================================================================================================
# import matplotlib.pyplot as plt
# plt.plot()
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title("Student Performance Evalution")
# plt.show()


#Given Problem
#Number of Students in  Class		Heights
#			20						4.5 5.5 6.5 3.5 5.5
#									3.5 5.5 6.2 3.5 5.5
#									3.5 5.5 4.5 3.5 5.5
#									2.5,3.5,6.0,6.0,5.5
#Draw the bar Plot the above Given Data
lst=[4.5,5.5,6.5, 3.5 ,5.5,3.5 ,5.5 ,6.2,3.5,5.5,3.5,5.5, 4.5,3.5,5.5,2.5,3.5,6.0,6.0,5.5]
d={}
for val in lst:
    if val not in d:
       d[val]=1
    else:
       d[val]=d[val]+1

import pandas as pd
df=pd.DataFrame(d,index=[1])
print(df)

print("----------------------------------------------")

lst=[]
for val in df.columns:
    lst.append(val)
print(lst)    


print("----------------------------------------------")
lst1 =[]
for i in df.values:
    for j in i:
        print(j)
        


import matplotlib.pyplot as plt
plt.bar(lst,lst1)
