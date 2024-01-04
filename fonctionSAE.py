import random

tab1_10 = []
tab2_10 = []
tab3_10 = []
tab4_10 = []
tab5_10 = []
tab6_10 = []
tab7_10 = []
tab8_10 = []
tab9_10 = []
tab10_10 = []

tab1_500 = []
tab2_500 = []
tab3_500 = []
tab4_500 = []
tab5_500 = []
tab6_500 = []
tab7_500 = []
tab8_500 = []
tab9_500 = []
tab10_500 = []

tab1_5000 = []
tab2_5000 = []
tab3_5000 = []
tab4_5000 = []
tab5_5000 = []
tab6_5000 = []
tab7_5000 = []
tab8_5000 = []
tab9_5000 = []
tab10_5000 = []

tab_10 = [tab1_10, tab2_10, tab3_10, tab4_10, tab5_10, tab6_10, tab7_10, tab8_10, tab9_10, tab10_10]
tab_500 = [tab1_500, tab2_500, tab3_500, tab4_500, tab5_500, tab6_500, tab7_500, tab8_500, tab9_500, tab10_500]
tab_5000 = [tab1_5000, tab2_5000, tab3_5000, tab4_5000, tab5_5000, tab6_5000, tab7_5000, tab8_5000, tab9_5000, tab10_5000]

i = 0
while i < 10:
    j = 0
    while j < 10:
        tab_10[j].append(random.randint(0, 100))
        j = j + 1
    i = i + 1

i = 0
while i < 500:
    j = 0
    while j < 10:
        tab_500[j].append(random.randint(0, 100))
        j = j + 1
    i = i + 1

i = 0
while i < 5000:
    j = 0
    while j < 10:
        tab_5000[j].append(random.randint(0, 100))
        j = j + 1
    i = i + 1


def tri_selection(tab):
    i = 0
    j = 0
    while i < len(tab) - 1:
        min = i
        j = i + 1
        while j < len(tab):
            if tab[j] < tab[min]:
                min = j
            j = j + 1
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
        i = i + 1


def interclassement(left, right, tab):
    compteur = 0
    i = j = k = 0
    compteur = compteur + 1
    while i < len(left) and j < len(right):
        compteur = compteur + 1
        if left[i] < right[j]:
            compteur = compteur + 1
            tab[k] = left[i]
            compteur = compteur + 1
            i += 1
            compteur = compteur + 1
        else:
            compteur = compteur + 1
            tab[k] = right[j]
            compteur = compteur + 1
            j += 1
            compteur = compteur + 1
        k += 1
        compteur = compteur + 1

    while i < len(left):
        compteur = compteur + 1
        tab[k] = left[i]
        compteur = compteur + 1
        i += 1
        compteur = compteur + 1
        k += 1
        compteur = compteur + 1

    while j < len(right):
        compteur = compteur + 1
        tab[k] = right[j]
        compteur = compteur + 1
        j += 1
        compteur = compteur + 1
        k += 1
        compteur = compteur + 1
        
    return compteur

def tri_fusion(tab):
    
    compteur = 0
    n = len(tab)
    compteur = compteur + 1
    if n > 1:
        mid = n // 2
        compteur = compteur + 1
        left = tab[:mid]
        compteur = compteur + 1
        right = tab[mid:]
        compteur = compteur + 1

        tri_fusion(left)
        compteur = compteur + 1
        tri_fusion(right)
        compteur = compteur + 1

        tab3 = [0] * n
        compteur = compteur + 1
        interclassement(left, right, tab3)
        compteur1 = interclassement(left, right, tab)
        compteur = compteur + 1
        copie(tab3, tab)
        compteur = compteur + 1
        compteur = compteur + compteur1 
        
    print(f"Nombre d'operations elementaires du tri par selection : {compteur}")    
    return(compteur)


def recherche_dicho(tab:[int],e:int):
    compteur=0
    deb=0
    fin=len(tab)-1
    ind = -1

    compteur = 5 + compteur

    while deb < fin:
        millieu = (fin + deb) //2

        compteur = 4 + compteur

        if tab[millieu] < e:

            deb = millieu + 1
            compteur = 3 + compteur

        elif tab[millieu] > e:

            fin = millieu - 1
            compteur = 4 + compteur

        else:

            ind = millieu
            compteur = 3 + compteur
           

    print(f"Nombre d'operations elementaires du tri par selection : {compteur}")
    return compteur



"""
print("tab_10 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + tri_selection(tab_10[i])
    i = i + 1
print(f"Moyenne = {calcul / 10}")

print("tab_500 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + tri_selection(tab_500[i])
    i = i + 1
print(f"Moyenne = {calcul / 10}")

print("tab_5000 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + tri_selection(tab_5000[i])
    i = i + 1
print(f"Moyenne = {calcul / 10}")
"""




"""
print("tab_10 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + recherche_dicho(tab_10[i], 0)
    i = i + 1
print(f"Moyenne = {calcul / 10}")

print("tab_500 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + recherche_dicho(tab_500[i], 0)
    i = i + 1
print(f"Moyenne = {calcul / 10}")

print("tab_5000 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + recherche_dicho(tab_5000[i], 0)
    i = i + 1
print(f"Moyenne = {calcul / 10}")
"""


print("tab_10 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + tri_fusion(tab_10[i])
    i = i + 1
print(f"Moyenne = {calcul / 10}")

print("tab_500 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + tri_fusion(tab_500[i])
    i = i + 1
print(f"Moyenne = {calcul / 10}")

print("tab_5000 : ")
calcul = 0
i = 0
while i < 10:
    calcul = calcul + tri_fusion(tab_5000[i])
    i = i + 1
print(f"Moyenne = {calcul / 10}")





def interclassement(tab1:[int],tab2:[int],tab3:[int]) :
    j=0
    i=0
    K=0
    n1=len(tab1)
    n2=len(tab2)

    while i < n1 and j < n2 :
        if tab1[i]<=tab2[j] :
            tab3[k]=tab1[i]
            i=i+1
        else
            tab3[k]=tab2[j]
            j=j+1
        k=k+1
        while i < n1 :
             tab3[k]=tab1[i]
             i=i+1
             k=k+1
        while j < n2 :
            tab3[k]=tab2[j]
            j=j+1
            k=k+1

def copie(tab1:[int],tab2:[int]) :
    n=len(tab1)
    i=0
    while i<n :
        tab2[i]=tab1[i]
        i=i+1

def tri_fusion (tab)
    n=len(tab)
    if n<1:
        mil=n//2
        tri_fusion(tab[:mil])
        tri_fusion(tab[mil:])
        tab3=empty(int,n)
        interclassement(tab[:mil],tab[mil:],tab3)
        copie(tab3,tab)