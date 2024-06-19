str1= "Welcome To Calculator"
print(str1.center(50).upper())
A= int(input("Enter The First Number  "))
B= int(input("Enter The Second Number  "))
Operation= input("Enter Your operation")

if Operation=="+":
    print('The sum is', A+B)
elif Operation=="-":
    print("the subtraction is", A-B)
elif Operation=="*":
    print("The Multiplication is", A*B)
elif Operation=="/":
    print("The Division is", A/B)
elif Operation=="**":
    print("The Power is", A**B)
elif Operation=="//":
    print("The floor division is", A //B )
elif Operation=="%":
    print("The Modulus is", A%B)
else:
    print("INVALID OPERATOR")

