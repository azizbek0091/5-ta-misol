import os; os.system("cls")

matn = input("Matn kiriting ==> ")

def unli_harflar(matn):
    unli_harflar = "aeiouAEIOU"  
    tekshirish = [i for i in matn if i in unli_harflar]
    return tekshirish

print("Unli harflar ==> ", unli_harflar(matn))