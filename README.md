<h1 align="center">SocProofAPI</h1>

SocProofAPI - библиотека для облегченного использования сервиса soc-proof.su

## Установка
Стабильная версия через GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/socproofapi/archive/main.zip --upgrade
   ```
   
## Пример использования
```python
from SocProofAPI import SocProofAPI

api = SocProofAPI('API_KEY')
print(api.balance())
```

## Методы
```.services()``` - Метод возвращает массив объектов со списком услуг

```.balance()``` - Возвращает баланс аккаунта

```.add_order()``` - Создание заказа
- service - номер сервиса
- link - ссылка
- quantity - количество

```.cancel_order()``` - Отменить заказ
- order - ID заказа

```.order_status()``` - Статус заказа
- order - ID заказа
