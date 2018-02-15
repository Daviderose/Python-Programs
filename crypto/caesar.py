from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    '''This function takes in a text message and a number and rotates the letters by the amount of the number given.'''

    encrypt_str = ''

    for i in text:
        if i.isalpha() == False:
            encrypt_str += i
            continue
        new_char = rotate_character(i,rot)
        encrypt_str += new_char
    return encrypt_str

def main():
    '''This function calls the encrypt function and prints out the result.'''

    from sys import argv,exit

    try:
        rotate = int(argv[1])
    except IndexError:
        print('Please enter a valid integer: (python caesar.py *number*)\nA valid integer must contain no decimals,special or alphabetic characters.')
        exit()
    except ValueError:
        print('Please enter a valid integer: (python caesar.py *number*)\nA valid integer must contain no decimals,special or alphabetic characters.')
        exit()

    message = input('Type a message you would like to encript:')
    print(encrypt(message,rotate))

if __name__ == '__main__':
    main()