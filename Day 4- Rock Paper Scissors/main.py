import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
games_images =(rock, paper, scissors)
userchoice = int(input("what you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))
print(games_images[userchoice])

computer_choice=random.randint(0,2)
print("computer choose: ")
print(games_images[computer_choice])

if userchoice >=3 or userchoice <0:
 print("you typed an invalid number, you lose!")
elif userchoice ==0 and computer_choice ==2:
 print("You wins")
elif userchoice==2 and computer_choice ==3:
 print("You wins")
elif userchoice==3 and computer_choice==1:
 print("You wins")
elif computer_choice ==0 and userchoice ==2:
 print("You loose")
elif computer_choice ==2 and userchoice ==3:
 print("You loose")
elif computer_choice==3 and userchoice==1:
 print("You loose")    
elif userchoice == computer_choice:
 print("its a draw")
