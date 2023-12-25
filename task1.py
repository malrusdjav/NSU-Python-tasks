#Малиев Р.Д.
#Программа для оценки температуры
#23.12.23

temperature = (float)(input("Введите температуру в Цельсиях:"))

if(temperature<=15.5):
    print("ХОЛОДНО")
elif(temperature>28):
    print("ЖАРКО")
else:
    print("НОРМАЛЬНО")