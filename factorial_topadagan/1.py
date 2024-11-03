import os; os.system("cls")

n = int(input("Faktorialini topish uchun son kiriting ==> "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"{n} sonining faktoriali ==> ", factorial(n))