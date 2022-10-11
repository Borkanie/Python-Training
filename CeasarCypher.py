import string


def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)

def caesarNoTranslate(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    newText = ""
    for letter in plain_text:
        if letter in letters:
            letter=letters[(letters.index(letter)+shift_num)%len(letters)]
        newText+=letter
    return newText


def main():
    value = input("Please enter the message to cypher:\n")
    positionsToShift=int(input("Please enter how many positions to shift the characters:\n"))
    newVal = caesarNoTranslate(value,positionsToShift)
    print("The encrypted message withouth translation is: ",newVal)
    newVal = caesar(value,positionsToShift)
    print("The encrypted message is: ",newVal)

if __name__=="__main__":
    main()