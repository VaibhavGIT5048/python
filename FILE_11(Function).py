'''def SayHello(name):
    """This function will display a greeting message."""
    print(" {}!! Welcome to Internshala".format(name))
    return
#SayHello("Vaibhav")

you=input("Enter yout name")
SayHello(you)
Friend=input("Enter ypur friends name")
SayHello(Friend)'''

#CODE PRACTICE

'''It's your chance to transform yourself into Harry Potter! Define a function called IPotter which will replace the name Harry with your name in the following string:
Looking Slughorn straight in the eye, Harry leant forwards a little.
'I am the Chosen One. I have to kill Voldemort. I need that memory.'
'You are the Chosen One?'
'Of course I am,' said Harry calmly.'''

'''def IPotter():
    "This function morphs anyone into Harry Potter!"
    name="VAIBHAV"
    print("""Looking Slughorn straight in the eye, {}leant forwards a little.\n
'I am the Chosen One. I have to kill Voldemort. I need that memory.'\n
'You are the Chosen One?'\n
'Of course I am,' said {} calmly""".format(name,name))
    return
IPotter() '''


#Do I have enough money to splurge on the latest smartphone 


""" Str= "Welcome to our store"
print(Str.upper().center(50))
input("Which Phone would You Like To purchase ")
def Check_Budget(total_Buget):
    if total_Buget>150000:
        print("You can buy the phone requested")
    elif 10000<=total_Buget<=150000:
        print("you can see the other option")
        print("you can buy the samsung or other phones")
    else:
     print("sorry sir!! You don't have enough money")
        
   
        
Total_Buget=int(input("Enter The Buget: "))
Check_Budget(Total_Buget) """

""" def variable(m1,m2,m3,m4=15000):
    total=m1+m2+m3
    if total>m4:
        print("You Have enough money To buy This phone")
    else:
        print("You Don't Have Funds")
        return
gift_money = int(input("Enter amt of money recieved as gift: rs"))
saving = int(input("Enter amt of moneyy you saved: rs"))
money_earned= int(input("Enter amount of money earned via internship: rs"))
variable(gift_money,saving,money_earned,10000) # pre-excuited
 """

#Function with arguments
#calcultion of the total contribution by the friends

def food(f):
    tip=0.1*f            # to remove tip delete line 68-69
    f=f+tip
    fperson=f/num
    return fperson

def movie(m):
    return m/num
num=int(input("Enter The Number Of Friends: "))
ftotal=int(input("Spent On Food:"))
mtotal=int(input("Enter Total Spent On Movie: "))

x=food(ftotal)
y=movie(mtotal)
print("The Per person Cost Is: ", x+y)