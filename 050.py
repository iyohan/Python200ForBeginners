class MyClass:
    var = 'hello'
    def sayHello(self):
        param1 = 'hi'
        self.param2 = 'hiii'
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()
#obj.param1
#Myclass.var 