import os

class MyClass:

    # Special methods.
    def __init__(self, someVar):
        # This is preferred location to define AND initialize member variables, especially reference variables,
        # like lists, dicts, sets.

        # Attributes -- Member Variables -- fields -- properties
        self._backingStore = 0
        self.userCount = 0
        self.someVar = someVar
        pass

    def __str__(self):
        pass

    # operator Overloads.
    def __add__(self):
        pass

    def __eq__(self):
        pass

    # Methods, or Member functions. Public & Private.
    def addUser(self, userName):
        pass
        
    def _processUser(self, userName):
        pass
        
    
class AnotherClass(MyClass):

    # Special methods.
    def __init__(self, newVar):

        self.newVar = newVar

        MyClass.__init__(self, newVar)
        # OR
        # super().__init__(newVar)

        pass
