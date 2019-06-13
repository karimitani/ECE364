
class Course:
    """
    A Class that holds the some information about a school course.
    """

    _validDepartments = ["ECE", "ME", "ENM"]

    department = ""
    creditHours = 1

    def fun(self, *args):
        pass

    def fun1(self, **kwargs):
        pass


    def __init__(self, title, number, department, creditHours=3):
        """
        The constructor!. Initialize instance variables.
        """

        self.fun(1, 2, 3, 4, "a")
        self.fun1(someVar="", av=2, )


        self._validateDepartment(department)
        self._validateCreditHours(creditHours)

        self.number = number
        self.title = title


    def getCourseInfo(self):
        """
        Return the course info in a tuple.
        """

        return self.department, self.number, self.title, self.creditHours


    def _validateDepartment(self, department):
        """
        Validates the department string to be one of the acceptable ones.
        """

        if department not in self._validDepartments:
            raise ValueError("Department entered is not valid.")

        self.department = department


    def _validateCreditHours(self, creditHours):
        """
        Validates the credit hours to be between 1 & 4.
        """

        if creditHours < 1 or creditHours > 4:
            raise ValueError("Credit hours must be between 1 and 4.")

        self.creditHours = creditHours
