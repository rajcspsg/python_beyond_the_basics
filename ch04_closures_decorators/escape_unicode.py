def escape_unicode(f):
    def wrap(*args, **kwargs):
        # print("*args = "+ args)
        # print("**kwargs "+kwargs)
        print("args start")
        for arg in args:
            print("arg = "+ arg)
        print("args end")
        print("keyvalue")
        for k,v in kwargs:
            print('k = ' +k + ' v ='+ v)
        print('kwargs end')
        x = f(*args, **kwargs)
        print("x = " +x)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    return 'Troms0'