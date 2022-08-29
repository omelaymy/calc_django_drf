## Ипотечный калькулятор
- - -
### Пользовательский сценарий

Клиент вводит следующие данные:

- Стоимость объекта недвижимости, в рублях без копеек 
- Первоначальный взнос, в рублях без копеек
- Срок кредита в годах

В ответ ему приходит массив с объектами ипотечных предложений. В каждом объекте есть следующие данные:
- Наименование банка
- Ипотечная ставка, в процентах
- Платеж по ипотеке, в рублях без копеек

### Локальный запуск приложения
**Клонировать репозиторий с Github** 
- ssh: git@github.com:omelaymy/calc_django_drf.git
- hhtps: [project on github](https://github.com/omelaymy/calc_django_drf.git)
- - -


**Перейти в директорию проекта**

**Поднять контейнеры** 

`sudo docker-compose up -d`

**Остановить контейнеры**

`sudo docker-compose stop`
- - -
Сервис буден доступен по ссылкам:

- С простой html формой: http://localhost:8000/calc/ 

- С drf: http://localhost:8000/calc/offer/ 

- Create http://localhost:8000/calc/api/
- Read, Update, Delete http://localhost:8000/calc/api/ + bank_id/
- - - 
**Суперпользователь для http://localhost:8000/admin**

admin

roiadmin