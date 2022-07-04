from re import sub
from admission import Admission
from career import Career
from student import Student
from subject import Subject
from university import University
from main_option import *

#registration = Registration()

def menu():
    print("")

print(MAIN_OPTION_TEXT)

# while True:
university = University("UM", "España y Bernardo de Yrigoyen", "um.edu.ar")
student = Student('Lucas', 'Galdame', 59114, 'luqui0008@gmail.com')
subject = Subject('Calculo I', 123)
career = Career('Ingenieria Informatica', "Ingeniera 1", university)
admission = Admission(student, "Calculo I", "Agosto 2022")
career.subjects.append(subject)
career.subjects.append(subject)
subject.students.append(student)
print(career)
print(student)
print(admission)
admission.status = False
print(admission)

menu()


