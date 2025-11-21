import sys

def convert_decimal_to_bases(decimal_arg=None):
    """
    Prompts the user for a decimal number and converts it to 
    binary, hexadecimal, and octal formats.
    """
    print("\n--- Decimal Base Converter (Python) ---")
    # If a decimal value was provided by the caller (or via argv/stdin),
    # use it and skip the interactive prompt.
    decimal_input = None

    if decimal_arg is not None:
        decimal_input = str(decimal_arg)
    else:
        # Check for command-line argument (argv)
        if len(sys.argv) > 1:
            decimal_input = sys.argv[1]
        # Check if stdin is piped (non-tty). Read any piped content.
        elif not sys.stdin.isatty():
            piped = sys.stdin.read().strip()
            if piped:
                # take the first token from piped input
                decimal_input = piped.split()[0]

    while True:
        try:
            # If we already got input from argv/piped stdin, use it.
            if decimal_input is None:
                # Get input from the user
                decimal_input = input("Enter a positive whole number (decimal): ")
            
            # Basic validation for empty input
            if not decimal_input.strip():
                print("Input cannot be empty. Please try again.")
                continue

            # Convert input string to an integer
            decimal_num = int(decimal_input)
            
            # Check for non-negative integer
            if decimal_num < 0:
                print("Please enter a POSITIVE whole number.")
                continue
            
            break # Exit the loop if input is valid
            
        except ValueError:
            # Handle cases where the input is not a valid integer
            print("Invalid input. Please enter a valid whole number (e.g., 42, 255).")
        except (EOFError, KeyboardInterrupt):
            # Happens when running in a non-interactive environment (no stdin)
            # or when the user interrupts the program (Ctrl+C).
            print("No input available or operation cancelled. Exiting.")
            return
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            return # Exit function on critical error

    # --- Conversion Logic ---
    # Python has built-in functions for quick base conversion:
    # bin() for binary (returns '0b...')
    # hex() for hexadecimal (returns '0x...')
    # oct() for octal (returns '0o...')
    
    # 1. Binary conversion
    # We use [2:] slicing to remove the '0b' prefix
    binary_num = bin(decimal_num)[2:]
    
    # 2. Hexadecimal conversion
    # We use [2:] slicing to remove the '0x' prefix and then make it uppercase
    hex_num = hex(decimal_num)[2:].upper()
    
    # 3. Octal conversion
    # We use [2:] slicing to remove the '0o' prefix
    octal_num = oct(decimal_num)[2:]
    
    # --- Output Results ---
    print("\n--- Conversion Results ---")
    print(f"Decimal (Base 10): {decimal_num}")
    print(f"Binary (Base 2):   {binary_num}")
    print(f"Hexadecimal (Base 16): {hex_num}")
    print(f"Octal (Base 8):    {octal_num}")
    print("--------------------------")
    
    # Return to the caller so the caller can decide how to exit
    return

# Run the function when the script is executed
if __name__ == "__main__":
    print("Program loaded. Starting conversion process...")
    convert_decimal_to_bases()
    # Exit explicitly here so scripts that import this module won't exit
    sys.exit(0)