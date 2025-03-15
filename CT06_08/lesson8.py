print("Hello from lesson 8")
import time
sec = int(input("How many seconds do you want to countdown from? "))
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print ("happy new year!")