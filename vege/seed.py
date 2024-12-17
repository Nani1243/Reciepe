from faker import Faker # type: ignore
fake=Faker()
from .models import *
import random


def sub_marks(n):
    try:
        student_objs=Student.objects.all()
        for student in student_objs:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0,100)
                )
    except Exception as e:
        print(e)


def seed_db(n=10) ->None:
    try:
        for _ in range(0,n):
            department_objs=Department.objects.all()

            department_index=random.randint(0,len(department_objs)-1)
            department=department_objs[department_index]
            student_id=f'STU-{random.randint(100,999)}'
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(20,30)
            student_details=fake.address()

 
            studentid_objs=StudentId.objects.create(student_id=student_id)

            student_objs=Student.objects.create(
                department=department,
                student_id=studentid_objs,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_details=student_details,
            )
    except Exception as e:
        print(e)