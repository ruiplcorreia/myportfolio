from django.db import models


education_stages = (
    ("degree", "Degree"),
    ("middle-school", "Middle-School"),
    ("certification", "Certification"),
)

degree_semester = (
    (1, 1),
    (2, 2),    
)

degree_year = (
    (1, 1),
    (2, 2),    
)



class Institution(models.Model):
    
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=80)
    webpage = models.CharField(blank=True,max_length=100)    
    logo = models.ImageField(
        upload_to='media', blank=True)

    def __str__(self):
        return self.name


class Degree(models.Model):
    
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name='degrees')
    name = models.CharField(max_length=80)
    abbrev = models.CharField(blank=True,max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    
    name = models.CharField(max_length=100)
    profile_url = models.URLField(blank=True,max_length=30)
    smprofile_url = models.URLField(blank=True,max_length=30)
    def __str__(self):
        return self.name

class Class(models.Model):
    
    degree = models.ManyToManyField(Degree, related_name='classes')
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher, related_name='teaches')
    semester = models.IntegerField(choices=degree_semester,default=1)
    year = models.IntegerField(choices=degree_year,default=1)
    def __str__(self):
        return self.name

class Student(models.Model):
    
    name = models.CharField(max_length=100)
    degrees = models.ManyToManyField(Degree, related_name='students')
    def __str__(self):
        return self.name

class Post(models.Model):
    
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='media/myportfolio/img/', blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
