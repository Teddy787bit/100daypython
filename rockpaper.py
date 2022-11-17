import random
dice = ['rock', 'paper', 'scissors']
dice1 = {'rock': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
         'paper': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
         'scissors': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

computer_choice = dice[random.randint(0, 2)]
user_choice = int(input("What do you choose? Type  0 for Rock 1 for Paper 2 for Scissor "))
if user_choice >2:
    print("Enter valid number Type  0 for Rock 1 for Paper 2 for Scissor")
else:
    user_choice = dice[user_choice]
    print(dice1[user_choice])
    if computer_choice == 'rock' and user_choice == 'scissor':
        print(f'Computer Chose: \n {dice1[computer_choice]}\n Computer won') 
    elif computer_choice == 'paper' and user_choice=='rock':
            print(f'Computer Chose: \n {dice1[computer_choice]}\n Computer won')
    elif computer_choice == 'scissor' and user_choice == 'paper':
            print(f'Computer Chose: \n {dice1[computer_choice]}\n Computer won')
    elif computer_choice == user_choice :
            print(f'Computer Chose: \n {dice1[computer_choice]}\n Draw')
    else:
            print(f'Computer Chose: \n {dice1[computer_choice]}\n You  won')
