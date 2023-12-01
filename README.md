# Тема 9. Концепции и принципы ООП.
### Отчет по Теме #9 выполнил:
- Ланцов Матвей Максимович
- ПИЭ-21-2

| Задание | Лаб. раб. | Сам. раб. |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
## Задание №1
### Задания для самостоятельного выполнения:
Задание Садовник и помидоры.
Классовая структура:
Есть Помидор со следующими характеристиками:
• Индекс
• Стадия созревания (стадии: отсутствует, цветение, зеленый, красный)
Помидор может:
• Расти (переходить на следующую стадию созревания)
• Предоставлять информацию о своей зрелости
Есть Куст с помидорами, который:
• Содержит список томатов, которые на нем растут
А также может:
• Расти вместе с томатами
• Предоставлять информацию о зрелости всех томатов
• Предоставлять урожай
И также есть Садовник, который имеет:
• Имя
• Растение, за которым он ухаживает
Он может:
• Ухаживать за растением
• Собирать с него урожай

Задание:
Класс Tomato:
1) Создайте класс Tomato
2) Создайте статическое свойство states, которое будет содержать все
стадии созревания помидора
3) Создайте метод __init__(), внутри которого будут определены два
динамических свойства: _index (передается параметром) и _state

(принимает первое значение из словаря states). После написания
этого блока кода в комментарии к нему укажите какими являются
эти два свойства
4) Создайте метод grow(), который будет переводить томат на
следующую стадию созревания
5) Создайте метод is_ripe(), который будет проверять, что томат созрел
Класс TomatoBush:
1) Создайте класс TomatoBush
2) Определите метод __init__(), который будет принимать в качестве
параметра количество томатов и на его основе будет создавать
список объектов класса Tomato. Данный список будет храниться
внутри динамического свойства tomatoes
3) Создайте метод grow_all(), который будет переводить все объекты
из списка томатов на следующий этап созревания
4) Создайте метод all_are_ripe(), который будет возвращать True, если
все томаты из списка стали спелыми.
5) Создайте метод give_away_all(), который будет чистить список
томатов после сбора урожая
Класс Gardener:
1) Создайте класс Gardener
2) Создайте метод __init__(), внутри которого будут определены два
динамических свойства: name (передается параметром, является
публичным) и _plant (принимает объект класса TomatoBush). После
написания этого блока кода в комментарии к нему укажите какими
являются эти два свойства
3) Создайте метод work(), который заставляет садовника работать, что
позволяет растению становиться более зрелым
4) Создайте метод harvest(), который проверяет, все ли плоды созрели.
Если все, то садовник собирает урожай. Если нет, то метод печатает
предупреждение
5) Создайте статический метод knowledge_base(), который выведет в
консоль справку по садоводству
Тесты:
1) Вызовите справку по садоводству
2) Создайте объекты классов TomatoBush и Gardener
3) Используя объект класса Gardener, поухаживайте за кустом с
помидорами
4) Попробуйте собрать урожай, когда томаты еще не дозрели.
Продолжайте ухаживать за ними
5) Соберите урожай
Результатом работы вашей программы будет листинг кода с подробными
комментариями и скриншоты выполенния всех тестов.

