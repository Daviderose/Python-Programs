def get_initials(fullname):
    """ This function takes in a person's name, returns the person's initials (uppercase) """
    
    saved_name = fullname
    names_listed = saved_name.split()
    initials = ''

    for name in names_listed:
	    initials += name[0].upper()

    return initials

def main():
    fullname = input('What is your full name?')
    print(get_initials(fullname))

if __name__ == '__main__':
    main()