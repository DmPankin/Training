
def test(*args):
    for v in args:
        print(v)


test(1,2,'кит',('e', 'q', 5))

def test(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')


test(a=1,b=2,c='кит',d=('e', 'q', 5))