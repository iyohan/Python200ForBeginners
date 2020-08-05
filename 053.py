class MyClass:
    def __del__(self):
        print('MyClass instance object gets removed from memory')

obj = MyClass()
del obj