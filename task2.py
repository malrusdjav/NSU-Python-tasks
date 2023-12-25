#Малиев Р.Д.
#Программа ищет заданную комбинацию букв в строке
#23.12.23


def findCat(n):
    isThere = False

    strings_list = list(range(n))
    substring1 = "Кот"
    substring2 = "кот"

    for i in range(0, n):
        strings_list[i] = input("Введите строку: ")

    for i in range(0, n):
        if (substring1 in strings_list[i] or substring2 in strings_list[i]):
            isThere = True
            break

    if(isThere):
        print("МЯУ")
    else:
        print("НЕТ")


def main():
    n = (int)(input("Введите количество строк: "))
    findCat(n)

main()





