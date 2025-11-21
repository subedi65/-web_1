import itertools
import string

# Your personal key number, used for the cyclic shift.
KEY_NUMBER = 2024891216
# Convert the number to a sequence of individual digits (shift amounts)
KEY_DIGITS = [int(d) for d in str(KEY_NUMBER)]
# The length of the key sequence (10 digits in this case)
KEY_LENGTH = len(KEY_DIGITS)

# Define the alphabet for the cipher. 
# We include all uppercase and lowercase English letters.
ALPHABET = string.ascii_letters 
ALPHABET_LENGTH = len(ALPHABET) # 52 characters (A-Z, a-z)

# The map is structured so A=0, B=1, ..., Z=25, a=26, b=27, ..., z=51.
CHAR_TO_INDEX = {char: i for i, char in enumerate(ALPHABET)}
INDEX_TO_CHAR = {i: char for i, char in enumerate(ALPHABET)}


def encoder(plaintext: str) -> str:
    """
    Encodes the given plaintext using a Vigenere-like cyclic shift based on the KEY_DIGITS.
    
    The shift is applied only to English letters (A-Z, a-z). Other characters
    (spaces, punctuation, numbers) remain unchanged.
    """
    
    # We use itertools.cycle to endlessly repeat the key digits: 2, 0, 2, 4, 8, 9, 1, 2, 1, 6, 2, 0, 2, 4, ...
    key_cycle = itertools.cycle(KEY_DIGITS)
    ciphertext = []
    
    for char in plaintext:
        if char in CHAR_TO_TO_INDEX:
            # 1. Get the current character's index (0-51)
            char_index = CHAR_TO_INDEX[char]
            
            # 2. Get the next shift value from the key sequence
            shift = next(key_cycle)
            
            # 3. Apply the shift and use the modulo operator (%) to wrap around the alphabet
            new_index = (char_index + shift) % ALPHABET_LENGTH
            
            # 4. Get the new character from the index
            encrypted_char = INDEX_TO_CHAR[new_index]
            ciphertext.append(encrypted_char)
        else:
            # Non-alphabetic characters are not encrypted and do not advance the key
            ciphertext.append(char)
            
    return "".join(ciphertext)


def decoder(ciphertext: str) -> str:
    """
    Decodes the given ciphertext by reversing the cyclic shift.
    
    The key sequence must be applied in the same order as the encoder.
    """
    
    # Use the same cyclic key sequence
    key_cycle = itertools.cycle(KEY_DIGITS)
    plaintext = []
    
    for char in ciphertext:
        if char in CHAR_TO_INDEX:
            # 1. Get the current character's index (0-51)
            char_index = CHAR_TO_INDEX[char]
            
            # 2. Get the next shift value from the key sequence
            shift = next(key_cycle)
            
            # 3. Apply the REVERSE shift. We add ALPHABET_LENGTH before subtracting 
            #    to ensure the modulo operation handles negative numbers correctly.
            new_index = (char_index - shift + ALPHABET_LENGTH) % ALPHABET_LENGTH
            
            # 4. Get the new character from the index
            decrypted_char = INDEX_TO_CHAR[new_index]
            plaintext.append(decrypted_char)
        else:
            # Non-alphabetic characters are not decrypted and do not advance the key
            plaintext.append(char)
            
    return "".join(plaintext)

# --- Demonstration ---
if __name__ == "__main__":
    print(f"--- Cyclic Encoder/Decoder Demo ---")
    print(f"Key Number: {KEY_NUMBER}")
    print(f"Key Digits (Shifts): {KEY_DIGITS}\n")

    # Example 1: Basic sentence
    original_text_1 = "Hello World! This is a secret message."
    
    # Example 2: Text with mixed case, numbers, and punctuation
    original_text_2 = "Cryptography is FUN and $123"

    print(f"[Original Text 1]: {original_text_1}")
    encoded_text_1 = encoder(original_text_1)
    print(f"[Encoded Text 1]:  {encoded_text_1}")
    decoded_text_1 = decoder(encoded_text_1)
    print(f"[Decoded Text 1]:  {decoded_text_1}\n")

    print(f"[Original Text 2]: {original_text_2}")
    encoded_text_2 = encoder(original_text_2)
    print(f"[Encoded Text 2]:  {encoded_text_2}")
    decoded_text_2 = decoder(encoded_text_2)
    print(f"[Decoded Text 2]:  {decoded_text_2}")

    # You can also manually test:
    # my_secret = input("\nEnter text to encode: ")
    # encoded_secret = encoder(my_secret)
    # print(f"Encoded: {encoded_secret}")
    # print(f"Decoded: {decoder(encoded_secret)}")