#Малиев Р.Д.
#Программа выводит персональное приветствие
#23.12.24

def greet(name, surname):
    greet = "Здравствуйте, "+name+" "+surname
    print(greet)

def main():
    name = input("\nВведите Ваше имя: ")
    surname = input("Введите Вашу фамилию: ")
    greet(name, surname)

main()