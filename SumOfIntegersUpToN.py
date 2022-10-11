

def sumUpToN(n:int)->int:
    returnValue=0
    for i in range(1,n):
        returnValue+=i
    return returnValue

def main():
    value = int(input("Please enter a integer:\n"))
    value = sumUpToN(value)
    print("Values of the sum is: ",value)

if __name__=="__main__":
    main()