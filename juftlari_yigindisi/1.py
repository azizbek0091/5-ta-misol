import os; os.system("cls")
matn = input("Sonlarni o'z ichiga olgan matn kiriting ==> ")

def juft_sonlar_yigindisi(matn):
    yigindi = 0
    
    sonlar = [int(son) for son in matn.split() if son.isdigit()]
    
    for son in sonlar:
        if son % 2 == 0:  
            yigindi += son
    return yigindi

print(f"Matndagi juft sonlar yig'indisi ==> ", juft_sonlar_yigindisi(matn))