#Currency Denomination Calculator

n= int(input("Enter the amount: "))
denominations=[2000,500,200,100,50,20,10,5,2,1]
for denom in denominations:
    count = n // denom
    if count > 0:
        print(f"{count} x {denom}")
        n = n % denom

