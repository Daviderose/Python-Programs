def alphabet_position(letter):
    '''This function takes in a letter and returns it's corresponding index: (a = 0, z = 25)'''

    letter = letter.lower()
    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    position = alpha_list.index(letter)

    return position

def rotate_character(char,rot):
    '''This function takes in a letter and rotates it according to the second argument given.'''

    new_char = ''
    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    char_index = alphabet_position(char)
    new_index = char_index + rot

    if char.isalpha() == False:
        return char
     
    if char_index == 25:
        char_index = -1
    
    if new_index > 25:
        new_index = new_index % 26

    new_char = alpha_list[new_index]

    if char != char.lower():
        new_char = new_char.upper()

    return new_char