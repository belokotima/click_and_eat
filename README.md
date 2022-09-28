# Click&Eat

Cashier is in your browser!

![Главная](/imgs/welcome.jpg?raw=true)

This service allows you to make a self-delivery order from cafes and restaurants.\
Institutions are making a menu and post address  
Заведения размещают на сервисе меню и указывают адреса заведений.\
Пользователь выбирает ресторан из списка (возможна сортировка по категориям) или на карте, набирает корзину из необходимых позиций и оформляет заказ.\
Сразу после оформления заказа, ресторан получает информацию о заказе и может обновлять его статус.\
Чтобы получить свой заказ, пользователь называет персоналу номер своего заказа и уникальный пин-код.

## Процесс заказа
![Процесс заказа](/imgs/user_process.gif?raw=true)

## Монитор заказов
Для удобства посетителей заведение может установить монитор заказов.\
Также возможна установка киосков для самостоятельных заказов в заведениях.\
![Монитор заказов](/imgs/monitor.gif?raw=true)

## Запуск проекта

- Создание и активация виртуального окружения:
```
# python -m venv venv

Unix or MacOS:
# source venv/bin/activate

Windows:
CMD: # venv\Scripts\activate.bat
PowerShell: # venv\Scripts\Activate.ps1
```
- Установка зависимостей:
```
# pip install -r requirements.txt
```

- Конфигурация проекта:\
Необходимо указать токен Яндекс.Карт в файле [settings.py](/server/server/settings.py) в словаре MAPS_CONFIG в поле API_KEY.

- Инициализация БД:
```
# python server/manage.py migrate
```

- Запуск сервера:
```
python server/manage.py runserver
```
