import random
import math
A = int(input("A="))
B = int(input("B="))
x = random.randint(A, B)
guess = int(input("guess:"))
count =  int(math.log(B-A+1, 2))
for i in range(0, count+1):
    if guess < x:
        print("small")
        guess = int(input("new guess:"))
    if guess > x:
        print("high")
        guess = int(input("new guess:"))
    else:
        print("good job")
        break
    