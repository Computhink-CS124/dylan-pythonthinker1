# print("Hello from lesson 13")

balance = 1000
while True:
    userans = int(input("WHAT DO U WANT DO DO ONE WITHDRAW TWO DEPOSIT TREE CHECK HOW MUCH MOOLAH FOUR EXITTT"))
    if userans == 1:
        amoooount = int(input("HWO MUCH MONEY  "))
        if amoooount <= balance:
            balance = balance - amoooount
            print("OKEY  DONE")
        else:
            print("YOU BROKE BOIII U A FAILUREEEEE ")
    if userans == 2:
        amooount = int(input("HOW MUCH"))