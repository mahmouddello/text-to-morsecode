import logging


class MorseCoder:
    def __init__(self, codes) -> None:
        self.codes = codes
        self.encoded_message = ""
        self.decoded_message = ""

    def text_to_morse(self) -> str:
        """
        Convert text to morse by looping over dictionary keys and getting the corresponding value.
        :return: Morse code of the text as a string.
        """
        self.encoded_message = ""  # ensure to clear the message in each new call
        text = input("What would you like to convert to morse code?\n")
        for letter in text:
            self.encoded_message += self.codes[letter.upper()] + " "
        return f"Your encoded message to morse code is:\n{self.encoded_message}"

    def morse_to_text(self) -> str:
        """
        Converts morse code back to text.
        :return: Decoded text from the given morse code.
        """
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
