
def decorate_display(func):
    def inner_display():
        print("Before")
        func()
        print("After")
    return inner_display

@decorate_display
def display():
    print("Welcome")

display()
