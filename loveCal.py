print("Welcome to love calcualtor")
name1=input("What is your name? ").lower()
name2=input("Whta is your pathner's name? ").lower()
bothName=name1+name2
print(bothName)
count1=bothName.count('t')+bothName.count('r')+bothName.count('u')+bothName.count('e')
count2=bothName.count('l')+bothName.count('o')+bothName.count('v')+bothName.count('e')
loveCount=int(str(count1)+str(count2))


if (loveCount<10) or (loveCount>90):
    print(f"Your score is {loveCount}, you go together like coke and mentos.")
elif (loveCount>=40) and (loveCount<=50):
    print(f"Your score is {loveCount}, you are alright together.")
else:
    print(f"Your score is {loveCount}.")