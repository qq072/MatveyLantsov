# Тема 4. Функции и модули
### Отчет по Теме #4 выполнил:
- Ланцов Матвей Максимович
- ПИЭ-21-2

| Задание | Лаб. раб. | Сам. раб. |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
## Задание №1
### Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудьте, что функции комментируются по-особенному.
#### Выполнение:
```python
# Импорт необходимых модулей из стандартной библиотеки Python
from datetime import datetime  # Импорт класса datetime для работы с датой и временем
from math import sqrt  # Импорт функции sqrt из модуля math для вычисления квадратного корня

# Определение функции main с переменными kwargs (аргументы функции, представленные в виде словаря)
def main(**kwargs):
    # Начало цикла: проход по каждой паре ключ-значение в словаре kwargs
    for key in kwargs.items():
        # Расчет результата, который является квадратным корнем суммы квадратов двух элементов в значении словаря
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Вывод значения result на экран
        print(result)

# Проверка, выполняется ли данный код как основная программа (а не как импортированный модуль)
if __name__ == '__main__':
    # Получение текущей даты и времени в момент начала выполнения программы
    start_time = datetime.now()
    
    # Вызов функции main с передачей словаря kwargs, содержащего пять ключей (one, two, three, four, five),
    # каждый из которых связан с двумя числами, представляющими координаты точки
    main(
        one=[10, 3], 
        two=[5, 4], 
        three=[15, 13], 
        four=[93, 53], 
        five=[133, 15]
    )
    
    # Вычисление времени, затраченного на выполнение программы (разница между текущим временем и временем начала)
    time_costs = datetime.now() - start_time
    
    # Вывод на экран строки, содержащей время выполнения программы
    print(f"Время выполнения программы - {time_costs}")
```
#### Результат:
![image](https://github.com/qq072/MatveyLantsov/assets/103333884/c73fa8e6-6d7d-4918-87ca-973fb87b650d)

## Задание №2
### Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо Михаил А.
#### Выполнение:
```python
import random

def dice():
    score = random.randint(1, 6)
    if score == 5 or score == 6:
        print("Вы победили!")
    elif score == 3 or score == 4:
        print("Переброс кубика...")
        dice()
    elif score == 1 or score == 2:
        print("Вы проиграли! :(")

if __name__ == '__main__':
    dice()
```
#### Результат

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/9dc4a19d-f054-4a1b-b9d2-33e9f77bdbd2)

#### Вывод: Эта программа представляет собой симуляцию игры с кубиком, в которой игрок бросает кубик и, в зависимости от выпавшего числа, получает разные результаты. Программа выполнена с помощью функции dice и её рекурсивного вызова.

## Задание №3
### Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд. Программу нужно написать с использованием цикла. Подсказка: необходимо использовать модуль datetime и time, а также вам необходимо как-то “усыплять” программу на 1 секунду.
#### Выполнение:
```python
import datetime
import time

end_time = datetime.datetime.now() + datetime.timedelta(seconds=5)

while datetime.datetime.now() < end_time:
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущее время: {formatted_time}")

    time.sleep(1)
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/99ed821d-abad-4dd4-b880-a46b3c6b9af0)

#### Вывод: Данная программа 5 раз выводит точное время с точностью до секунд каждую секунду с помощью функции 'sleep', которая приостанавливает выполнение программы на определенное кол-во секунд.

## Задание №4
### Напишите программу, которая считает среднее арифметическое от аргументов вызываемое функции, с условием того, что изначальное количество этих аргументов неизвестно. Программу необходимо реализовать используя одну функцию и “точку входа”.
#### Выполнение:
```python
def average(*args):
    if len(args) == 0:
        return None
    total = sum(args)
    return total / len(args)

if __name__ == '__main__':
    values = []

    while True:
        user_input = input("Введите число (или 'Stop' для завершения): ")
        if user_input == 'stop' or user_input == "Stop":
            break
        try:
            value = float(user_input)
            values.append(value)
        except ValueError:
            print("Неверный формат числа. Попробуйте снова.")

    avg = average(*values)
    if avg is not None:
        print(f"Среднее арифметическое: {avg}")
    else:
        print("Нет чисел для вычисления среднего.")
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/b7dacc68-fe09-4573-b7c3-bd80510d1eeb)

#### Вывод: Данная программа позволяет пользователю вводить произвольное количество чисел и затем вычисляет и выводит среднее арифметическое из этих чисел.