Тест 1
#### Выполнение:
```python
class Tomato:
    states = {
        0: "отсутствует",
        1: "цветение",
        2: "зеленый",
        3: "красный"
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Сбор урожая...")
            self._plant.give_away_all()
        else:
            print("Помидоры не созрели. Продолжай выращивать.")

    @staticmethod
    def knowledge_base():
        print("База знаний садовода:")
        print("- Поливай растения регулярно.")
        print("- Нужно больше солнечнного света.")
        print("- ИСпользуй удобрение для улучшение почвы.")

Gardener.knowledge_base()
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/8b58e88e-f3e0-40b7-a06d-f0e0f198f97a)

## Тест 2
#### Выполнение:
```python
class Tomato:
    states = {
        0: "отсутствует",
        1: "цветение",
        2: "зеленый",
        3: "красный"
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Сбор урожая...")
            self._plant.give_away_all()
        else:
            print("Помидоры не созрели. Продолжай выращивать.")

    @staticmethod
    def knowledge_base():
        print("База знаний садовода:")
        print("- Поливай растения регулярно.")
        print("- Нужно больше солнечнного света.")
        print("- ИСпользуй удобрение для улучшение почвы.")

# Создаем объекты классов TomatoBush и Gardener
tomato_bush = TomatoBush(num_tomatoes=5)
gardener = Gardener(name="John", plant=tomato_bush)

```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/7abfb277-b5d0-423d-ba10-0682f9c76394)

## Тест 3
#### Выполнение:
```python
class Tomato:
    states = {
        0: "отсутствует",
        1: "цветение",
        2: "зеленый",
        3: "красный"
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Сбор урожая...")
            self._plant.give_away_all()
        else:
            print("Помидоры не созрели. Продолжай выращивать.")

    @staticmethod
    def knowledge_base():
        print("База знаний садовода:")
        print("- Поливай растения регулярно.")
        print("- Нужно больше солнечнного света.")
        print("- ИСпользуй удобрение для улучшение почвы.")



# Создаем объекты классов TomatoBush и Gardener
tomato_bush = TomatoBush(num_tomatoes=5)
gardener = Gardener(name="John", plant=tomato_bush)

# Ухаживаем за кустом с помидорами
gardener.work()
gardener.work()
gardener.work()
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/1c26b40b-2ed4-4a82-af29-fd8e6ccaa8df)

## Тест 4
#### Выполнение:
```python
class Tomato:
    states = {
        0: "отсутствует",
        1: "цветение",
        2: "зеленый",
        3: "красный"
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Сбор урожая...")
            self._plant.give_away_all()
        else:
            print("Помидоры не созрели. Продолжай выращивать.")

    @staticmethod
    def knowledge_base():
        print("База знаний садовода:")
        print("- Поливай растения регулярно.")
        print("- Нужно больше солнечнного света.")
        print("- ИСпользуй удобрение для улучшение почвы.")




# Создаем объекты классов TomatoBush и Gardener
tomato_bush = TomatoBush(num_tomatoes=5)
gardener = Gardener(name="John", plant=tomato_bush)
# Попробуем собрать урожай, когда томаты еще не дозрели
gardener.harvest()

# Продолжаем ухаживать за помидорами
gardener.work()
gardener.work()
gardener.work()

# Собираем урожай
gardener.harvest()

```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/69cb1017-85aa-4f19-8e51-278d46803537)

## Тест 5
#### Выполнение:
```python
class Tomato:
    states = {
        0: "отсутствует",
        1: "цветение",
        2: "зеленый",
        3: "красный"
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Сбор урожая...")
            self._plant.give_away_all()
        else:
            print("Помидоры не созрели. Продолжай выращивать.")

    @staticmethod
    def knowledge_base():
        print("База знаний садовода:")
        print("- Поливай растения регулярно.")
        print("- Нужно больше солнечнного света.")
        print("- ИСпользуй удобрение для улучшение почвы.")




# Создаем объекты классов TomatoBush и Gardener
tomato_bush = TomatoBush(num_tomatoes=5)
gardener = Gardener(name="John", plant=tomato_bush)
# Попробуем собрать урожай, когда томаты еще не дозрели
gardener.harvest()

# Продолжаем ухаживать за помидорами
gardener.work()
gardener.work()
gardener.work()

# Собираем урожай
gardener.harvest()

# Собираем урожай
gardener.harvest()

# Выводим информацию о зрелости томатов в кусте после сбора урожая
print("\nAre all tomatoes ripe?", gardener._plant.all_are_ripe())

# Проверяем состояние каждого томата после сбора урожая
for i, tomato in enumerate(gardener._plant.tomatoes, 1):
    print(f"Tomato {i}: State - {Tomato.states[tomato._state]}, Ripe - {tomato.is_ripe()}")

```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/55949b0d-d097-4df8-9f61-64ec79432e2f)

### Вывод: Этот код создает классы Tomato, TomatoBush и Gardener, а также проводит тесты, демонстрируя работу садовника и его взаимодействие с кустом помидоров.

## Общий вывод: 
Объектно-ориентированное программирование (ООП) в Python, как и в других языках программирования, предоставляет ряд преимуществ и инструментов для более удобной и эффективной разработки программ. 
