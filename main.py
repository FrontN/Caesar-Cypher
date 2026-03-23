from Caesar_Cypher_art import logo
import string
import os
import time

ALPHABET = string.ascii_letters

def clear_screen():
    """
    Clears the terminal screen and prints the logo.

    This function is used to create a clean slate on the terminal by clearing the screen and then printing the logo. It checks the operating system and calls either 'cls' or 'clear' to clear the screen, and then prints the logo.

    Returns
    -------
    None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def get_valid_input(prompt: str, valid_options: list):
    """
    Prompts the user for input and checks if the input is valid.

    Parameters
    ----------
    prompt : str
        The prompt to display to the user.
    valid_options : list
        A list of valid options that the user can enter.

    Returns
    -------
    str
        The valid input entered by the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid option. Please try again.")
            time.sleep(1.5)
            clear_screen()

def get_valid_nb(prompt: str):
    """
    Prompts the user for input and checks if the input is a valid number.

    Parameters
    ----------
    prompt : str
        The prompt to display to the user.

    Returns
    -------
    int
        The valid number entered by the user.
    """
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")
            time.sleep(1.5)
            clear_screen()

def encode_and_decode(choice: str, text: str, shift: int):
    """
    Encodes or decodes a given text using the Caesar Cypher algorithm.

    Parameters
    ----------
    choice : str
        The direction of the encoding/decoding. 'encode' for encoding, 'decode' for decoding.
    text : str
        The text to be encoded/decoded.
    shift : int
        The shift number to be used in the encoding/decoding.

    Returns
    -------
    str
        The encoded/decoded text.
    """
    if choice.startswith("d"):
        shift = shift * (-1)
    result = [ALPHABET[(ALPHABET.index(char) + shift) % len(ALPHABET)] for char in text if char in ALPHABET]
    return "".join(result)

def main():
    """
    Main function of the program. This function is an infinite loop that
    continues to prompt the user for input until the user decides to quit.
    The user is asked to select whether they want to encode or decode a
    message and then to input the message and the shift number. The
    result is then printed and the user is asked if they want to go again.
    If the user types 'no' or 'n', the loop is exited and the program ends.
    """
    keep_going = True
    while keep_going:
        clear_screen()
        choice = get_valid_input("Type 'encode' to encrypt, type 'decode' to decrypt: ", ["encode", "encrypt", "decrypt", "decode"])
        clear_screen()
        print(f"{choice} mode selected.".center(50, "*"))
        message = input("Type your message: ")
        shift = get_valid_nb("Type the shift number: ")
        print(f"Here's the {choice}d result: {encode_and_decode(choice, message, shift)}")
        play_again = get_valid_input("Type 'yes' if you want to go again. Otherwise type 'no': ", ["yes", "no", "y", "n"])
        if play_again.startswith("n"):
            keep_going = False
            print("Bye Bye!!")

if __name__ == "__main__":
    main()
