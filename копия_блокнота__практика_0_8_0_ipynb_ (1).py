# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.8.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a7r0CykJ3fnMczsN5yOFYEBsW9now_sy

# Задание 1

Задача: Создать чат бота для получения информации об исследованиях космоса

Описание: Создайте комплексное приложение командной строки, которое будет использоваться в качестве панели управления исследованиями космоса. Данное приложение будет обращаться к https://api.nasa.gov/ для предоставления пользователям набора информации о космосе, включая:

- Астрономическая картинка дня (APOD): Отображение APOD с пояснениями к нему.
- Фотографии с марсохода: позволяет пользователям выбирать и фильтровать фотографии с марсохода по дате и типу камеры.
- Объекты, сближающиеся с Землей (ОСЗ): Поиск и отображение информации об объекте, сближающихся с Землей, на определенную дату, включая их размеры и потенциальную опасность.
- Данные о космической погоде: Отображают последние данные о космической погоде, включая солнечные вспышки и геомагнитные бури.
Приложение должно позволять пользователям ориентироваться в этих функциях, корректно обрабатывать ошибки и обеспечивать удобство работы.

Требования:
- Пользовательский ввод: Приложение должно предложить пользователю ввести данные, чтобы выбрать, какую функцию он хочет изучить.
- Проверка данных: Убедитесь, что пользовательские данные (например, даты) проверены.
- Обработка ошибок: Корректно обрабатывайте ошибки API и неверные ответы.
- Представление данных: Представляйте данные в четкой и организованной форме.
- Опция выхода: позволяет пользователям выходить из приложения в любое время.
"""

import requests
import json
from datetime import datetime


NASA_API_KEY = 'f3is16iBRgMN51hS2DT0dXfhKQgjl9nPqNH8hdc8'

def get_apod():
    url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Название: {data['title']}\n")
        print(f"Описание: {data['explanation']}\n")
        print(f"URL изображения: {data['url']}\n")
    else:
        print("Ошибка при получении APOD:", response.status_code)
    return


def get_mars_photos():
    sol = input("Введите сол (день миссии на Марсе): ")
    camera = input("Введите тип камеры (например, 'FHAZ', 'RHAZ', 'CHEMCAM' и т.д.): ")

    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&camera={camera}&api_key={NASA_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            for photo in data['photos']:
                print(f"Фото URL: {photo['img_src']}, Дата: {photo['earth_date']}")
        else:
            print("Фото не найдены по заданным параметрам.")
    else:
        print("Ошибка при получении фотографий с марсохода:", response.status_code)
    return


def get_near_earth_objects():
    date = input("Введите дату (гггг-мм-дд): ")

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Неправильный формат даты. Пожалуйста, используйте формат гггг-мм-дд.")

    url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={NASA_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for neo in data['near_earth_objects'][date]:
            name = neo['name']
            size = neo['estimated_diameter']['meters']['estimated_diameter_max']
            hazardous = 'да' if neo['is_potentially_hazardous_asteroid'] else 'нет'
            print(f"Объект: {name}, Размер: {size:.2f} м, Потенциальная опасность: {hazardous}")
    else:
        print("Ошибка при получении объектов, сближающихся с Землей:", response.status_code)
    return


def get_space_weather():
    date = input("Введите дату (гггг-мм-дд): ")

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Неправильный формат даты. Пожалуйста, используйте формат гггг-мм-дд.")
        return

    url_1 = f'https://api.nasa.gov/DONKI/FLR?startDate={date}&endDate={date}&api_key={NASA_API_KEY}'
    url_2 = f'https://api.nasa.gov/DONKI/GST?startDate={date}&endDate={date}&api_key={NASA_API_KEY}'

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)

    if response_1.status_code == 200:
        flr_data = response_1.json()
        if flr_data:
            print("Данные FLR:", flr_data)
        else:
            print("Нет данных FLR на эту дату.")
    else:
        print("Ошибка при получении данных FLR:", response_1.status_code)

    if response_2.status_code == 200:
        gst_data = response_2.json()
        if gst_data:
            print("Данные GST:", gst_data)
        else:
            print("Нет данных GST на эту дату.")
    else:
        print("Ошибка при получении данных GST:", response_2.status_code)

    return flr_data, gst_data


def main():
    while True:
        print("\nПанель управления исследованиями космоса:")
        print("1. Астрономическая картинка дня (APOD)")
        print("2. Фотографии с марсохода")
        print("3. Объекты, сближающиеся с Землей (ОСЗ)")
        print("4. Данные о космической погоде")
        print("5. Выход")

        choice = input("Выберите опцию (1-5): ")

        if choice == '1':
            get_apod()
        elif choice == '2':
            get_mars_photos()
        elif choice == '3':
            get_near_earth_objects()
        elif choice == '4':
            get_space_weather()
        elif choice == '5':
            print("Выход из приложения.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
    return


if __name__ == "__main__":
    main()

"""# Задание 2

