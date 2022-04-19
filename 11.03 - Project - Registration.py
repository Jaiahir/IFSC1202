from tabulate import tabulate
class Student :
   def __init__(self, firstname="Mary", lastname="Drake", tnumber="T123567") :
       self.FirstName = firstname
       self.LastName = lastname
       self.TNumber = tnumber
       self.CourseList = []

class Studentlist :
   def __init__(self) :
       self.Studentlist = []
   def add_student(self, firstname, lastname, tnumber) :
       student = Student(firstname, lastname, tnumber)
       self.Studentlist.append(student)
   def find_student(self, studenttofind) :
       for i in range(len(self.Studentlist)) :
           if(self.Studentlist[i].TNumber == studenttofind) :
               return i
   def print_student_list(self) :
       headers = ["First Name", "Last Name", "T-Number", "Course", "Name", "Room", "Meeting Times"]
       table = [headers]
       for student in self.Studentlist :
           studentinfo = [student.FirstName, student.LastName, student.TNumber]
           table.append(studentinfo)
           for course in student.CourseList :

#For formatting the table as given in output
               courseinfo = [" "," "," "]
               courseinfo.extend([course.department+" "+course.number, course.name, course.room, course.meetingtimes])
               table.append(courseinfo)
       print(tabulate(table))

   def add_student_from_file(self, filename) :
       f = open(filename, "r")
       students = f.readlines()
       for student in students :
           student = student.split(',')
           self.add_student(student[0].strip(), student[1].strip(), student[2].strip())

class Course :
   def __init__(self, department="IFSC", number="1110", name="Introduction to Ethics", room="EIT 211", meetingtimes="M-W 9:00-10:50") :
       self.department = department
       self.number = number
       self.name = name
       self.room = room
       self.meetingtimes = meetingtimes

class Courselist :
   def __init__(self) :
       self.Courselist = []
   def add_course(self, department, number, name, room, meetingtimes) :
       course = Course(department, number, name, room, meetingtimes)
       self.Courselist.append(course)
   def find_course(self, departmenttofind, numbertofind) :
       for i in range(len(self.Courselist)) :
           if(self.Courselist[i].department == departmenttofind and self.Courselist[i].number == numbertofind) :
               return i
   def add_course_from_file(self, filename) :
       f = open(filename, "r")
       courses = f.readlines()
       for course in courses :
           course = course.split(',')
           self.add_course(course[0].strip(), course[1].strip(), course[2].strip(), course[3].strip(), course[4].strip())

if __name__ == '__main__' :
   mycourselist = Courselist()
   mycourselist.add_course_from_file("11.03 Courses.txt")
  
   mystudentlist = Studentlist()
   mystudentlist.add_student_from_file("11.03 Students.txt")
  
   fRegisterations = open("11.03 Registration.txt", "r")
   registerations = fRegisterations.readlines()
   for registeration in registerations :
       registeration = registeration.split(',')
       department, number = registeration[1].strip(), registeration[2].strip()
       courseindex = mycourselist.find_course(department, number)
       if courseindex == None:
           continue
       mycourse = mycourselist.Courselist[courseindex]
       tnumber = registeration[0]
       studentindex = mystudentlist.find_student(tnumber)
       mystudentlist.Studentlist[studentindex].CourseList.append(mycourse)
   mystudentlist.print_student_list()