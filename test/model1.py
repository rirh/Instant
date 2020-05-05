print('model one')
if (__name__ == '__main__'):
    print('model one main')


def fun1(args='', **anys):
    print('''这是args ''', args, anys)
    print('fun1')


class Foo:
    def __init__(self):
        print('init')
        super().__init__()

    def foo(self, args):
        print('foo',args)
