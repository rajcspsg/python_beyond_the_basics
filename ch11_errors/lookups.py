def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except IndexError:
        print('Handled Index error')
        
    d = dict(a = 65, b = 66, c = 67)
    
    try:
        d['x']
    except KeyError:
        print('Handled KeyError')
        
        
if __name__ == '__main__':
    lookups()