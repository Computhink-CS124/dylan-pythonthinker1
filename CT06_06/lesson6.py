# #print("Hello from lesson 6")
# for count in range(2, 25, 2):
#     print(count)
# for count in range(8, 97, 8):
#     print(count)
# for count in range(5, 0, -1):
#     print(count)
start = int(input("what number do you want with start with ?"))
stop = int(input("what number do you want to end with "))
if start > stop:
    for i in range(start, stop+1):
        print(i)
else:
    stop = stop - 1
    for i in range(start, stop-1, -1):
        print(i)