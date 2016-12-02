#!/usr/bin/python

#example of using inherit

class SchoolMember:
    '''Represent any school member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialize SchoolMember:%s' %self.name)

    def tell(self):
        '''Tell the detail'''
        print('name:%s,age:%d' %(self.name, self.age))

class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Inialized Teacher: %s' %self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:%d' %self.salary)

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print("Initialize Student: %s" %self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:%d' %self.mark)

#####################################################
student = Student('Jack', 23, 98)
teacher = Teacher('Mary', 25, 5000)
print('--------------------------------------')

members = [student, teacher]
for i in members:
    i.tell()


