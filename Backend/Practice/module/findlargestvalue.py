def findlargeststringvalue(value):
    d={}
    for val in value:
        if val not in d:
            d[val]=1
        else:
            d[val]=d[val]+1    
    else:
        print(d)       
        mv=max(d.values()) 
        for k in d.values():
            if k==mv:
                print("largest value :",k)

# findlargeststringvalue("bbbbbaaaa")