#object oriented programming
class user:

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age 
        self.dept = dept
    def age_increment(self):
        self.age += 1
        return self.age
    def change_name(self, name):
        self.name = name
        return name
    def change_dept(self, dept):
        self.dept = dept
        return self.dept
somebody = user("Dara", 21, "ECE")
print(somebody.change_name("John"))
print(somebody.change_dept("MSE"))
print(somebody.age_increment())
