def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func