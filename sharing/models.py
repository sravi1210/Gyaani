from django.db import models


TYPEOFUPLOAD = (
    ('Midsem', 'Midsem'),
    ('Endsem', 'Endsem'),
    ('Quiz', 'Quiz'),
    ('Book' , 'Book'),
    ('Slide' , 'Slide'),
    ('Miscalleneous','Miscalleneous')
)


HOSTEL_CHOICES = (
    ('Barak', 'Barak'),
    ('Bramhaputra', 'Bramhaputra'),
    ('Dhansiri', 'Dhansiri'),
    ('Dibang', 'Dibang'),
    ('Dihing', 'Dihing'),
    ('Kameng', 'Kameng'),
    ('Kapili', 'Kapili'),
    ('Lohit', 'Lohit'),
    ('Manas', 'Manas'),
    ('Siang', 'Siang'),
    ('Subansiri', 'Subansiri'),
    ('Umiam', 'Umiam'),
    ('Married_Scholar', 'Married_Scholar'),

)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others','Others')
)

DEGREE = (
    ('Mtech', 'Mtech'),
    ('Phd', 'Phd'),
    ('Btech', 'Btech')
)

ACADEMIC_YEAR = (
    (1, ("1")),
    (2, ("2")),
    (3, ("3")),
    (4, ("4")),
    (5, ("5")),
    (6, ("6")),
    (7, ("7")),
)

SEMESTER = (
    (1, ("1")),
    (2, ("2")),
    (3, ("3")),
    (4, ("4")),
    (5, ("5")),
    (6, ("6")),
    (7, ("7")),
    (8, ("8")),

)

class Course(models.Model):
    courseName = models.CharField(max_length=200 )
    courseid = models.CharField(max_length=200  )

class Upload(models.Model):
    content = models.FileField(upload_to='uploads/')
    course = models.ForeignKey(Course , null=True , on_delete=models.CASCADE)
    type = models.CharField(max_length=35, choices=TYPEOFUPLOAD ,blank=False)

class Student(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    profile_pic = models.ImageField(upload_to='student', blank=True, null=True)
    roll_no = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER, blank=False)
    webmail = models.CharField(max_length=128, blank=False, unique=True)
    degree = models.CharField(max_length=128, choices=DEGREE, blank=True)
    acedemic_year = models.IntegerField(choices=ACADEMIC_YEAR, default=0)
    present_semester = models.IntegerField(choices=SEMESTER, null=True, blank=True)
    hostel_name = models.CharField(max_length=255, choices=HOSTEL_CHOICES, blank=True, default="")
    mob_number = models.CharField(max_length=15, blank=False, default=" ")

class Moderator(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    profile_pic = models.ImageField(upload_to='student', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=False)
    mob_number = models.CharField(max_length=15, blank=False, default=" ")
