# Тест-кейс 1. Тестирование точки доступа GET (Получение сущности)

## Предусловия:  
0.1. Запущен сервис:  
- https://github.com/bondarenkokate73/simbirsoft_sdet_project  
- HOST http://localhost:8080  
- SWAGGER документация http://localhost:8080/api/_/docs/swagger/

0.2. Удаление всех сущностей (для независимой работы всех тест-кейсов)  


## Шаги:  
1. Создание сущности
2. Получение созданной сущности по id.  
3. Удаление созданной сущности  

## Ожидаемый результат:  
Шаг 1. Сущность создана, получен ее id  

Шаг 2.
- Код статуса запроса 200
- Соответствие id созданной и полученной сущности  

Шаг 3. Созданная сущность удалена по id


## Постусловия:  
4. Удаление всех сущностей (для независимой работы всех тест-кейсов)
