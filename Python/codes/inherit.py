class SchoolMember:
	'''Represent a school member.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print '(Initialized SchoolMember: %s)' % self.name

	def tell(self):
		'''Tell my details.'''
		print 'Name:"%s" Age:"%s"' % (self.name, self.age)

class Teacher(SchoolMember):
	'''Represents a teacher.'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.__salary = salary
		print '(Initialized Teacher: %s)' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: "%d"' % self.__salary

class Student(SchoolMember):
	'''Represents a student.'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.__marks = marks
		print '(Initialized Student: %s)' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: "%d"' % self.__marks
