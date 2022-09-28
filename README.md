# Click&Eat

Cashier is in your browser!

![main](/imgs/welcome.jpg?raw=true)

This service allows you to make a self-delivery order from cafes and restaurants.\
Restaurants are making a menu and mark on a map there's location as they register.\
User chooses the restaurant from a list(sorting is possible) or a map, fills the bucket and make an order.\
Immediately restaurant gets the information from user about his order and can change it's status.\
User names the secrete pin code to get an order from cashier.

## Ordering process
![Ordering process](/imgs/user_process.gif?raw=true)

## Monitor of order
For a user's convenience restaurant can mount a monitor(any gadget) of orders.\

As well there is a possibility of installing a self-service terminal in the restaurant.\
Также возможна установка киосков для самостоятельных заказов в заведениях.
![Monitor of orders](/imgs/monitor.gif?raw=true)

## Launch of a project 

- Create and activate a virtual environment:
```
# python -m venv venv

Unix or MacOS:
# source venv/bin/activate

Windows:
CMD: # venv\Scripts\activate.bat
PowerShell: # venv\Scripts\Activate.ps1
```
- Install dependencies:
```
# pip install -r requirements.txt
```

- Project configuration:\
Require to state a token of Yandex.Maps in a file [settings.py](/server/server/settings.py) in a dict MAPS_CONFIG in a pole API_KEY.

- Database initialization:
```
# python server/manage.py migrate
```

- Server launch:
```
python server/manage.py runserver
```
