import os; os.system("cls")

def toq_sonlar_kvadrati(sonlar):
    return [i**2 for i in sonlar if i % 2 != 0]

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sonlar)

for i in sonlar:
    if i % 2 != 0 :
        print(i, end=" ")
print("toq sonlarning kvadratlari ==> ", toq_sonlar_kvadrati(sonlar))