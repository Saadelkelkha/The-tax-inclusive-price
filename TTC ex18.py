PHT=float(input("type the price excluding tax :"))
c=str(input("type category"))
if c=="A" :
    print("TTC is",PHT+(PHT/100)*7)
elif c=="B" :
    print("TTC is",PHT+(PHT/100)*20)
else :
    print("TTC is",PHT+(PHT/100)*25)