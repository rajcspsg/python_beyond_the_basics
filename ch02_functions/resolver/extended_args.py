def hypervolume(length, *lengths):
    v = length
    for l in lengths:
        v *= l
    return v

def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))
    
# __all__ = ['hypervolume', 'tag']

def color(red, blue, green, **kwargs):
    print("r = ", red)
    print("blue = ", blue)
    print("green = ", green)
    print("kwargs = ", kwargs)