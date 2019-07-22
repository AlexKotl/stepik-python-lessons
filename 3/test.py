class A:
    __var_1 = 1

    def __init__(self):
        self.var_3 = 3

    def get_var_3(self):
        return self

    def get_cls(cls):
        return cls
        
    def get_v(self):
        return self.__var_1
        
class B(A):
    pass

a = A()
b = B()

print(b.get_var_3())