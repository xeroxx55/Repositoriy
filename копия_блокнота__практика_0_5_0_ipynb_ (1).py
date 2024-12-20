# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.5.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1af5EyH150pbeo4KFK9OMYRzrl5Bq4Tjo

ФИО:
"""

Копьев Данила Александрович

"""# **Задание 1**

Дан словарь, содержащий имена и возраст людей, напишите программу выводящую возраст человека по имени

Дано:

```
{"Alice": 25, "Bob": 30, "Charlie": 35}
```

Вввод:


```
Alice
```

Вывод:


```
Alice 25
```
"""

my_dict = {"Alice": 25, "Bob": 30, "Charlie": 35}
name = str(input())
print(name, my_dict[name])

"""# **Задание 2**

Дан список, состоящий из целых чисел, необходимо написать функцию считающую сумму всех положительных четных чисел списка

Ввод:

```
1, 2, 3, 4, 5, 6, 7, 8, 9
```

Вывод:


```
20
```

***Запрещено:***

*   Использование готовых функций для суммирования чисел
"""

lst = list(map(int, input().strip().split(", ")))

total_sum = 0

for number in lst:
    if number > 0 and number % 2 == 0:
        total_sum += number

print(total_sum)

"""# **Задание 3**

Дан словарь, содержащий название фрукта и его цвет, выведите список всех желтых фруктов


Дано:

```
fruits_and_colors = {
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}
```

Вывод:


```
Yellow fruits:
banana
lemon
mango
```
"""

fruits_and_colors = {
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}
print('Yellow fruits:')
for v in fruits_and_colors.keys():
  if 'yellow' in fruits_and_colors[v]:
    print(v)

"""# **Задание 4**

Дан словарь, необходимо написать функцию меняющую ключ и значение местами

Дано:


```
{"a": 1, "b": 2, "c": 3}
```

Вывод:

```
{1: 'a', 2: 'b', 3: 'c'}
```
"""

my_dict_1 = {"a": 1, "b": 2, "c": 3}
my_dict_2 = {}
for k, v in my_dict_1.items():
  my_dict_2[v] = k
print(my_dict_2)

"""# **Задание 5**

Дан список слов, неограниченной длинны, сформируйте словарь, где в качестве ключа будет слово, а в качестве значения количество слов

**Критерии**


*   Словарь необходимо отсортировать по убыванию количества элементов в списке.
*   Подсчет элементов должен быть реализован в отдельной функции
*   Сортировка пары `ключ:значение` должна быть реализована также в виде отдельной функции




Дано:
```
['apple','banana','orange','apple','apple','banana']
```


Вывод:
```
{'apple':3, 'banana': 2, 'orange': 1}
```

***Запрещено:***

*   Использование готовых функций для сортировки
*   Использование готовых функций для подсчета элементов
"""

my_dict_1 = ['apple','banana','orange','apple','apple','banana']
my_dict_2 = {}
while my_dict_1 != []:
  a = my_dict_1[0]
  i = 0
  while a in my_dict_1:
    my_dict_1.remove(a)
    i += 1
  my_dict_2[a] = i
print(my_dict_2)

"""# **Задание 6**

Дан словарь, содержащий информацию о людях, необходимо:



*   Вывести всех людей старше 30 лет
*   Вывести список городов и количество людей из словаря проживающих в них
*   Вывести список профессий и список людей для каждой профессии

**Критерии**

Каждый из пунктов необходимо реализовать в виде функции
"""

people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}

people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}


def more_30(people_info):
  for k, v in people_info.items():
    if v["age"] > 30:
      print(k)
  return


more_30(people_info)
print("\n")


def cityes_people(people_info):
  my_dict_zero = {}
  for k,v in people_info.items():
    a = v["city"]
    if a in my_dict_zero:
      my_dict_zero[a] += 1
    else:
      my_dict_zero[a] = 1
    print(a, my_dict_zero[a])
  return my_dict_zero

cityes_people(people_info)
print('\n')


def occupation_pep(people_info):
    my_dict_one = {}
    for k, v in people_info.items():
        b = v["occupation"]
        if b in my_dict_one:
            my_dict_one[b].append(k)
        else:
            my_dict_one[b] = [k]

    formatted_output = []
    for occupation, names in my_dict_one.items():
        formatted_output.append(f"{occupation}: {', '.join(names)}")

    return "\n".join(formatted_output)

print(occupation_pep(people_info))

"""# **Задание 7**

