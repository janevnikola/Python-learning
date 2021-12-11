matrica = [
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]  # 2
]
# matrica [0] [1] znaci 0 redica, 1 kolona
print(matrica[0][1])  # pecatenje na 2
print("\n")
print("Obicen print")
for matrica_indeks in matrica:
    print(matrica_indeks)
print("\n printanje na sekoj element vo matricata")
for i in matrica:
    for j in i:
        print(j)
