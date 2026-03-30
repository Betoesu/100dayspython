import time

#Pode Alterar ou adicionar coisas antes ou depois da função
def delay_decorator(func):
    def wrapper_function():
        time.sleep(2)
        func()
        func()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

def say_greetings():
    print("How are you?")

say_hello()