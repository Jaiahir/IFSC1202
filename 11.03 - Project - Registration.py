#I did all the directions but couldn't figure out how to pass the commas on every file and got stuck. This means the program won't run but I did do all the instructions.
def read_from_file(filename):
    f = open(filename, 'r')
    lines = f.read().split('\n')
    lines = list(filter(None, lines))
    f.close()
    return lines

class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.CourseList = []
        return

class StudentList():
    def __init__(self):
        self.StudentList = []
        return

    def add_student(self, firstname, lastname, tnumber):
        newStudent = Student(firstname,lastname,tnumber)
        self.StudentList.append(newStudent)
        return

    def find_student(self, studenttofind):
        for ind,student in enumerate(self.StudentList):
            if student.TNumber == studenttofind:
                return ind
        return

    def print_student_list(self):
        for student in self.StudentList:
            print(f'Courses for {student.FirstName} {student.LastName} (T-Number: {student.TNumber})')
            for course in student.CourseList:
                print(f'  {course.department}{course.number} - {course.name}')
            print()
        return

    def add_student_from_file(self, filename):
        students = read_from_file(filename)
        for student in students:
            firstname, lastname, tnumber = student.split(',')
            self.add_student(firstname, lastname, tnumber)
        return

class Course:
    def __init__(self, department, number, name, room, meetingtimes):
        self.department = department
        self.number = number
        self.name = name
        self.room = room
        self.meetingtimes = meetingtimes
        return

class CourseList:
    def __init__(self):
        self.Courselist = []
        return

    def add_course(self, department, number, name, room, meetingtimes):
        newCourse = Course(department, number, name, room, meetingtimes)
        self.Courselist.append(newCourse)
        return

    def find_course(self, departmenttofind, numbertofind):
        for ind,course in enumerate(self.Courselist):
            if course.department == departmenttofind and course.number == numbertofind:
                return ind
        return

    def add_course_from_file(self, filename):
        courses = read_from_file(filename)
        print(len(courses))
        for course in courses:
            print(len(course.split(',')))
            department, number, name, room, meetingtimes = course.split(',')
            self.add_course(department, number, name, room, meetingtimes)
        return


coursesf = '11.03 Courses.txt'
students = '11.03 Students.txt'
registration = '11.03 Registration.txt'

mycourselist = CourseList()
mycourselist.add_course_from_file(coursesf)
mystudentlist = StudentList()
mystudentlist.add_student_from_file(students)


registration_data = read_from_file(registration)
for reg in registration_data:
    tnumber, department, number = reg.split(',')
    course_index = mycourselist.find_course(department, number)
    mycourse = mycourselist.Courselist[course_index]
    mydepartment, mynumber, myname, myroom, mymeetingtimes = mycourse.department, mycourse.number, mycourse.name, mycourse.room, mycourse.meetingtimes
    mycourse = Course(mydepartment, mynumber, myname, myroom, mymeetingtimes)
    student_index = mystudentlist.find_student(tnumber)
    mystudent = mystudentlist.StudentList[student_index]
    mystudent.CourseList.append(mycourse)

mystudentlist.print_student_list()