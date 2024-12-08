# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.4.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1crBg8_adhnv34HCebvBxiqMnlZnI8lBO

Введите ваше ФИО:
"""

Копьев Данила Алескандрович

"""***Дисклеймер***

В данной практике запрещено использования функций:


*   sum()
*   min()
*   max()
*   average()
*   reversed()
*   sorted()
*   готовые функции или библиотеки

**Задача 1:**



Интернет-магазин предлагает следующие условия скидок:

*   Для заказов больше 1000 единиц, клиент получает скидку 5%. Если клиент использует промокод SUPERDISCOUNT, он получает скидку 10% (вместо 5%).
*  Для заказов более 5000 единиц, клиент получает скидку 15%, а использование промокода SUPERDISCOUNT увеличивает скидку до 20% (вместо 15%).

Этап 1:
Ввод:
```
Введите стоимость единицы товара: 5
Введите количество товара: 1001
Введите промокод: GiVEMEDISCONT
```

Вывод:

```
Ваша скидка: 5%
Итоговая сумма: 4754.75
```
Этап 2:

Оформите ваш код в виде функции
"""

while True:


  def shop(cost, count, promo):
    if count > 1000:
      if 'SUPERDISCOUNT' in promo:
        print(f'\nВаша скидка: 10%\nИтоговая сумма: {count * cost * 0.9}')
      else:
        print(f'\nВаша скидка: 5%\nИтоговая сумма: {count * cost * 0.95}')
    elif count > 5000:
      if 'SUPERDISCOUNT' in promo:
        print(f'\nВаша скидка: 20%\nИтоговая сумма: {count * cost * 0.8}')
      else:
        print(f'\nВаша скидка: 15%\nИтоговая сумма: {count * cost * 0.85}')
    else:
      print(f'\nВаша скидка: 0%\nИтоговая сумма: {count * cost}')
    return
  shop(cost, count, promo)


  cost = int(input('Введите стоимость единицы товара: '))
  count = int(input('Введите количество товара: '))
  promo = input('Введите промокод: ')

"""**Задача 2:**

Этап 1:
Напишите программу способную отфильтровать список и вывести только положительные элементы


Ввод:
```
-1 5 1 2 -3
```

Вывод:

```
5 1 2
```

Этап 2:

Оформите ваш код в виде функции
"""

def number_filter(numbers):
  i = 0
  while i != len(numbers):
    if int(numbers[i]) <= 0:
      numbers.remove(numbers[i])
    else:
      i += 1
  return numbers


numbers = input().split(' ')
x = number_filter(numbers)
print(' '.join(x))

"""**Задача 3:**

Этап 1:
Напишите программу реализующую Алгоритм Евклида


> Алгоритм Евклида – это алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел.



Ввод:
```
30 18
```

Вывод:

```
6
```

Этап 2:
Оформите ваш код в виде функции

"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


numbers = input().split(' ')
result = gcd(int(numbers[0]), int(numbers[1]))
print(f"НОД({numbers[0]}, {numbers[1]}) = {result}")

"""**Задача 4:**

Этап 1:
Напишите функцию программу, которая принимает строку и возвращает список слов и количество их упомнинаний в предложении

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
apple banana apple
```

Вывод:

```
apple: 2,
banana: 1
```
"""

def word_order(words):
    unique_words = []
    counts = []

    for word in words:
        if word in unique_words:
            index = unique_words.index(word)
            counts[index] += 1
        else:
            unique_words.append(word)
            counts.append(1)


    for i in range(len(unique_words)):
        end_char = ',' if i < len(unique_words) - 1 else ''
        print(f'{unique_words[i]}: {counts[i]}{end_char}')
    return


words = input('Введите слова через пробел: ').split(' ')
word_order(words)

"""**Задача 5:**

Этап 1:
Детектор анаграмм Напишите программу на Python, которая принимает в качестве входных данных две строки и проверяет, являются ли они анаграммами друг друга

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
listen, silent
```

Вывод:

```
True
```
"""

