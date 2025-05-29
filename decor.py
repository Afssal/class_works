def greet(func):

    def wrapper():
        print("Hello")
        func()
        print("How are you")
    return wrapper

@greet
def say():
    print("Afzal")

print(say())