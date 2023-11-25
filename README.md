### Отчет по Теме #8 выполнил:
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
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/f7e8d2c7-fe1d-4eb1-9936-241efd406dd7)

#### Вывод: класс, представляющий книгу, и объект этого класса.

## Задание №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

my_book = Book("Anna Carenina", "Tolstoi")

my_book.info()
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/19b50fcf-7476-4e0b-96f8-877e7ba2479d)

### Вывод:класс, представляющий книгу, и объект этого класса. В этом примере книга будет иметь атрибуты title (название) и author (автор), а также метод display_info(), который выводит информацию о книге.

## Задание №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли

#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

my_book = Book("Anna Carenina", "Tolstoi")



class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format

    def info(self):
        super().info()
        print(f"Format: {self.format}")

my_ebook = EBook("Ottsi i deti", "Turgenev", "PDF")

my_ebook.info()
```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/a453f5b4-85e8-41b5-a0f3-aae9fd22e706)

### Вывод: Использовано наследование для создания нового класса EBook, который расширяет функциональность базового класса Book и добавляет новый атрибут format. Метод info в EBook был переопределен для учета нового атрибута и одновременно использования функциональности родительского класса.

## Задание №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def info(self):
        print(f"Book Title: {self._title}")
        print(f"Author: {self._author}")

class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self._format = format

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format

    def info(self):
        super().info()
        print(f"Format: {self.get_format()}")

my_ebook = EBook("Ottsi i deti", "Turgenev", "PDF")

my_ebook.set_title("New Title")

my_ebook.info()

```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/17aa22d3-4f48-46a0-a8a0-12eb580215f0)

#### Вывод: Атрибуты title, author и format закрытыми (приватными) и предоставим методы для получения и установки этих значений. Таким образом, мы скрываем прямой доступ к атрибутам и обеспечиваем контролируемый доступ к данным.

## Задание №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

#### Выполнение:
```python
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def info(self):
        print(f"Book Title: {self._title}")
        print(f"Author: {self._author}")

    def read(self):
        print("Reading a physical book.")

class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self._format = format

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format

    def info(self):
        super().info()
        print(f"Format: {self.get_format()}")

    def read(self):
        print("Reading an ebook.")

my_book = Book("Ottsi i deti", "Turgenev")
my_ebook = EBook("Yevgeniy Onegin", "Pushkin", "PDF")

my_book.read()
my_ebook.read()

```
#### Результат:

![image](https://github.com/qq072/MatveyLantsov/assets/103333884/bab4ec37-c9ea-4111-89be-6bcb7becc478)

#### Вывод: Использованн полиморфизм, где метод read представляет общий интерфейс для чтения книг, но каждый подкласс (Book и EBook) предоставляет свою уникальную реализацию этого метода.

## Общий вывод: 
Объектно-ориентированное программирование (ООП) в Python, как и в других языках программирования, предоставляет ряд преимуществ и инструментов для более удобной и эффективной разработки программ. 
