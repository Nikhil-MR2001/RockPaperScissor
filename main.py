import random


computer = random.randint(1,3)
list = ['1-Rock', '2-paper',  '3-Scissor']
print('Choose from this - \n', list)
choices = int(input())


def valuation():
    if computer == 1 and choices == 1:
        print("Tied")
    elif computer == 2 and choices ==1:
        print("you lose")
    elif computer == 3 and choices ==2:
        print("you lose")
    elif computer == 1 and choices ==3:
        print("you lose")
    else:
        print("congrats...!!!!    You won")

valuation()
    
