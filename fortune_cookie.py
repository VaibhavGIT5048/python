import random

lucky_number= random.randint(1,100)

fortune_number = random.randint(1,3)
fortune_text = ''

if fortune_number == 1:
    fortune_text = 'You will have a great day today'
elif fortune_number == 2:
    fortune_text = 'You will have some good news today'
elif fortune_number == 3:
    fortune_text = 'You will have a bad day today'
    
    
    
print(f" {fortune_text} , your lucky no is: {lucky_number}")