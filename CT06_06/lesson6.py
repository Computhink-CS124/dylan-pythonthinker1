# #print("Hello from lesson 6")
# for count in range(2, 25, 2):
#     print(count)
# for count in range(8, 97, 8):
#     print(count)
# for count in range(5, 0, -1):
#     print(count)
# start = int(input("what number do you want with start with ?"))
# stop = int(input("what number do you want to end with "))
# if start > stop:
#     for i in range(start, stop+1):
#         print(i)
# else:
#     for i in range(start, stop-1, -1):
#         print(i)

students = int(input("how many students are there? "))
score = 0
for i in range(students):
    score = score + int(input())