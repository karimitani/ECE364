import sys
import re

from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        #clear button clicked
        self.btnClear.clicked.connect(self.clear)

        #save button clicked
        self.btnSave.clicked.connect(self.save)

        #load button clicked
        self.btnLoad.clicked.connect(self.loadData)

        #text entered in any box
        self.txtStudentName.textChanged.connect(self.saveEnable)
        self.txtStudentID.textChanged.connect(self.saveEnable)
        self.chkGraduate.stateChanged.connect(self.saveEnable)
        self.cboCollege.currentIndexChanged.connect(self.saveEnable)

        self.txtComponentName_1.textChanged.connect(self.saveEnable)
        self.txtComponentName_2.textChanged.connect(self.saveEnable)
        self.txtComponentName_3.textChanged.connect(self.saveEnable)
        self.txtComponentName_4.textChanged.connect(self.saveEnable)
        self.txtComponentName_5.textChanged.connect(self.saveEnable)
        self.txtComponentName_6.textChanged.connect(self.saveEnable)
        self.txtComponentName_7.textChanged.connect(self.saveEnable)
        self.txtComponentName_8.textChanged.connect(self.saveEnable)
        self.txtComponentName_9.textChanged.connect(self.saveEnable)
        self.txtComponentName_10.textChanged.connect(self.saveEnable)
        self.txtComponentName_11.textChanged.connect(self.saveEnable)
        self.txtComponentName_12.textChanged.connect(self.saveEnable)
        self.txtComponentName_13.textChanged.connect(self.saveEnable)
        self.txtComponentName_14.textChanged.connect(self.saveEnable)
        self.txtComponentName_15.textChanged.connect(self.saveEnable)
        self.txtComponentName_16.textChanged.connect(self.saveEnable)
        self.txtComponentName_17.textChanged.connect(self.saveEnable)
        self.txtComponentName_18.textChanged.connect(self.saveEnable)
        self.txtComponentName_19.textChanged.connect(self.saveEnable)
        self.txtComponentName_20.textChanged.connect(self.saveEnable)

        self.txtComponentCount_1.textChanged.connect(self.saveEnable)
        self.txtComponentCount_2.textChanged.connect(self.saveEnable)
        self.txtComponentCount_3.textChanged.connect(self.saveEnable)
        self.txtComponentCount_4.textChanged.connect(self.saveEnable)
        self.txtComponentCount_5.textChanged.connect(self.saveEnable)
        self.txtComponentCount_6.textChanged.connect(self.saveEnable)
        self.txtComponentCount_7.textChanged.connect(self.saveEnable)
        self.txtComponentCount_8.textChanged.connect(self.saveEnable)
        self.txtComponentCount_9.textChanged.connect(self.saveEnable)
        self.txtComponentCount_10.textChanged.connect(self.saveEnable)
        self.txtComponentCount_11.textChanged.connect(self.saveEnable)
        self.txtComponentCount_12.textChanged.connect(self.saveEnable)
        self.txtComponentCount_13.textChanged.connect(self.saveEnable)
        self.txtComponentCount_14.textChanged.connect(self.saveEnable)
        self.txtComponentCount_15.textChanged.connect(self.saveEnable)
        self.txtComponentCount_16.textChanged.connect(self.saveEnable)
        self.txtComponentCount_17.textChanged.connect(self.saveEnable)
        self.txtComponentCount_18.textChanged.connect(self.saveEnable)
        self.txtComponentCount_19.textChanged.connect(self.saveEnable)
        self.txtComponentCount_20.textChanged.connect(self.saveEnable)

    def saveEnable(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setDisabled(True)

    def clear(self):
        self.txtStudentName.setText("")
        self.txtStudentID.setText("")
        self.chkGraduate.setChecked(False)
        self.cboCollege.setCurrentIndex(0)

        self.txtComponentName_1.setText("")
        self.txtComponentName_2.setText("")
        self.txtComponentName_3.setText("")
        self.txtComponentName_4.setText("")
        self.txtComponentName_5.setText("")
        self.txtComponentName_6.setText("")
        self.txtComponentName_7.setText("")
        self.txtComponentName_8.setText("")
        self.txtComponentName_9.setText("")
        self.txtComponentName_10.setText("")
        self.txtComponentName_11.setText("")
        self.txtComponentName_12.setText("")
        self.txtComponentName_13.setText("")
        self.txtComponentName_14.setText("")
        self.txtComponentName_15.setText("")
        self.txtComponentName_16.setText("")
        self.txtComponentName_17.setText("")
        self.txtComponentName_18.setText("")
        self.txtComponentName_19.setText("")
        self.txtComponentName_20.setText("")

        self.txtComponentCount_1.setText("")
        self.txtComponentCount_2.setText("")
        self.txtComponentCount_3.setText("")
        self.txtComponentCount_4.setText("")
        self.txtComponentCount_5.setText("")
        self.txtComponentCount_6.setText("")
        self.txtComponentCount_7.setText("")
        self.txtComponentCount_8.setText("")
        self.txtComponentCount_9.setText("")
        self.txtComponentCount_10.setText("")
        self.txtComponentCount_11.setText("")
        self.txtComponentCount_12.setText("")
        self.txtComponentCount_13.setText("")
        self.txtComponentCount_14.setText("")
        self.txtComponentCount_15.setText("")
        self.txtComponentCount_16.setText("")
        self.txtComponentCount_17.setText("")
        self.txtComponentCount_18.setText("")
        self.txtComponentCount_19.setText("")
        self.txtComponentCount_20.setText("")

        self.btnSave.setDisabled(True)
        self.btnLoad.setEnabled(True)


    def save(self):
        with open("target.xml", 'w') as wFile:
            wFile.writelines("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            wFile.writelines("<Content>\n")

            if (self.chkGraduate.isChecked()):
                graduate = "true"
            else:
                graduate = 'false'
            wFile.writelines("\t<StudentName graduate=\"{}\">{}</StudentName>\n".format(graduate, self.txtStudentName.text()))
            wFile.writelines("\t<StudentID>{}</StudentID>\n".format(self.txtStudentID.text()))

            colleges = ["-----", "Aerospace Engineering", "Civil Engineering", "Computer Engineering", "Electrical Engineering", "Industrial Engineering", "Mechanical Engineering"]
            wFile.writelines("\t<College>{}</College>\n".format(colleges[self.cboCollege.currentIndex()]))
            wFile.writelines("\t<Components>\n")

            if (self.txtComponentName_1.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_1.text(), self.txtComponentCount_1.text()))
            if (self.txtComponentName_2.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_2.text(), self.txtComponentCount_2.text()))
            if (self.txtComponentName_3.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_3.text(), self.txtComponentCount_3.text()))
            if (self.txtComponentName_4.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_4.text(), self.txtComponentCount_4.text()))
            if (self.txtComponentName_5.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_5.text(), self.txtComponentCount_5.text()))
            if (self.txtComponentName_6.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_6.text(), self.txtComponentCount_6.text()))
            if (self.txtComponentName_7.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_7.text(), self.txtComponentCount_7.text()))
            if (self.txtComponentName_8.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_8.text(), self.txtComponentCount_8.text()))
            if (self.txtComponentName_9.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_9.text(), self.txtComponentCount_9.text()))
            if (self.txtComponentName_10.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_10.text(), self.txtComponentCount_10.text()))
            if (self.txtComponentName_11.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_11.text(), self.txtComponentCount_11.text()))
            if (self.txtComponentName_12.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_12.text(), self.txtComponentCount_12.text()))
            if (self.txtComponentName_13.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_13.text(), self.txtComponentCount_13.text()))
            if (self.txtComponentName_14.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_14.text(), self.txtComponentCount_14.text()))
            if (self.txtComponentName_15.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_15.text(), self.txtComponentCount_15.text()))
            if (self.txtComponentName_16.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_16.text(), self.txtComponentCount_16.text()))
            if (self.txtComponentName_17.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_17.text(), self.txtComponentCount_17.text()))
            if (self.txtComponentName_18.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_18.text(), self.txtComponentCount_18.text()))
            if (self.txtComponentName_19.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_19.text(), self.txtComponentCount_19.text()))
            if (self.txtComponentName_20.text() != ""):
                wFile.writelines("\t\t<Component name=\"{}\" count=\"{}\" />\n".format(self.txtComponentName_20.text(), self.txtComponentCount_20.text()))

            wFile.writelines("\t</Components>\n")
            wFile.writelines("</Content>\n")


    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        * YOU MUST USE THIS METHOD TO LOAD DATA FILES. *
        * This method is required for unit tests! *
        """

        with open (filePath, 'r') as file:
            lines = file.readlines()


        nameLine = lines[2]
        IDLine = lines[3]
        collegeLine = lines[4]

        nameComps = nameLine.split()
        IDComps = IDLine.split()
        collegeComps = collegeLine.split()

        #print (nameComps)
        #print (IDComps)
        #print (collegeComps)

        regex1 = r"graduate=\"([truefalseTF]+)\">([\w]+)"
        regex2 = r"([\w]+)</StudentName>"

        m1 = re.search(regex1, nameComps[1])
        m2 = re.search(regex2, nameComps[2])

        firstName = m1.group(2)
        lastName = m2.group(1)
        name = firstName + " " + lastName
        #print (name)

        gradStatus = m1.group(1)
        #print (gradStatus)

        regex3 = r"<StudentID>([\w-]+)</StudentID>"
        m3 = re.search(regex3, IDComps[0])
        ID = m3.group(1)
        #print (ID)

        regex4 = r"<College>([\w]+)"
        m4 = re.search(regex4, collegeComps[0])
        temp1 = m4.group(1)
        regex5 = r"([\w]+)</College>"
        m5 = re.search(regex5, collegeComps[1])
        temp2 = m5.group(1)

        college = temp1 + " " + temp2
        #print (college)

        self.txtStudentName.setText(name)
        self.txtStudentID.setText(ID)
        if (gradStatus == "true" or gradStatus == "True"):
            self.chkGraduate.setChecked(True)
        else:
            self.chkGraduate.setChecked(False)
        colleges = ["-----", "Aerospace Engineering", "Civil Engineering", "Computer Engineering", "Electrical Engineering", "Industrial Engineering", "Mechanical Engineering"]
        l = len(colleges)
        for i in range(0, l):
            if (college == colleges[i]):
                ind = i
        self.cboCollege.setCurrentIndex(ind)

        components = [self.txtComponentName_1,
                      self.txtComponentName_2,
                      self.txtComponentName_3,
                      self.txtComponentName_4,
                      self.txtComponentName_5,
                      self.txtComponentName_6,
                      self.txtComponentName_7,
                      self.txtComponentName_8,
                      self.txtComponentName_9,
                      self.txtComponentName_10,
                      self.txtComponentName_11,
                      self.txtComponentName_12,
                      self.txtComponentName_13,
                      self.txtComponentName_14,
                      self.txtComponentName_15,
                      self.txtComponentName_16,
                      self.txtComponentName_17,
                      self.txtComponentName_18,
                      self.txtComponentName_19,
                      self.txtComponentName_20,]

        counts = [self.txtComponentCount_1,
                  self.txtComponentCount_2,
                  self.txtComponentCount_3,
                  self.txtComponentCount_4,
                  self.txtComponentCount_5,
                  self.txtComponentCount_6,
                  self.txtComponentCount_7,
                  self.txtComponentCount_8,
                  self.txtComponentCount_9,
                  self.txtComponentCount_10,
                  self.txtComponentCount_11,
                  self.txtComponentCount_12,
                  self.txtComponentCount_13,
                  self.txtComponentCount_14,
                  self.txtComponentCount_15,
                  self.txtComponentCount_16,
                  self.txtComponentCount_17,
                  self.txtComponentCount_18,
                  self.txtComponentCount_19,
                  self.txtComponentCount_20,]

        index = 0

        for line in lines[6:]:
            #print (line)
            temp = line.split()
            if (len(temp) == 5):
                #print (temp)
                pattern1 = r"name=\"([\w-]+)"
                pattern2 = r"([\w-]+)\""
                mat1 = re.search(pattern1, temp[1])
                mat2 = re.search(pattern2, temp[2])

                component = mat1.group(1) + " " + mat2.group(1)
                #print (component)

                pattern3 = r"count=\"([0-9]+)\""
                mat3 = re.search(pattern3, temp[3])
                count = mat3.group(1)
                #print (count)

                components[index].setText(component)
                counts[index].setText(count)

                index = index + 1

        self.btnSave.setEnabled(Tr+ue)
        self.btnLoad.setDisabled(True)







    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        * DO NOT MODIFY THIS METHOD! *
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if _name_ == "_main_":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()