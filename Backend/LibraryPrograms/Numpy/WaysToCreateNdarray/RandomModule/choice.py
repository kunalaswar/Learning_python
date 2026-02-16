 #todo -
import numpy as np
import numpy.random as r
# a = np.array([10,20,30,40,50,60,70])
# print(a,type(a))

# cv = r.choice(a)
# print(cv,type(cv))


# a= np.array(list("python"))
# print(a,type(a))
# cv = r.choice(a)
# print(cv,type(cv))

# a = r.choice(np.array(list("12345ABCDEFabcdef")))
# print(a,type(a))

# a = np.array([10,20,30,40,50,60])
# cv =r.choice(np.array([10,20,30,40,50,60,70,80,90]),size=3)
# print(cv,type(cv))

# cv= r.choice(np.array(list("123456789abcdefghijklmnopqrstuvwxyz")),size=4)
# print(cv,type(cv))

# cv= r.choice(np.array(list("123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")),size=5)
# print(cv,type(cv))
# z = "".join(cv)
# print(z)

# cp =""
# for v in cv:
#     cp = cp+v
# print("Capptcha =",cp)

# cp = []
# for v in cv:
#     cp.append(v)
# print("captcha = ","".join(cp))    

# a = np.array([10,20,30,40,50,60,70,12,23,43,5,6,67,78,90,13,14,15,])
# cv = r.choice(a,size=(2,2))
# print(cv,type(cv))

# a = np.array([10,20,30,40,50,60,70,12,23,43,5,6,67,78,90,13,14,15,])
# cv = r.choice(a,size=(2,2))
# print(cv,type(cv))

#todo -question write program 2x2 random matrix between the value 10 to 99

#todo- 1
# a = np.arange(10,100)
# # print(a,type(a))
# cv = r.choice(a,size=(2,2))
# print(cv,type(cv))
# print(cv.ndim)
# print(cv.dtype)
# print(cv.shape)
# print(cv.size)

#todo- 2
# a = r.randint(10,100,size=(2,2))
# print(a,type(a))

#todo -3
# a= r.randint(10,100,size=20)
# mat = r.choice(a,size=(2,2))
# print(mat)

# a = r.randint(10,100,size=1)
# b = r.choice(a,size=(2,2))    
# print(b)

# [[61 61]
#  [61 61]]

# a = r.randint(10,100,size=5)
# print(a)
# b = r.choice(a,size=(3,4))
# print(b,type(b))

#todo - i wnat random matrices with 2x4 random matrix between the values 10 to 99
# a = r.randint(10,100,size=20)
# # print(a,type(a))
# b = r.choice(a,size=(2,2,4))
# print(b,type(b))
# print("Dimension =",b.ndim)

# print(list("python")) #?

#todo - generated RTA number plating value #TS08FL1234
# sa =np.array(["TS","AP","MH","KA","TN"])
# tc =np.array(["08","09","39","40","07"])
# lst=np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
# nums=np.array(list("0123456789"))
# for val in range(5):
        
#     a= r.choice(sa,size=1)
#     a1="".join(a)
#     b = r.choice(tc,size=1)
#     a2="".join(b)
#     c = r.choice(lst,size=2)
#     a3 ="".join(c)
#     d = r.choice(nums,size=4)
#     a4="".join(d)

#     e = a1+a2+a3+a4
#     print(e)
