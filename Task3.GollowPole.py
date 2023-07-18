import random
import requests
import re


def downloads_russian_words() -> list:
    """
    Загружает файл, содержащий русские слова, с удаленного URL-адреса и
    возвращает содержимое в виде строки.

    Принимает:
        None

    Возвращает:
        str: содержимое файла в виде списка.
    """
    response = requests.get(
        "https://raw.githubusercontent.com/LussRus/Rus_words/master/UTF8/txt/raw/summary.txt"
    )
    text = response.content.decode("utf-8")

    return text


def choice_random_word(word_list: list) -> str:
    """
    Выбирает случайное слово из списка.

    Принимает:
        word_list (list): Список слов.

    Возвращает:
        str: Слово.
    """
    random_index = random.randint(0, len(word_list) - 1)

    new_list_words = word_list.split('\n')

    return new_list_words[56]


def is_russian_char(guess: str) -> bool:



    """
    Проверяет, является ли буква из русского алфавита.

    Принимает:
        guess (str): Буква или знак '-'.

    Возвращает:
        bool: True, если буква русского алфавита, False в противном случае
    """
    if (
        (re.match("[а-я]", guess) is None)
        and (ord(guess[0]) != 1105)
        and (ord(guess[0]) != 45)
    ):
        return False
    return True

def main():
    list_words = downloads_russian_words()

    list_word_to_guess = list(word_to_guess)

    user_word = str()

    word_to_guess = 12

    hidden_word = ""
    list_of_tried_letters = ""

    for i in word_to_guess: 
        hidden_word += "_"

    while(guess_number !=0):
        print(hidden_word)
        print(f"Attempts:{guess_number} ")
        print("Letter: ")

        current_letter = input()
        if(is_russian_char(current_letter)):
            if current_letter in list_word_to_guess:
                # hidden_word.replace("_", current_letter)
            for i in list_word_to_guess:
                if (i == current_letter):
                    list_hidden_word[i] = current_letter
            else:
                guess_number = guess_number - 1
                list_of_tried_letters +=current_letter
        else:
            print("Enter russain letter")


if __name__ == "__main__":
    main()