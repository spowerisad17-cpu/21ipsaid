import math

x = float(input())
x = math.radians(x)

y = math.sin(x) + math.cos(x) + math.tan(x)**2

print(y)