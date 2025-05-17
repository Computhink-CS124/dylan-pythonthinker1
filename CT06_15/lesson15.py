def isEven():
    n % 2 == 0
numbers = [3, 9, 2, 4, 5, 8]
for n in numbers:
    if isEven() == True:
        print (str(n) + " is an even number")
    else:
        print (str(n) + " is an odd number")