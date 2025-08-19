# Name: Ian Lee Kim Yen
# My attempt on a simple Caesar Cryptography program, able to encrypt or decrypt text based on your intended shifted value

# Learn different functions of Python


def caesar_cipher(text, shift):
    new_text = ""
    for i in range(len(text)):
        if text[i].isalpha() == False:
            new_text += text[i]
            continue

        else:
            if text[i].isupper():
                num = (ord(text[i]) - ord('A')  + shift) % 26 + ord('A')

            elif text[i].islower():
                num = (ord(text[i]) - ord('a') + shift) % 26 +  ord('a') 

            new_text += chr(num)



    return new_text

def caesar_decrypter(text, shift):
    new_text = ""

    for i in range(len(text)):
        if text[i].isalpha() == False:
            new_text += text[i]
            continue

        else:
            if text[i].isupper():
                num = (ord(text[i]) - ord('A') - shift) % 26 + ord('A')

            elif text[i].islower():
                num = (ord(text[i]) - ord('a') - shift) % 26 + ord('a')

            new_text += chr(num)

    return new_text



def main():
    choice = input("Do you want to encrypt or decrypt text? ")
    text = input("Please enter the text: ")
    while True:
        shift = int(input("Enter how much you want the shift to be: "))
        if shift < 1 or shift > 25:
            print("Error. Number must be between 1 and 25.")
            continue

        break

    if choice.lower().strip() == "encrypt":
        new_text = caesar_cipher(text, shift)

    elif choice.lower().strip() == "decrypt":
        new_text = caesar_decrypter(text, shift)
        
    print(new_text)







if __name__ == "__main__":
    main()
