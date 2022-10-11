import string


def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


def main():
    value = input("Please enter the message to cypher:\n")
    positionsToShift=int(input("Please enter how many positions to shift the characters:\n"))
    newVal = caesar(value,positionsToShift)
    print("The encrypted message is: ",newVal)

if __name__=="__main__":
    main()