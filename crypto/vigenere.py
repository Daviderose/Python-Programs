from helpers import alphabet_position, rotate_character

def encrypt(text,key):
    '''This function takes in a text message and keyword and encrypts it using vigenere encryption.'''

    xs = key
    listed_key = list(xs)
    keyed_text = []
    indexed_text = []
    encrypted_text = ''
    index = 0
    index2 = 0

    for i in text:
        if i.isalpha() == False:
            keyed_text += i
            continue
        keyed_text += listed_key[index]
        index += 1
        if index > len(key) - 1:
            index = 0

    keyed_text = ''.join(keyed_text)
        
    for i in text:
        j = 0
        if i.isalpha() == False:
            encrypted_text += i
            index2 += 1
            continue
        j = rotate_character(i,alphabet_position(keyed_text[index2]))
        encrypted_text += j
        index2 += 1

    return encrypted_text

def main():
    '''This function calls the encrypt function and prints out the result.'''

    from sys import argv,exit

    try:
        secret_key = argv[1]
    except IndexError:
        print('Please enter a valid keyword: (python vigenere.py *keyword*)\nA valid keyword must contain no numbers or decimals.\nOnly alphabetic characters.')
        exit()
    except ValueError:
        print('Please enter a valid keyword: (python vigenere.py *keyword*)\nA valid keyword must contain no numbers or decimals.\nOnly alphabetic characters.')
        exit()

    if argv[1].isalpha() == False:
        print('Please enter a valid keyword: (python vigenere.py *keyword*)\nA valid keyword must contain no numbers or decimals.\nOnly alphabetic characters.')
        exit()

    message = input('Type a message you would like to encrypt:')
    
    print(encrypt(message,secret_key))

if __name__ == '__main__':
    main()
	    
	    
	    

	    

