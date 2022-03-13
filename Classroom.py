#We need to Class a Teacher, 5 students, and the janitor.
#Every person has a 1st name, last name, and an age.
#All of the Students also of a grade.
#The teacher will have a subject they teach
#The janitor will have a favourite tool
#Each person must say: "Hello! My name is- my age is- My grade is- I teach- My favorite tool is-"
#BONUS: Creat three classrooms.

teacher = {
    'name': 'mary',
    'last_name': 'davenport',
    'age': '31,',
    'subject': 'math'
};

students = {
    'name': ['bob', 'jake', 'lester', 'ashley', 'heather'],
    'last_name': ['mayday', 'walker', 'hansen', 'drake', 'lancing'],
    'age': ['10'],
    'grade': ['5']
};

janitor = {
    'name': 'jefferson',
    'last_name': 'davis',
    'age': '54',
    'tool': 'broom'
};
class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def speak(self):
        print("Hello my name is " + self.name +" "+ self.last_name +" and I am "+ self.age)
class Students(Person):
    def __init__(self, name, last_name, age, grade):
        Person.__init__(name, last_name, 10)
        self.grade = 5
class Teacher(Person):
    def __init__(self, name, last_name, age, subject):
        Person.__init__(self, name, last_name, age)
        self.subject = subject
class Janitor(Person):
    def __init__(self, name, last_name, age, tool):
        Person.__init__(self, name, last_name,age)
        self.tool = "broom" 
i = 0;
classroom = [];
while i > 6: 
    classroom[i] = Students(students['name'][i], students['last_name'][i], 10, 5);
teacher = Teacher('Mary', 'Davenport', '31', 'math')    
janitor = Janitor('Jefferson', 'Davis', '54', 'broom')

janitor.speak();