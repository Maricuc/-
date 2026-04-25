import time
import functools

def timing_decorator(func):
    """Декоратор, который измеряет время выполнения функции"""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()          # Время до вызова
        result = func(*args, **kwargs)    # Вызов функции
        end_time = time.time()            # Время после вызова
        
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнялась {execution_time:.10f} секунд")
        
        return result
    
    return wrapper


@timing_decorator
def calculate_sum(numbers):
    """Вычисляет сумму списка"""
    return sum(numbers)


# Тестирование
my_list = [1557577577, 23635, 3353553, 43838, -5676666]
print("Сумма:", calculate_sum(my_list))

# Дополнительный тест с большим списком
big_list = list(range(1_000_000))
print("Сумма большого списка:", calculate_sum(big_list))