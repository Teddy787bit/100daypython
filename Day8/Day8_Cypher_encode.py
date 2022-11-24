alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep=True
def caesar(text, shift, direction):
    cypher = ""
    position = 0
    for char in text:
        if direction == "encode":
            if char in alphabet:
                position = alphabet.index(char)
                new_position=position+shift
                if new_position > 26:
                    cypher+=alphabet[new_position-26]
                else:
                    cypher+=alphabet[new_position]
            else:
                cypher+=char
        elif (direction=="decode"):
            if char in  alphabet:
                position = alphabet.index(char)
                new_position = position-shift
                cypher += alphabet[new_position]
            else:
                cypher+=char
        else:
            print("Select decode or decode")
    print(f"your {direction}d  text is {cypher}")

while keep:
    choice=input("Do you want to encode or decode  text ? yes or no ").lower()
    if choice == 'yes' or choice == 'y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift>26:
            shift=shift%26
        caesar(text=text,shift=shift,direction=direction)
    elif choice=='no' or choice == 'n':
        keep=False
        print("Goodbye 👋 ")
    else:
        print("Kindly enter yes or no ?")