def detect(word_1, word_2):
    if len(word_1) != len(word_2):
        print('False')
        return


    count_1 = {}
    count_2 = {}


    for char in word_1:
        count_1[char] = count_1.get(char, 0) + 1

    for char in word_2:
        count_2[char] = count_2.get(char, 0) + 1


    if count_1 == count_2:
        print('True')
    else:
        print('False')
    return


word = input('Введите два слова через запятую: ').split(', ')
word_1 = list(word[0])
word_2 = list(word[1])
detect(word_1, word_2)

"""**Задача 6:**

Шифр ​​Цезаря

Напишите программу на Python, которая реализует шифр Цезаря, простой метод шифрования, который заменяет каждую букву буквой на фиксированное количество позиций вниз по алфавиту. Программа должна запрашивать у пользователя сообщение и значение сдвига, а затем шифровать и расшифровывать сообщение.

Этап 1:

Напишите код для реализации данной задачи

Этап 2:

Оформите код в виде нескольких функций:

* Зашифровывает сообщение
* Расшифровывает сообщение
"""

def code(text, space, shifted_text):
  for char in text:
    if char in letters:
        index = letters.index(char)
        new_index = (index + space) % len(letters)
        shifted_text.append(letters[new_index])
    else:
        shifted_text.append(char)
  return shifted_text


letters = ['а', 'б', 'в', 'г', 'д', 'е',
           'ё', 'ж', 'з', 'и', 'й', 'к',
           'л', 'м', 'н', 'о', 'п', 'р',
           'с', 'т', 'у', 'ф', 'х', 'ц',
           'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
           'э', 'ю', 'я']
text = list(input('Введите сообщение: ').lower())
space = int(input('Введите значение сдвига: ')) % len(letters)
shifted_text = []


fin = code(text, space, shifted_text)
print(''.join(fin))

"""**Задача 7**

Задача: «Банковская система»

Создайте программу Python, которая имитирует базовую банковскую систему. Система должна иметь следующие функции:

Требования
*   Система должна позволять клиентам создавать счета и хранить их балансы.
*   Система должна позволять клиентам вносить и снимать деньги со своих счетов.
*   Система должна позволять клиентам проверять свой текущий баланс.
*   Система должна позволять клиентам переводить деньги между счетами.
*   Система должна отслеживать транзакции (депозиты, снятия и переводы) и иметь возможность печатать детали транзакций.


Задачи
1. Реализуйте банковскую систему, используя только базовые конструкции Python, такие как def, lists, if, elif и else, без классов или словарей.
Определите функции для создания счетов, внесения и снятия денег, получения балансов счетов, перевода денег между счетами, а также создания и печати транзакций.
2. Напишите основную функцию, которая демонстрирует использование банковской системы путем создания счетов, внесения и снятия денег и перевода денег между счетами.
3. Бонусное задание
Реализуйте способ хранения и печати истории транзакций для каждого счета.

Ограничения
Не используйте классы или словари.
Используйте только базовые конструкции Python, такие как def, lists, if, elif и else.

"""

def action___1(action_1_1):
    while action_1_1 != 2:
        print('\n1. Создание банковского счета\n'
        '2. Вернуться в главное меню\n')
        action_1_1 = int(input('Введите порядковый номер нужного вам действия из перечисленных выше: '))
        if action_1_1 == 1:
            action_1_1_1 = input('\nВведите название счета: ')
            accounts.append(action_1_1_1)
            money_in_accounts.append([])
            print('Ваш счет успешно создан!\n')
        elif action_1_1 == 2:
            break
    return


