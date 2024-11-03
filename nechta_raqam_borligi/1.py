import os; os.system("cls")
matn = input("Matn kiriting ==> ")

def raqamlar_soni(matn):
    raqamlar_soni = sum(1 for i in matn if i.isdigit())
    return raqamlar_soni

print(f"Matnda nechta {raqamlar_soni(matn)} raqam bor")