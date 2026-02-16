import share
def disshare(d):
    print("\tsharename\tshareValue")
    for sn,sv in d.items():
        print("\t",sn,"\t",sv)

d=share.shareinfo()        
disshare(d)
