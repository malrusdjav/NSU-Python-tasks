#Малиев Р.Д.
#Программа ищет самое короткое и длинное слово в списке, а также проверяет,
# содержится ли самое короткое в самом длинном

#23.12.23

def min_n_max(words):
    longest = max(words, key=len)
    shortest = min(words, key=len)

    print("Самое короткое слово в списке: "+shortest)
    print("Самое длинное слово в списке: "+longest)

    return shortest, longest

def substr_in_str_checker(shortest, longest):

    char_list = list()  # объявляем пустой список,
                        # куда записываются буквы короткого слова

    for c in shortest:
        char_list.append(c)  # добавляем буквы короткого слова в список

    i = 0
    counter = 0
    while(i<len(char_list)):
        if (char_list[i] in longest):
         counter+=1
        i+=1

    if(counter == len(shortest)): #то есть в counter по размерности должен быть
                                  # как shortest, что значит, что все его буквы в
                                  # произвольной последовательности есть в longest
        print("ДА")
    else:
        print("НЕТ")


def main():
    words = list()

    while(True):
        new_word =input("Введите слово: ")
        if (new_word == "стоп"):
            print("\n\n")
            break
        words.append(new_word)

    shortest, longest = min_n_max(words) #распаковка кортежа
    substr_in_str_checker(shortest, longest)

main()