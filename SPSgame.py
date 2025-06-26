#  create a game :=  Stone Paper Scissor
import random  

def check (comp, user):
    if(comp == user):
        return 0
    elif(comp == 0 and user == 2):
        return -1
    elif(comp == 1 and user == 0):
        return -1
    elif(comp == 2 and user == 1):
        return -1
    
    return 1
    
        
comp = random.randint(0, 2)
user = int(input("0 for Stone, 1 for Paper, 2 for Scissor:\n "))

score = check(comp , user)

print("You: ",user)
print("Computer: ",comp)
if(score == 0):
    print("Its draw")
elif(score == 1):
    print("You Won")
else:
    print("You Lose")




