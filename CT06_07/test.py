start = input("What number do you want to start with")#asking the user what number they want to start with
end = input("What number do you want to end with")#asking the user what number they want to end with
increment = int(input("What number is the increment "))  #asking the user for the increment
for i in range(start, end, increment):
    print (i)