first=int(input('Введите число 1: '))
second=int(input('Введите число 2: '))
thrird=int(input('Введите число 3: '))
if first==second==thrird:
    print(3)
elif first==second or first==thrird or second==thrird:
    print(2)
else:
    print(0)