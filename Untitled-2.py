N = int(input("Введіть кількість слів N: "))

spisok_sliv = []

for i in range(N):
    slovo = input(f"Введіть слово {i+1}: ")

    slovo_s_probilami = ' '.join(slovo)

    spisok_sliv.append(slovo_s_probilami)

rezultat = ','.join(spisok_sliv)

print("Результат:", rezultat)
