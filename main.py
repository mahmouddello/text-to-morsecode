import logging
import time
from typing import Callable


class MorseCoder:
    def __init__(self, codes):
        self.codes = codes
        self.encoded_message = ""
        self.decoded_message = ""

    def text_to_morse(self) -> str:
        """Convert text to morse by looping over dictionary keys and getting the corresponding value"""
        self.encoded_message = ""  # ensure to clear the message in each new call
        text = input("What would you like to convert to morse code?\n")
        for letter in text:
            self.encoded_message += self.codes[letter.upper()] + " "
        return f"Your encoded message to morse code is:\n{self.encoded_message}"

    def morse_to_text(self) -> str:
        """Convert morse code to text"""
        self.decoded_message = ""  # ensure to clear the message in each new call
        code = input("What would you want to convert to text?\n")
        # getting the key from the value (knowing that every morse code is unique for each letter)
        keys_list = list(self.codes.keys())
        values_list = list(self.codes.values())
        code_list = code.split(" ")
        for coded_letter in code_list:
            try:
                position = values_list.index(coded_letter)
                self.decoded_message += keys_list[position]
            except ValueError:
                logging.warning("A letter has not been found in the original dictionary!")
        return f"Your decoded message is:\n{self.decoded_message}"


morse_codes = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/', '': ''
}

still_on: bool = True
morse_coder: MorseCoder = MorseCoder(codes=morse_codes)
funcs: dict = {
    1: morse_coder.text_to_morse,
    2: morse_coder.morse_to_text
}
while still_on:
    try:
        choice: int = int(input("1) Translate text to morse code.\n2) Translate morse code to original text.\n"))
    except ValueError as error:
        logging.warning(f"\nVariable `choice` is not an integer! - {error}")
        time.sleep(0.1)
    else:
        final_choice: Callable[[], str] = funcs.get(choice, None)
        if final_choice is not None:
            print(final_choice())
        else:
            logging.warning(f"Wrong key!")
    finally:
        want_to_quit: str = input("\nWant to quit? type 'Y': ")
        if want_to_quit.upper() == "Y":
            still_on = False