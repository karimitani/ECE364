class Parent:

    def __init__(self):
        self.local = 0

    def method1(self):
        print('Method 1 in Base')

    def method2(self):
        print('Method 2 in Base')

    def selectMethod(self, num):

        if num == 1:
            self.method1()
        elif num == 2:
            self.method2()

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.local1 = 0

    def method1(self):
        print('Method 1 in Child')

    def method2(self):
        print('Method 2 in Child')

