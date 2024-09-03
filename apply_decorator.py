def apply_decorator(func):
    def wrapper(*args, **kwrags):
        print('Decorator applied')
        return func(*args,**kwrags)
    return wrapper
def decorator_func(func):
    return apply_decorator(func)
def day():
    print('learning is awesome')
    #application of the decorator
    @apply_decorator
    def this_function():
     print("Original Function Called")

    this_function()
