# File Encryption
# Programmer: Victoria Mendoza

# dictionary
codes = {'A': '%', 'a': '9',
         'B': '@', 'b': '#',
         'C': '!', 'c': '2',
         'D': '^', 'd': '$',
         'E': '&', 'e': '3',
         'F': 'C', 'f': '0',
         'G': '*', 'g': '8',
         'H': '<', 'h': '4',
         'I': '(', 'i': '7',
         'J': ':', 'j': '5',
         "K": '>', 'k': '1',
         'L': ')', 'l': '6',
         'M': '{', 'm': '?',
         'N': '|', 'n': ']',
         'O': '}', 'o': '`',
         'P': ';', 'p': '~',
         'Q': '/', 'q': 'a',
         'R': '=', 'r': 'x',
         'S': '_', 's': '[',
         'T': ',', 't': 'f',
         'U': '-', 'u': 'p',
         'V': '+', 'v': 'e',
         'W': '.', 'w': 'h',
         'X': 'o', 'x': 't',
         'Y': 'r', 'y': 'b',
         'Z': 'u', 'z': 'j',
         '1': 'S', '2': 'V',
         '3': 'J', '4': 'B',
         '5': 'O', '6': 'L',
         '7': 'I', '8': 'R',
         '9': 'W', '0': 'Y',
         ',': 'Q', '.': 'T', '-': 'A'}


def main():
    # open up the .txt file
    open_file = open('python.txt', 'r')
    # read the lines in the .txt file
    file = open_file.readline()
    encrypt(file)


def encrypt(the_file):
    # writes new .txt file
    encrypted_file = open("new_encryption.txt", "w+")
    encrypted = ""

    # look at each letter in the file
    for letter in the_file:
        # if the letter matches a key in the dictionary
        if letter in codes:
            # convert letter to code
            encrypted += codes[letter]
        else:
            # for spaces
            encrypted += letter

    print(encrypted)
    # write to new file
    encrypted_file.write(encrypted)


main()