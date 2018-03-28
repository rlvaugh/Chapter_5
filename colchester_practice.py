"""Solve a null cipher based on every nth-letter in every nth-word."""
import sys

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

loaded_message = load_text()

# check loaded message & # of lines
print("\nORIGINAL MESSAGE = {}\n".format(loaded_message))

# convert message to list and get length
message = loaded_message.split()
end = len(message)

# get user input on interval to check
increment = int(input("Input max word & letter position to \
check (e.g., every 1 of 1, 2 of 2, etc.): "))
print()

# find letters at designated intervals               
for i in range(1, increment + 1):
    print("\nUsing increment letter {} of word {}".format(i, i))
    print()
    count = i - 1
    location = i - 1
    for index, word in enumerate(message):
        if index == count:
            if location < len(word):
                print("letter = {}".format(word[location]))
                count += i
            else:
                print("Interval doesn't work", file=sys.stderr)
