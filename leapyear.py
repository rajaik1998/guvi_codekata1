a=int(input("enter the year"))
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
            print("leap year")
else:
    print("not leap year")