"""Decode a null cipher based on number of letters after punctuation marks."""
import sys
import string

print("\nList of punctuation marks to check =", string.punctuation, "\n")

def load_text():
    """Load a text file as a string."""
    while True:
        try:
            in_file = input("Enter full filename for message to translate: ")
            with open(in_file) as my_file:
                loaded_txt = my_file.read().strip()
                break
        except IOError as e:
            print("Error opening {}. {}".format(in_file, e), file=sys.stderr)
    return loaded_txt
         
def solve_null_cipher(message, lookahead):
    """Solve a null cipher based on number letters after punctuation mark.

    message = null cipher text as string stripped of whitespace
    lookahead = endpoint of range of letters after punctuation mark to examine
    """
    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print("Using offset of {} after punctuation = {}".format(i, plaintext))
        print()

def main():
    """Load text, solve null cipher."""
    # load & process message:
    loaded_message = load_text()
    print("\nORIGINAL MESSAGE =")
    print("{}".format(loaded_message), "\n")
    
    # remove whitespace:
    message = ''.join(loaded_message.split())

    # get range of possible cipher keys from user:
    while True:
        lookahead = input("\nNumber of letters to check after " \
                          "punctuation mark: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please input a number.", file=sys.stderr)           
    print()

    # run finder function:
    solve_null_cipher(message, lookahead)
    
if __name__ == '__main__':
    main()