Задание: Разработка системы отзывов о предметах

Описание: Создать программу на Python для хранения и управления отзывами о предметах учебного курса. Программа должна позволять пользователям добавлять, просматривать и удалять отзывы, а также вычислять средний балл по заданному предмету.

**Функционал:**

*   Добавление отзыва и оценки:
   *   Пользователь может ввести название предмета, оценку (от 1 до 5) и текст отзыва.
   *   Отзывы должны храниться в структуре данных (например, словаре), где ключом будет название предмета, а значением - список отзывов (каждый отзыв может хранить оценку и комментарий).
*   Просмотр отзывов и оценок:
   *   Пользователь может запросить отзывы для указанного предмета.
   *   Если для указанного предмета есть отзывы, программа должна отобразить список всех отзывов и соответствующих оценок.
*   Удаление отзыва:
   *   Пользователь может удалить отзыв по индексу. Необходимо заранее уведомить пользователя о том, какие отзывы доступны для удаления.
   *   Программа должна обработать ситуацию, когда индекс введен неправильно.
*   Вычисление среднего балла по предмету:
   *   Пользователь может ввести название предмета, и программа должна вычислить и вывести средний балл по всем отзывам для этого предмета.
   *   Если отзывов нет, программа должна сообщить об этом.


**Критерии:**

*   Код должен быть оформлен в виде функций
*   Необходимо обрабатывать неправильный ввод пользователя
*   Должны быть комментарии к функциям
*   Присутсвует весь дополнительный функционал



**Опционально:**

Предлагаю вам добавить свои критерии оценки или вопросы, на которые должен ответить студент, чтобы оценить пару
"""

reviews = {}

def add_review(subject, rating, comment):
    if subject not in reviews:
        reviews[subject] = []
    reviews[subject].append({"Оценка": rating, "Комментарий": comment})
    print(f"Ваш отзыв успешно добавлен к предмету '{subject}'.")

def view_reviews(subject):
    if subject in reviews and reviews[subject]:
        print(f"Отзывы для предмета '{subject}':")
        for index, review in enumerate(reviews[subject], start=1):
            print(f"{index}. Оценка: {review['Оценка']}, Комментарий: {review['Комментарий']}")
    else:
        print(f"Нет отзывов для предмета '{subject}'.")

def delete_review(subject, index):
    if subject in reviews and 0 <= index < len(reviews[subject]):
        removed_review = reviews[subject].pop(index)
        print(f"Удален отзыв: Оценка: {removed_review['Оценка']}, Комментарий: {removed_review['Комментарий']}")
    else:
        print("Некорректный индекс для удаления отзыва.")

def calculate_average_rating(subject):
    if subject in reviews and reviews[subject]:
        total_rating = sum(review['Оценка'] for review in reviews[subject])
        average = total_rating / len(reviews[subject])
        print(f"Средний балл для предмета '{subject}': {average:.2f}")
    else:
        print(f"Нет отзывов для предмета '{subject}'.")

def main():
    while True:
        choice = int(input("Вас приветствует Отзовик. Выберите действие:\n"
                            "1. Просмотр отзывов по уч. предметам\n"
                            "2. Добавление отзывов\n"
                            "3. Удаление отзывов\n"
                            "4. Просмотр среднего балла по отзывам предмета\n"
                            "5. Выход\n"
                            "Введите число нужного вам действия: "))
        if choice == 1:
            subject = input("Введите название предмета: ")
            view_reviews(subject)
        elif choice == 2:
            subject = input("Введите название предмета: ")
            rating = int(input("Введите оценку (1-5): "))
            while rating < 1 or rating > 5:
                rating = int(input("Введенное число должно быть от 1 до 5: "))
            comment = input("Напишите ваш комментарий: ")
            add_review(subject, rating, comment)
        elif choice == 3:
            subject = input("Введите название предмета для удаления отзыва: ")
            view_reviews(subject)
            if subject in reviews and reviews[subject]:
                index = int(input("Введите номер отзыва для удаления: ")) - 1
                delete_review(subject, index)
        elif choice == 4:
            subject = input("Введите название предмета для вычисления среднего балла: ")
            calculate_average_rating(subject)
        elif choice == 5:
            print("Выход из программы.")
            break
        else:
            print("Некорректный вариант. Пожалуйста, введите число от 1 до 5.")

if __name__ == "__main__":
    main()

