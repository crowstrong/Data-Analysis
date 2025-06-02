def debug(func):
    """Декоратор для логування інформації про функцію"""
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@debug
def get_even(numbers: list) -> list:
     """повертає список лише парних чисел із заданого списку чисел"""
     return [num for num in numbers if num % 2 == 0]

@debug  
def make_multiplier(factor: int) -> callable: 
    """Повертає функцію, яка множить число на заданий множник"""
    def multiplier(x):
        return x * factor
    return multiplier

def check_positive(func):
    def wrapper(*args, **kwargs):
        """Перевіряє, що усі числові аргументи більші за 0, інакше піднімає ValueError."""
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Усі числові аргументи повинні бути більше за 0")
        
        return func(*args, **kwargs)
    
    return wrapper

@check_positive
def multiply(a, b):
    return a * b

def safe_divide(a, b):
    """Ділення з перевіркою на нуль"""
    if b == 0:
        return "division by zero"
    return a / b

def  get_int_input(prompt: str) -> int:
    """Функція для отримання цілочисельного вводу від користувача з обробкою помилок"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")

def error_hendler(func):
    """Декоратор для обробки помилок"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка: {e}")
            return None
    return wrapper

@error_hendler
def risky_function(x):
    """Приклад функції, яка може викликати помилку"""
    return 10 / x

if __name__ == "__main__":
    # Приклад використання
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = get_even(numbers)
    print(even_numbers)  # Виведе: [2, 4, 6, 8, 10] 

    double = make_multiplier(2)
    print(double(5))  # Виведе: 10

    print(multiply(5, 3))   # OK
    # print(multiply(-2, 4))  # ValueError

    print(safe_divide(10, 2))   # 5.0
    print(safe_divide(10, 0))   # "division by zero"

    #user_input = get_int_input("Введіть ціле число: ")
    #print(f"Ви ввели: {user_input}")  # Виведе введене число3

    print(risky_function(2))  # Виведе: 5.0
    print(risky_function(0))  # Виведе: Помилка: division by zero
    print(risky_function("a"))  # Виведе: Помилка: unsupported operand type(s) for /: 'int' and 'str'
    print(risky_function([]))  # Виведе: Помилка: division by zero
    print(risky_function(None))  # Виведе: Помилка: unsupported operand type(s) for /: 'int' and 'NoneType'
    print(risky_function())  # Виведе: Помилка: risky_function() missing 1 required positional argument: 'x'
    print(risky_function(1, 2))  # Виведе: Помилка: risky_function() takes 1 positional argument but 2 were given 