def action___2(action_1_2):
    while action_1_2 != 2:
                print('\n1. Выбрать счет для пополнения\n'
                '2. Вернуться в главное меню\n')
                action_1_2 = int(input('Введите порядковый номер нужного вам действия из перечисленных выше: '))
                if action_1_2 == 1:
                    for i in range(len(accounts)):
                        print(f'{i + 1}.{accounts[i]}')
                    action_1_2_1 = int(input('\nВыберите порядковый номер счета для пополнения: '))
                    action_1_2_2 = int(input('\nВведите сумму для пополнения данного счета (в рублях): '))
                    money_in_accounts[action_1_2_1 - 1].append(action_1_2_2)
                    print('\nВаш счет успешно пополнен!')
                elif action_1_2 == 2:
                    break
    return


def action___3(action_1_3):
    while action_1_3 != 2:
            print('\n1. Выбрать счет для снятия\n'
            '2. Вернуться в главное меню\n')
            action_1_3 = int(input('Введите порядковый номер нужного вам действия из перечисленных выше: '))
            if action_1_3 == 1:
                for i in range(len(accounts)):
                    print(f'{i + 1}.{accounts[i]}')
                action_1_3_1 = int(input('\nВыберите порядковый номер счета для снятия: '))
                action_1_3_2 = int(input('\nВведите сумму для снятия средств со счета (в рублях): '))
                money_in_accounts[action_1_3_1 - 1].append(action_1_3_2 * -1)
                print('\nС вашего счета успешно сняты денежные средства!')
            elif action_1_3 == 2:
                break
    return


def action___4(action_1_4):
    while action_1_4 != 2:
        print('\n1. Проверка баланса выбранного счета\n'
        '2. Вернуться в главное меню\n')
        action_1_4 = int(input('Введите порядковый номер нужного вам действия из перечисленных выше: '))
        if action_1_4 == 1:
            for i in range(len(accounts)):
                print(f'{i + 1}.{accounts[i]}')
            action_1_4_1 = int(input('\nВыберите порядковый номер счета для просмотра баланса: '))
            print(f'Баланс счета №{action_1_4_1} составляет {sum(money_in_accounts[action_1_4_1 - 1])} рублей')
        elif action_1_4 == 2:
            break
    return


def action___5(action_1_5):
    while action_1_5 != 2:
        print('\n1. Выбор счета для снятия и дальнейшего перевода денежных средств\n'
        '2. Вернуться в главное меню\n')
        action_1_5 = int(input('Введите порядковый номер нужного вам действия из перечисленных выше: '))
        if action_1_5 == 1:
            for i in range(len(accounts)):
                print(f'{i + 1}.{accounts[i]}')
            action_1_5_1 = int(input('\nВыберите порядковый номер счета для снятия денежных средств: '))
            action_1_5_2 = int(input('\nВыберите порядковый номер счета для пополнения денежных средств: '))
            action_1_5_3 = int(input('\nВведите сумму денежных средств для перевода: '))
            money_in_accounts[action_1_5_2 - 1].append(action_1_5_3)
            money_in_accounts[action_1_5_1 - 1].append(action_1_5_3 * -1)
            print('Перевод успешно выполнен!')
        elif action_1_5 == 2:
            break
    return


def action___6():
    break



def body(action_1):
    if action_1 == 1:
        action___1(action_1_1)
    elif action_1 == 2:
        action___2(action_1_2)
    elif action_1 == 3:
        action___3(action_1_3)
    elif action_1 == 4:
        action___4(action_1_4)
    elif action_1 == 5:
        action___5(action_1_5)
    elif action_1 == 6:
        action___6(action_1_6)


accounts = list()
money_in_accounts = list()

while True:
    print('Вас приветствует банковская система \"X-BANK\"\n\n'
    'Я способна выполнять следующие действия:\n'
    '1. Создание банковского счета\n'
    '2. Внесение денежных средств на любой счет\n'
    '3. Снятие денежнных средств с любого счета\n'
    '4. Проверка баланса\n'
    '5. Перевод денежных средств между счетами\n'
    '6. Выход\n')
    action_1 = int(input('Введите порядковый номер нужного вам действия из перечисленных выше: '))
    action_1_1 = 0
    action_1_2 = 0
    action_1_3 = 0
    action_1_4 = 0
    action_1_5 = 0
    body(action_1)

''