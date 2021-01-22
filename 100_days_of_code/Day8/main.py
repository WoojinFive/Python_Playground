from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    new_text = ""

    if direction == "decode":
        shift *= -1

    for letter in text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift) % 26
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            new_text += letter

    print(f"The {direction}d text is {new_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Hint: Think about how you can use the modulus (%).
    caesar(direction, text, shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if result == "no":
        should_continue = False
        print("Goodbye")