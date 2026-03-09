class Employee:
    name = "Ahmad"
    language = "Python"
    salary = 1200000

    def getinfo(self):
            print(f"The language is {self.language}.The salary is {self.salary}.")

Ahmad = Employee()
print (Ahmad.name, Ahmad.language, Ahmad.salary)
Ahmad.getinfo()