Описание задачи

Цель этой задачи - создать скрипт на Python, который взаимодействует с API Чикагского института искусств (https://api.artic.edu/docs/) для извлечения и отображения произведений искусства. Скрипт должен позволять пользователям просматривать работы по страницам, фильтровать их по имени художника и просматривать подробную информацию о выбранных произведениях искусства. Ниже приведены требования и функциональные возможности, которые необходимо реализовать:

Требования:
Извлекать произведения искусства:

- Создайте функцию, которая извлекает список произведений искусства из API Чикагского института искусств.
Функция должна принимать параметр page для разбивки на страницы и возвращать список произведений искусства вместе с информацией о разбивке на страницы.
Фильтровать произведения искусства:

- Реализуйте функцию, которая фильтрует список произведений искусства на основе имени указанного художника. Функция должна возвращать список работ, которые соответствуют имени художника (без учета регистра).
Отображать подробную информацию об оформлении:

- Напишите функцию, которая отображает названия работ для пользователя и позволяет ему выбрать одну из них, введя соответствующий номер.
После выбора функция должна отображать подробную информацию о выбранном произведении, включая название, исполнителя, дату и носитель.
Разбивка на страницы и взаимодействие с пользователем:

- Создайте основную функцию, которая управляет выборкой произведений и взаимодействием с пользователем.

Разрешите пользователям перемещаться по страницам с произведениями искусства, выполнять фильтрацию по исполнителю или выходить из программы.

Если страниц с произведениями искусства несколько, укажите варианты перехода к следующей странице, предыдущей странице, фильтрации по исполнителю или выхода из программы.
"""

import requests


BASE_URL = "https://api.artic.edu/api/v1/artworks"

def fetch_artworks(page=1):
    params = {
        'page': page,
        'limit': 10
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data['data'], data['pagination']


def filter_artworks_by_artist(artworks, artist_name):
    return [art for art in artworks if artist_name.lower() in art.get('artist_title', '').lower()]


def display_artwork_details(artwork):
    print(f"Название: {artwork['title']}")
    print(f"Исполнитель: {artwork.get('artist_title', 'Неизвестен')}")
    print(f"Дата: {artwork.get('date_display', 'Неизвестна')}")
    print(f"Носитель и техника: {artwork.get('medium_display', 'Неизвестно')}")


def display_artworks(artworks):
    print("\nСписок произведений искусства:")
    for idx, artwork in enumerate(artworks):
        print(f"{idx + 1}. {artwork['title']} (Исполнитель: {artwork.get('artist_title', 'Неизвестен')})")


def main():
    current_page = 1
    while True:
        artworks, pagination = fetch_artworks(current_page)
        display_artworks(artworks)

        print("\nВыберите опцию:")
        print("1. Перейти к следующей странице")
        print("2. Перейти к предыдущей странице")
        print("3. Фильтровать по исполнителю")
        print("4. Выход")

        choice = input("Введите номер опции: ")

        if choice == '1':
            if current_page < pagination['total_pages']:  # Исправлено здесь
                current_page += 1
            else:
                print("Это последняя страница.")
        elif choice == '2':
            if current_page > 1:
                current_page -= 1
            else:
                print("Это первая страница.")
        elif choice == '3':
            artist_name = input("Введите имя художника: ")
            filtered_artworks = filter_artworks_by_artist(artworks, artist_name)
            if filtered_artworks:
                display_artworks(filtered_artworks)
                artwork_choice = input("Введите номер произведения для просмотра деталей: ")
                if artwork_choice.isdigit() and 1 <= int(artwork_choice) <= len(filtered_artworks):
                    display_artwork_details(filtered_artworks[int(artwork_choice) - 1])
                else:
                    print("Неверный номер.")
            else:
                print("Произведения искусства этого художника не найдены.")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    main()

"""# Задание 3

Задача: Создать программу по управлению портфелем криптовалют

Цель: Создать скрипт на Python, который извлекает цены на криптовалюты в режиме реального времени, позволяет пользователям управлять портфелем криптовалют, вычисляет общую стоимость портфеля, отслеживает изменения цен и предоставляет исторические данные о ценах для анализа.

Требования:
Получение текущих цен на криптовалюты:

Используйте https://docs.coingecko.com/ для получения актуальных цен на список криптовалют.

Управление портфелем:

- Позволяет пользователю создавать портфель криптовалют и управлять им, указывая количество каждой криптовалюты, которой он владеет.
- Расчитывает общую стоимость портфеля в указанной фиатной валюте (например, долларах США).

Отслеживание изменения цен:

- Отображение процентного изменения цены для каждой криптовалюты в портфеле за последние 24 часа.
- Выделите все криптовалюты, стоимость которых значительно увеличилась или снизилась.

Поиск исторических данных о ценах:

- Получение исторических данных о ценах на указанную криптовалюту за последнюю неделю.
- Предоставьте пользователю возможность визуализировать эти данные в простом текстовом формате (например, цены за день).

Взаимодействие с пользователем:

- Реализуйте интерфейс командной строки для ввода данных пользователем.
- Предоставьте опции для получения текущих цен, управления портфелем, просмотра изменений цен или анализа исторических данных.
"""

import requests
import json
from datetime import datetime, timedelta


class CryptoPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_crypto(self, name, amount):
        if name in self.portfolio:
            self.portfolio[name] += amount
        else:
            self.portfolio[name] = amount

    def remove_crypto(self, name, amount):
        if name in self.portfolio:
            self.portfolio[name] -= amount
            if self.portfolio[name] <= 0:
                del self.portfolio[name]
        else:
            print(f"{name} не найден в портфеле.")

    def get_total_value(self, fiat_currency='usd'):
        total_value = 0
        for crypto, amount in self.portfolio.items():
            price = self.get_current_price(crypto, fiat_currency)

            total_value += price[0] * amount
        return total_value

    def get_current_price(self, crypto_id, fiat_currency='usd'):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={fiat_currency}&include_24hr_change=true"
        response = requests.get(url)
        data = response.json()
        return data[crypto_id][fiat_currency], data[crypto_id][f'{fiat_currency}_24h_change']

    def get_historical_prices(self, crypto_id, days=7, currency='usd'):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart/range?vs_currency={currency}&from={start_date.timestamp()}&to={end_date.timestamp()}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Ошибка получения данных: {response.status_code}")
            return {}

        data = response.json()

        if 'prices' not in data:
            print(f"Ошибка в полученных данных: {data}")
            return {}

        prices = data['prices']
        historical_data = {}

        for price in prices:
            timestamp, value = price
            date = datetime.fromtimestamp(timestamp // 1000).strftime('%Y-%m-%d')  # делим на 1000, так как API возвращает время в мс
            historical_data[date] = value

        return historical_data

    def display_portfolio(self):
        print("Ваш портфель:")
        for crypto, amount in self.portfolio.items():
            current_price, change = self.get_current_price(crypto)
            print(f"{crypto.capitalize()}: {amount} (Текущая цена: {current_price}$, Изменение за 24 часа: {change}% )")
        print(f"Общая стоимость портфеля: {self.get_total_value()}$")


def main():
    portfolio = CryptoPortfolio()

    while True:
        print("\n1. Добавить криптовалюту")
        print("2. Удалить криптовалюту")
        print("3. Показать портфель")
        print("4. Получить исторические данные")
        print("5. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            crypto_name = input("Введите имя криптовалюты: ").strip().lower()
            amount = float(input("Введите количество: "))
            portfolio.add_crypto(crypto_name, amount)

        elif choice == '2':
            crypto_name = input("Введите имя криптовалюты для удаления: ").strip().lower()
            amount = float(input("Введите количество для удаления: "))
            portfolio.remove_crypto(crypto_name, amount)

        elif choice == '3':
            portfolio.display_portfolio()

        elif choice == '4':
            crypto_name = input("Введите имя криптовалюты для анализа: ").strip().lower()
            historical_prices = portfolio.get_historical_prices(crypto_name)
            print("Исторические данные (цены за последние 7 дней):")
            for date, price in historical_prices.items():
                print(f"{date}: {price}$")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()

"""# Дополнительно: Задание 4

Задание 4: Проектное

Вам необходимо самостоятельно найти откртое API предоставляющее информацию в открытом доступе и реализовать собственный проект!


Критерии приемки результата:

- Проект включает в себя не менее 5 возможостей для пользователя
- Проект позволяет использовать все возможности проекта пользователю при помощи взаимодействия через коммандную строку
- Проект работает с открытым API (это значит что при проверке вашей работы преподавателем, преподавателю необходимо просто запустить ячейку с кодом вашего проекта и она будет работать без дополнительных манипуляции)
- Проект должен обязательно включать в себя ряд используемых конструкции:
    - Функции
    - Условные конструкции
    - Ввод/вывод
    - Словари/Списки
- Допускается использование библиотек:
    - requests
    - datetime
    - random

**Здесь добавьте описание вашего проекта**
"""

#  А здесь код