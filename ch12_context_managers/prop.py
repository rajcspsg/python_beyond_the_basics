import contextlib
import sys

@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception as e:
        print(name, 'received an excetion {}'.format( e.__str__))
        if propagate:
            raise
        
def run():
    with propagater('outer', False), propagater('inner', True):
        raise TypeError('Cannot convert lead into gold!!!')
    
if __name__ =='__main__':
    run()