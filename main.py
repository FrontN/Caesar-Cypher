from Caesar_Cypher_art import logo
import string

print(logo)
ALPHABET = string.ascii_letters

def encode_and_decode(choice: str, text: str, shift: int):
    """
    Encode or decode a given text using the Caesar Cipher.
    
    Parameters:
    choice (str): either 'encode' or 'decode'
    text (str): the text to be encoded or decoded
    shift (int): the shift number
    
    Returns:
    str: the encoded or decoded text
    """
    result = []
    if choice == "decode":
        shift = shift * (-1)
    for char in text:
        if char in ALPHABET:
            position = ALPHABET.index(char)
            new_position = (position + shift) % len(ALPHABET)
            result.append(ALPHABET[new_position])
        else:
            result.append(char)
    return "".join(result)

go_again = True
while go_again:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    print(f"Here's the encoded result: {encode_and_decode(choice, message, shift)}")
    again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if again == "no":
        print("Bye Bye!!")
        go_again = False
