def gen(x):
    s=x
    while(s>0):
        yield s
        s=s-1

num=int(input("Enter a number :"))
res=gen(num)        
#*  with the use of For loop not to use of next() function to see the value
for val in res:
    print(val)
