class Persom(object):
	"""docstring for ClassName"""
	def __init__(self, name, mass, gender):
		super(ClassName, self).__init__()
		self.name = name
	    self.mass = mass
	    self.gender = gender

	def firstName(self):
		fname = self.name.split()[0]
		return fname

	def lastName(self):
		fname = self.name.split()[1]
		return lname

    def body_mass_index(self, height):
		bmi = self.mass / (height*height)
		return bmi




class Employee(Person):
		"""docstring for Employee"""
		def __init__(self, salary, jd, dpt):
			
			self.name = Person.firstName()
			self.salary = salary
			self.jd = jd
			self.dpt = dpt


		def return_one_employee(self):
			return:"{} is a {} and earns {}".format(Person.firstName("Abraham Ogol"), self jd, self salary)


				