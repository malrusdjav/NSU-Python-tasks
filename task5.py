#Малиев Р.Д.
#Программа дублирует каждую букву в строке
#23.12.23

cold = "Холодно"
redo2 = 2
cold_long = ''.join([char*redo2 for char in cold])

print(cold_long)