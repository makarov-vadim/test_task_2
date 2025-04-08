# Тест-кейс 1. Создание клиента (Add Customer)

## Предусловие:  
Открыт объект тестирования  
https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager

## Шаги:  
1. Клик по вкладке Add "Customer";  
2. Ввод данных в поля "First Name", "Last Name", "Post Code" по следующим правилам:  
 -- для поля "Post Code" сгенерировать номер из 10 цифр;  
 -- для поля "First Name" сгенерировать имя на основе Post Code (Post Code условно разбить на 5 двузначных чисел, каждое из которых преобразовать в букву английского алфавита по порядку от 0 до 25);  
3. Клик по кнопке "Add Customer".

## Ожидаемый результат:  
1. Появится форма с полями "First Name", "Last Name", "Post Code";  
2. Данные в поля "First Name", "Last Name", "Post Code" будут введены;  
3. Появится всплывающее окно с текстом "Customer added successfully..."  
