'''Mutability - 
       The property of whether or not data object can be modified in the same memory loaction where they are stored is called as Mutability.'''
       
 

a= [5, 10 ,20]
id(a)
a[1]=20
print (a)
a =[5 , 20 , 20]
id(a)
''' OUTPUT WILL BE 1906292064 id memory location'''
''' As memory loaction of didnot changed before and after the modification the list is mutable'''