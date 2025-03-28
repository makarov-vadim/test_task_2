from random import randint


def get_post_code():
    '''Функция, возвращающая строку, состоящую из 10 случайных цифр для поля "Post Code"'''
    return ''.join([str(randint(0, 9)) for _ in range(10)])

def get_first_name(post_code: str):
    '''Функция, возвращающая строку, состоящую из 5 букв для поля "First Name"'''
    nums = map(int, map(''.join, zip(*([iter(post_code)] * 2))))
    first_name = ''.join(chr(97 + num % 26) for num in nums)
    return first_name

def get_name_to_delete(names:list[str]) -> str:
    '''Функция, возвращающая элемент списка (строку), который имеет длину равную
    среднему арифметическому длин всех элементов"'''
    avg_len = sum(map(len, names)) / len(names)
    sorted_names = sorted(names, key=lambda i: abs(avg_len - len(i)), reverse=True)
    return sorted_names.pop()