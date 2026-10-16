x1 = int(input("Введите первый столбец: "))
y1 = int(input("Введите первую строку: "))
x2 = int(input("Введите второй столбец: "))
y2 = int(input("Введите вторую строку: "))

if x1 == x2 and y1 == y2:
    print("NO")
elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")