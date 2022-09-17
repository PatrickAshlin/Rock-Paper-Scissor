from cgi import print_form
from lib2to3.pgen2.token import EQUAL
import random
from traceback import print_tb
from unittest import result


draw=0
print("Winning rules of the rock paper scissor game as follows:\n"
+"rock vs paper->paper wins\n"+"rock vs scissor ->rock wins\n"+"paper vs scissor ->  scissor wins \n")

while True:
 print("Enter the choice \n 1 for rock,\n 2 for paper , \n 3 for scissor\n ")
 choice = int(input("user turn; ")) 
 while choice > 3 or choice < 1 :
    choice = int(input(" Enter valid input"))
 if choice == 1:
    choice_name = 'Rock'
 elif choice == 2:
    choice_name = 'Paper'        
 else:
    choice_name = 'scissor'
 print("user choice is :"+ choice_name)
 print("\n Now it  is computer turn...")


 comp_choice = random.randint(1,4)
 while comp_choice == choice:
  comp_choice = random.randint(1,4)

 if comp_choice == 1:
    comp_choice_name = 'Rock'
 if comp_choice == 2:
    comp_choice_name == 'Paper'
 elif comp_choice == 3:
    comp_choice_name = 'Scissor'


 print("Computer choice is: " + comp_choice_name)    
 print(choice_name+" V/S "+ comp_choice_name)

 if choice == comp_choice:
    print(" draw=>",end ="")
    result = draw


    if((choice == 1 and comp_choice ==2)or
     (choice == 2 and comp_choice == 1)):
       print("paper wins =>",end ="")
    result= "paper"
      

 elif ((choice == 1 and comp_choice ==3)or
     (choice == 3 and comp_choice ==1)):
    print("Rock wins=>", end ="")
    print("<== User wins ==>")   
    result = "Rock"
      
 else:
    print("Scissoir Wins =>",end ="")   
    result = "Scissor"
    if result == "Draw" :
     print("<== Its a tiee ==>")
    if result   == choice :
     print("<== User wins ==>")
    else: 
     print("<== computer Wins ==>")  
     print(" Do u want to play again  (Y/N)")
    ans = input().lower
    if ans == 'n':       
      break
    print("\n Thanks for playing my game ")