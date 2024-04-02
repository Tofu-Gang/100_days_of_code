from constants import LETTERS

ALPHABET = LETTERS[:int(len(LETTERS) / 2)]
LOGO = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


########################################################################################################################

def _encode_dialogue() -> None:
    """
    Get a message and the shift number from the user. Then, encode the message with the Caesar cipher.
    """

    print("Type your message (only letters are encoded, the rest stays the same; will be converted to lower case):")
    message = input("> ")
    offset = _get_shift_number()
    print("Here's the encoded result: " + _encode_message(message, offset))


########################################################################################################################

def _decode_dialogue() -> None:
    """
    Get a message encoded with the Caesar cipher and the shift number from the user. Then, decode it.
    """

    print("Type your message (only letters are decoded, the rest stays the same; will be converted to lower case):")
    message = input("> ")
    offset = _get_shift_number()
    print("Here's the decoded result: " + _decode_message(message, offset))


########################################################################################################################

def _get_shift_number() -> int:
    """
    :return: shift number for the Caesar cipher from the user
    """

    while True:
        print("Type the shift number:")
        try:
            offset = int(input("> "))
            return offset
        except ValueError:
            print("Invalid value; integer required.")
            continue


########################################################################################################################

def _encode_message(message: str, offset: int) -> str:
    """
    :param message: message to be decoded
    :param offset: shift number for the Caesar cipher
    :return: message encoded with the Caesar cipher
    """

    result = ""

    for character in message.strip().lower():
        if character in ALPHABET:
            index = (ALPHABET.index(character) + offset) % len(ALPHABET)
            result += ALPHABET[index]
        else:
            result += character

    return result


########################################################################################################################

def _decode_message(message: str, offset: int) -> str:
    """
    :param message: message to be decoded
    :param offset: shift number for the Caesar cipher
    :return: decoded message
    """

    result = ""

    for character in message.strip().lower():
        if character in ALPHABET:
            index = ALPHABET.index(character) - offset
            if index < 0:
                index = len(ALPHABET) + index
            result += ALPHABET[index]
        else:
            result += character

    return result


########################################################################################################################

def run_program() -> None:
    """
    Let the user either encode or decode a message using the Caesar cipher.
    """

    while True:
        print("Type \"(e)ncode\" to encrypt, or type \"(d)ecode\" to decrypt:")
        choice = input("> ").strip().lower()

        if choice in ("e", "encode"):
            _encode_dialogue()
        elif choice in ("d", "decode"):
            _decode_dialogue()
        else:
            print("Invalid value. Try again.")
            continue

        print("Press Enter to continue or Ctrl+C to exit.")
        input()


########################################################################################################################
