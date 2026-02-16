import csv
with open("CSVFILE\\Employee.csv","r") as rp:
    csvdic=csv.DictReader(rp)
    for dictrec in csvdic:
        for k,v in dictrec.items():
            print(f"\t{k}--->{v}")
        print()    