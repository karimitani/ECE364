from Course import Course

class PurdueStudent:
    """
    A Class that a student at Purdue.
    """

    def __init__(self, firstName, lastName, gender, hasLongHair=True):
        """
        Initialize instance variables.
        """

        self._courseList = []

        # Validate names are not empty.
        if not firstName:
            raise ValueError('First name cannot be empty.')

        self.firstName = firstName
        self.lastName = lastName
        self.hasLongHair = hasLongHair

        if not self._validateGender(gender):
            raise ValueError("Gender provided not allowed.")

        self.gender = gender
        self.pronoun = "she" if self.gender is "female" else "he"


    def printInfo(self):
        """
        Print a properly formatted string of the name and the course work.
        """

        about = "Student name is {0}, {1}, and {2} is taking {3}.".format(
                 self.lastName, self.firstName, self.pronoun, len(self._courseList))

        print(about)


    # def addCourse(self, title, number, department, creditHours):
    #     """
    #     Add a course to the student course list.
    #     """
    #     pass

    def addCourse(self, someCourse):
        """
        Add a course to the student course list.
        """

        courseTuple = someCourse.getCourseInfo()
        self._courseList.append(courseTuple)

    def _validateGender(self, gender):
        """
        Validate gender to be a male, female or unspecified.
        """

        valid = ["male", "female", "unspecified"]

        return gender in valid

    def isGraduatingSoon(self):
        """
        As the name suggests.
        """

        if self.hasLongHair:
            print("Student has long hair, so 'Yes' {} is graduating.".format(self.pronoun))



class GraduateStudent(PurdueStudent):
    """
    A Class that holds some information about graduate students.
    """

    isGraduate = True

    def isGraduatingSoon(self):
        """
        As the name suggests.
        """

        if self.hasLongHair:
            print("Student has long hair, so, of course NOT!")
