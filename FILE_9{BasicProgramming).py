'''Price = int(input("Enter the price of dounut in rs : "))
quantiy = int(input("Enter the Number of dounts: "))
amount = Price*quantiy


if amount>1000 :
    print("yay!! , you have awailed a 10% discount ")
    Discount = amount*10/100
    amount = amount-Discount
else:
    print("yay!! , you have awailed a 5% discount ")
    Discount = amount*5/100
    amount = amount-Discount

print(    "your total bill is:" , amount  )
'''

'''#customer requirement
required_capacity = 10000
max_price= 3500

#store avaliblity 
store_capacity = 20000
store_price = 3400

if store_capacity >= required_capacity and store_price<max_price:
    print("yes!, his power bank is for you")
else: 
    print("no!,this power bank is for you")'''

'''price = 105.50
qty = 36
amount = price * qty

if amount > 10000:
    print("10% discount applicable")
    discount = amount * 10 / 100
    amount -= discount
elif amount > 5000:
    print("5% discount applicable")
    discount = amount * 5 / 100
    amount -= discount
elif amount > 2000:
    print("2% discount applicable")
    discount = amount * 2 / 100
    amount -= discount
elif amount > 1000:
    print("1% discount applicable")
    discount = amount * 1 / 100
    amount -= discount
else:
    print("No discount applicable")

print("Amount payable:", amount)
'''

YEAR= int(input("Enter the year   "  ))
if(YEAR % 4 == 0  and YEAR % 100 != 0 or YEAR % 400 ==0):
    print("the year is leap year")
else:
    print("year is not leap year")
    
    