#Малиев Р.Д.
#Программа выводит список, вводимый пользователем с клавиатуры, в терминал
#23.12.23

n = (int)(input("Введите количество строк: "))

purchases = list(range(n))

for i in range(0,n):
    purchases[i]=input("Введите строку: ")

for i in range(0, n):
    print(purchases[i])