import random
word_list=["Anoa","Asse","Bear","Dog","Cat"]
word=random.choice(word_list).lower()
#print(word)
lifeline=6
title='''
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝'''
final_word=["_"]*len(word)
print(title)
print(final_word)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
letter =""
while not lifeline == 0 : 
    guess=input("Enter Letter :").lower()
    for pos  in range(len(word)):
        if guess == word[pos]:
            final_word[pos]=guess
            print(final_word)
    if guess not in word and "_" in final_word:
        lifeline-=1
        print("Your Choosion letter not in word. 🥲  You lose life.")
        print(stages[lifeline])
    elif "_" not in final_word:
        print("🎉 You win 😄 ")
        exit()