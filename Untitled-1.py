s = input("Введіть рядок: ")

k_liter = 0
k_cifr = 0

for c in s:
    if c.isalpha():
        k_liter += 1
    elif c.isdigit():
        k_cifr += 1
        
print('Кількість літер =', k_liter)
print('Кількість цифр =', k_cifr)
