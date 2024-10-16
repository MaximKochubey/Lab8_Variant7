s = input("Введіть рядок: ")

letter_count = 0
digit_count = 0

for char in s:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("Кількість літер:", letter_count)
print("Кількість цифр:", digit_count)
