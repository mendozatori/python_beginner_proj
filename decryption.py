# File Decryption
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

# rewrite dictionary so values are where keys are
new_codes = dict(zip(codes.values(), codes.keys()))


def main():
    # open up the .txt file
    open_file = open('new_encryption.txt', 'r')
    # read the lines in the .txt file
    file = open_file.readline()
    decrypt(file)


def decrypt(the_file):
    decrypted = ""

    # read each letter in the file
    for letter in the_file:
        # if letter is a value in the dictionary (now key)
        if letter in new_codes:
            # convert code to actual letter
            decrypted += new_codes[letter]
        else:
            # for spaces
            decrypted += letter

    # print to console
    print(decrypted)


main()