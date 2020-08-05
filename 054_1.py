class Add:
    def add(self, n1, n2):
        return n1+n2

class Multiply:
    def mul(self, n1, n2):
        return n1*n2

class Calculator(Add, Multiply):
    def sub(self, n1, n2):
        return n1-n2

obj = Calculator()
print(boj.add(1, 2))
print(obj.mul(3, 2))