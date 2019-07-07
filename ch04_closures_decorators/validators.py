def check_non_negative(index):
    print('index = {}'.format( index))
    def validator(f):
        def wrap(*args):
            print('args start')
            for a in args:
                print(a)
            print('args end')
            if args[index] < 0:
                raise ValueError('Argument {} must be non negative'.format(index))
            result = f(*args)
            print("result = {}".format(result))
            return result
        return wrap
    return validator

@check_non_negative(1)
def create_list(value, size):
    return [value] * size