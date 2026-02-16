def kvrrange(start,stop,step):
    while(start<=stop):
        yield start 
        start=start+step



res=kvrrange(10,100,20)
for val in res:
    print(val)









