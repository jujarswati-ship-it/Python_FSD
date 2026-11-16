class student:
    def __init__(self,name,age):
       self.name=name
       self.age=age

    def display(self):
        print(f'name:{self.name}, age:{self.age} ')
    def study(self,subject):
        print(f'{self.name} is studying{subject}')

s1=student("swati",11)
s2=student("san",12)
s1.display()
    