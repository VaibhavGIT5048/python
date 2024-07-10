#using globals ()

""" alpha=1
beta=2
gamma=3

print(globals())
globals()['gamma']=5

 """
"""  
age=9
def a():
    print("global varibale age :" , globals()['age'])
    
    #Now Modifiying the global variable age inside the function.
    globals()['age']=89
    print("Global age modified age",globals()['age'])
    
    #now creating a LOCAL varibale , age inside the function.
    age=11
    print("The local Age: ", age)
    return
a()
print("Checking the global variable Outside the function: ",age) """



'''def myfunction(newlist):
   print("List accessed in function: ", "id:", id(newlist))
   return

mylist=[10,20,30,40,50]
print("List before passing to function: ", "id:", id(mylist))
myfunction(mylist) '''

""" def checkmoney(num):
    if   num<7000:
        print("Ahem, can you rethink this number please?")
    elif num>10000:
        print("Wow sis! You are a queen")
    elif num in range(7000,10000):
        print("Cool, thanks sis! {} rupees will certainly help.".format(num))

    return

sis=8500
checkmoney(sis)

 """
 

