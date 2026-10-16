x1 = int(input("Введите первый столбец: "))
y1 = int(input("Введите первую строку: "))
x2 = int(input("Введите второй столбец: "))
y2 = int(input("Введите вторую строку: "))

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")