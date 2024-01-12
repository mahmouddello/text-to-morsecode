import time
import logging
from morsecoder import MorseCoder
from typing import Callable, Optional

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
        final_choice: Optional[Callable[[], str]] = funcs.get(choice, None)
        if final_choice is not None:
            print(final_choice())
        else:
            logging.warning(f"Wrong key!")
    finally:
        want_to_quit: str = input("\nWant to quit? type 'Y': ")
        if want_to_quit.upper() == "Y":
            still_on = False
