bname="ICICI"
addr="HYD"
def simpleint():
    p=float(input("Enter principle amount :"))
    t=float(input("Enter a time :"))
    r=float(input("Enter a rate :"))
    si=(p*t*r)/100
    totamt=p+si
    print("Simple interest calculations :")

    print("simple interest :",si)
    print("Total amount to pay :",totamt)


