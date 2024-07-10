'''num = int(input("Enter the number"))
d=2
while num>1:
    if num%d==0:
        print (d)
        num=num/d
        continue
    d=d+1'''
    
'''i=0
while i<4:
    print(i)
    i=i+1
    if i==2:
        break
else:
    print(0)'''


#The variable X takes the value from zero to 10 and prints one value at a time
# however when X is even X is assigned the next value in the range without executing the subsequent print statement 
# so the odd number in the range are printed

'''for x in range(11):
    if x%2==0:
        print(x)'''

#And for odd we can use continue 
for num in range(1, 21):
    if num % 2 == 0:
        continue 
    print(num)
