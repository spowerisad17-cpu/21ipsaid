temperatura = float(input("Введите температуру: "))
davlenie = int(input("Введите давление: "))
puls = int(input("Введите пульс: "))
    
if temperatura < 35 or temperatura > 38 or davlenie < 105 or davlenie > 140 or puls < 55 or puls > 110:
        print("Требуется врач")
elif 36 <= temperatura <= 37 and 110 <= davlenie <= 130 and 60 <= puls <= 100:
        print("Нормальное состояние")
else: 
        print("Легкое недомогание")
        
