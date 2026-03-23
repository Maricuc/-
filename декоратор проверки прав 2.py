import time
from datetime import datetime


users = {                                                            # Словарь с пользователями и их ролями
    'alice': {'role': 'admin'},                                      # У alice роль admin
    'bob': {'role': 'user'},                                         # У bob роль user
    'eve': {'role': 'guest'}                                         # У eve роль guest
}

def require_role(required_role):
    """декоратор проверки прав доступа"""
    def decorator(func):                                             # Внутренняя функция-декоратор
        def wrapper(*args, **kwargs):                                # Функция-обёртка
            user=kwargs.get('user',{})                            # Получаем пользователя из kwargs, если нет - пустой словарь
            if user.get('role')==required_role:                    # Проверяем, совпадает ли роль пользователя с требуемой
                return func(*args,**kwargs)                         # Если да — выполняем оригинальную функцию
            else:                                                     # Если роль не совпадает
                return f"доступ запрещен.Требуется роль:{required_role}"  # Возвращаем сообщение об отказе
        return wrapper                                                # Возвращаем обёртку
    return decorator                                                  # Возвращаем декоратор

@require_role('admin')                                                # Применяем декоратор с требованием роли admin
def delete_database(db_name, user=None):                             # Функция удаления базы данных
    return f"база {db_name} удалена!"                                # Возвращаем сообщение об успешном удалении


# проверка для пользователя bob (роль user)
current_user='bob'                                                 # Устанавливаем текущего пользователя
result=delete_database('test_db', user=users[current_user])       # Пытаемся удалить базу
print(f"{current_user}:{result}")                                   # Должно вывести сообщение об отказе

# проверка для пользователя alice (роль admin)
current_user='alice'                                               # Меняем пользователя
result = delete_database('test_db', user=users[current_user])       # Снова пытаемся удалить базу
print(f"{current_user}:{result}")                                   # Должно вывести сообщение об успехе