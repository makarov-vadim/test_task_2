# Тест-кейс 2. Тестирование точки доступа GETALL (Получение всех сущностей)

## Предусловия:  
0.1. Запущен сервис:  
- https://github.com/bondarenkokate73/simbirsoft_sdet_project  
- HOST http://localhost:8080  
- SWAGGER документация http://localhost:8080/api/_/docs/swagger/

0.2. Удаление всех сущностей (для независимой работы всех тест-кейсов)  


## Шаги:  
1. Создание нескольких сущностей и их запись
2. Получение всех сущностей  
3. Удаление созданных сущностей  

## Ожидаемый результат:  
Шаг 1. Созданные сущности записываются в словарь (ключ - id сущности, значение - сущность)

Шаг 2.
- Код статуса запроса 200
- Созданные сущности присутствуют в ответе на запрос  

Шаг 3. Созданные сущности удаляются по id


## Постусловия:  
4. Удаление всех сущностей (для независимой работы всех тест-кейсов)
