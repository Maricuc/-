import time
from datetime import datetime

def log_args(func):
    """декоратор, записывающий в файл информацию о вызове функции"""
    def wrapper(*args,**kwargs):                                     # Функция-обёртка, принимает любые аргументы
        call_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")    # Получаем текущее время в нужном формате
        result=func(*args, **kwargs)                               # Вызываем оригинальную функцию с её аргументами
        
        with open('log.txt','a', encoding='utf-8') as f:           # Открываем файл для добавления записи
            f.write(f"время:{call_time}\n")                         # Записываем время вызова
            f.write(f"имя функции:{func.__name__}\n")              # Записываем имя функции
            f.write(f"аргументы:{args}\n")                          # Записываем переданные аргументы
            f.write(f"возвращаемое значение: {result}\n")           # Записываем результат работы функции
            f.write("-"*40 +"\n")                                 # Разделитель для читаемости
        
        return result                                                # Возвращаем результат оригинальной функции
    return wrapper                                                   # Возвращаем функцию-обёртку

@log_args                                                            # Применяем декоратор к функции calculate_sum
def calculate_sum(n):
    """вычисляет сумму списка"""
    return sum(n)                                                    # Возвращаем сумму всех элементов списка


my_list=[1,2,3,4,5]                                           # Создаём список чисел
result=calculate_sum(my_list)                                      # Вызываем декорированную функцию
print(f"сум списка {my_list}={result}")                      
print("лог сохранен в файл log.txt\n")                              

