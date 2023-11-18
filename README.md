# Тема 7. Работа с файлами (ввод, вывод)
### Отчет по Теме #7 выполнил:
- Ланцов Матвей Максимович
- ПИЭ-21-2

| Задание | Сам. раб. |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №7
## Задание №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
#### Выполнение:
```python
from collections import Counter
import re

def count_words(text):

    words = re.findall(r'\b\w+\b', text.lower())


    word_counts = Counter(words)


    most_common_word, count = word_counts.most_common(1)[0]

    return most_common_word, count

if __name__ == "__main__":
    # Задайте абсолютный путь к вашему файлу
    file_path = "C:\\Users\\1\\PycharmProjects\\pythonProject1\\Text_1.txt"

    try:

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        most_common_word, count = count_words(text)


        print(f"Самое популярное слово: {most_common_word}")
        print(f"Количество использований: {count}")

    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
```
#### Результат:
![image](https://github.com/qq072/MatveyLantsov/assets/103333884/8fc25720-8405-4311-b491-8a9bb11b6cb4)

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/49bd0d98-b8ae-413e-8ddb-de49c67cbf7c)


#### Вывод: Программа успешно считывает текст из указанного файла, а затем подсчитывает количество слов и определяет самое популярное слово с его количеством использований. Убедитесь, что указанный путь к файлу верен и файл существует. В случае ошибки при чтении файла программа предоставит соответствующее уведомление.

## Задание №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
#### Выполнение:
```python
def get_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            # Подсчет количества букв латинского алфавита
            alphabet_letters_count = sum(c.isalpha() and c.isascii() for c in text)

            # Подсчет количества слов
            word_count = len(text.split())

            # Подсчет количества строк
            line_count = text.count('\n') + 1

            return alphabet_letters_count, word_count, line_count
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = 'input.txt'

    statistics = get_statistics(file_path)

    if statistics is not None:
        alphabet_letters_count, word_count, line_count = statistics
        print(f"Количество букв латинского алфавита: {alphabet_letters_count}")
        print(f"Количество слов: {word_count}")
        print(f"Количество строк: {line_count}")
    else:
        print(f"Файл '{file_path}' не найден.")
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/d5dbc762-ed4c-4283-9e76-f952dca465e9)

#### Вывод: Данная программа на Python выполняет анализ текстового файла `input.txt`, выводя статистику, включающую количество букв латинского алфавита, число слов и количество строк. Простота использования и понятность вывода делают этот инструмент удобным для быстрого анализа текстовых данных на латинице. Убедитесь, что файл `input.txt` существует в том же каталоге, что и скрипт, и запустите программу для получения статистики.

## Задание №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
#### Выполнение:
```python
def censor_text(sentence, forbidden_words):
    for word in forbidden_words:
        # Заменяем каждое вхождение слова независимо от регистра
        sentence = sentence.replace(word, '*' * len(word), -1)
    return sentence


def load_forbidden_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            forbidden_words = [word.strip().lower() for word in file.read().split()]
        return forbidden_words
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    sentence = input("Введите предложение: ")

    forbidden_words = load_forbidden_words('input.txt')

    if forbidden_words is not None:
        censored_sentence = censor_text(sentence.lower(), forbidden_words)
        print("Цензурированное предложение:")
        print(censored_sentence)
    else:
        print("Файл 'input.txt' не найден.")
```
#### Результат: 

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/0607e90b-ff3c-4d1c-9403-f967fd588625)

## Задание №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
#### Выполнение:
```python
def calculate_average_grade(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            total_students = len(lines)
            total_grades = sum(int(line.split(':')[1].strip()) for line in lines)

            if total_students > 0:
                average_grade = total_grades / total_students
                return average_grade
            else:
                return None
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = 'input.txt'

    average_grade = calculate_average_grade(file_path)

    if average_grade is not None:
        print(f"Средняя зп всех сотрудников: {average_grade:.2f}")
    else:
        print(f"Файл '{file_path}' не найден или не содержит данных.")
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/baf6c88a-f35a-4021-9f0c-c5404104bcc2)

#### Вывод: Программа успешно вычисляет среднюю заработную плату сотрудников предприятия, используя данные из файла `input.txt`, где указаны данные в строку типа "Имя:Зарплата". Для этого предоставлены случайные имена и зарплаты. Пользователь может легко адаптировать эти данные или добавить свои собственные для дополнительного тестирования программы.

## Общий вывод: В ходе решения различных задач на Python, я научился эффективно взаимодействовать с текстовыми файлами, выполнять анализ данных и создавать простые программы для обработки информации. Изучение работы с файлами позволило мне создать программы, способные читать и записывать текстовые данные. Программа для цензурирования текста, анализирующая файл с запрещенными словами, демонстрирует понимание регулярных выражений и методов обработки строк. Решение задачи о среднем балле студентов подчеркивает использование циклов и обработку исключений для обеспечения стабильности программы при работе с файлами. В целом, решение этих задач позволило мне расширить свои навыки программирования на Python и применить их в реальных сценариях.
