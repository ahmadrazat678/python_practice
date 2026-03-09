class Employee:
    name = "Ahmad"
    language = "Python"
    salary = 1200000

    def _init_(self , name, salary, language): #dunder method which is automatically called.
          self.name = name
          self.salary = salary
          self.language = language
          print ("I am creating an object.")
          
    def getinfo(self):
            print(f"The language is {self.language}.The salary is {self.salary}.")

    @staticmethod
    def greet():
          print("Good Morning!")
           
Ahmad = Employee()
print (Ahmad.name, Ahmad.language, Ahmad.salary)
Ahmad.getinfo()

Zain = Employee()