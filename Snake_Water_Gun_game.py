# snake beat water. water beat gun. gun beat snake according to my Logic

import random

def game(comp,you):

    if (comp ==  you ):
        return None
    elif(comp == 's'):
        if (you == 'w'):
            return False
        elif (you == 'g'):
            return True
        
    elif(comp == 'w'):
        if (you == 's'):
            return True
        elif (you == 'g'):
            return False
    
    elif(comp == 'g'):
        if (you == 'w'):
            return True
        elif (you == 's'):
            return False

rand = random.randint(1,3)
if (rand==1):
    comp = 's'
elif (rand==2):
    comp = 'w'
elif (rand==3):
    comp = 'g'

print(" Snake(s), Water (w), Gun (g)")
you = (input("Enter Snake (s), Water (w), Gun (g) : "))

a = game(comp, you)

if (a==None):
    print("Draw")
elif a :
    print("Congratulations you win ")
else:
    print("you Loose")
print(f"\nComputer choose {comp}")
print(f"You choose {you}") 



# snake beat water. water beat gun. gun beat snake according to harry bhai's logic
'''
import random 
score =0
print("Get ready to play 'Snake,water and gun' with computer,and enter your choice ,if you win your score will increase \n  ")
try:
  n=int(input("Enter the number of levels you wanna play : ")) 
  for i in range(1,n+1):
    l=["snake","water","gun"]
    num=random.randint(0,2)
  
    x=str(input("Choose snake , water or gun : "))
    x=x.lower()
    if x not in l: raise ValueError
    print("Computers choice is",l[num])
    if l[num]==x :
      print(f"level {i} draw")
      print("\n")

    elif (l[num] == l[0] and x==l[1]):
      print(f"You lost level{i}")
      print ("\n")

    elif (l[num] == l[0] and x==l[2]):
      print(f"You won level{i}")
      score=score+1
      print ("your score is :",score)
      print ("\n")
    
    elif (l[num] == l[1] and x==l[0]):
      print(f"You won level{i}")
      score=score+1
      print ("your score is :",score)
      print ("\n")
    
    elif (l[num] == l[1] and x==l[2]):
      print(f"You lost level{i}")
      print ("\n")
    
    elif (l[num] == l[2] and x==l[0]):
      print(f"You lost level{i}")
      print ("\n")
     
    elif (l[num] == l[2] and x==l[1]):
      print(f"You won level{i}")
      score=score+1
      print ("your score is :",score)
      print ("\n")
    
  print("Your final score is ",score)
  print("thanks for playing ")

except:
  print("please enter valid input")
  
 '''