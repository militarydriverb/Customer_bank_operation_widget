from functools import wraps


def log(filename=None):
    """Декоратор автоматический логирующий начало и конец выполнения функции,
    а так же результаты или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Функция {name_func} ok. Результат: {result}" + "\n")
                    file.close()
                else:
                    print(f'{name_func} ok. Результат: {func(*args, **kwargs)}')
            except Exception as e:
                result = None
                print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


my_function(1, 5)
