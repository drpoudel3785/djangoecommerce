class C(object):
    def __init__(self):
        self.c = 21

        # d is private instance variable
        #We can make an private instance variable by adding double underscores before its name
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)


object1 = D()
#to
# produces an error as d is private instance variable
print(object1.c)
print(object1.d)
