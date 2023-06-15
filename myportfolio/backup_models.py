from django.db import models


education_stages = (
    ("degree", "Degree"),
    ("middle-school","Middle-School"),
    ("certification","Certification"),
)

class Institution(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    webpage = models.CharField(blank=True,max_length=100)    
    logo = models.ImageField(
        upload_to='media', blank=True)

    def __str__(self):
        return self.name

class Education_type(models.Model):
    name = models.CharField(max_length=100) 
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_cert = models.BooleanField()
    cert_code = models.CharField(blank=True, max_length=100)
    stage_type = models.CharField(max_length=13,
                  choices=education_stages,
                  default="Degree")
    
    def __str__(self):
        return self.name

""" class Course(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    year = models.IntegerField()
    semester = models.CharField(max_length=50)
    ects = models.IntegerField()
    topics = models.TextField()
    ranking = models.IntegerField(default=1)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name[:50] """

class Post(models.Model):
    """model that allows to specify models """
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='media/myportfolio/img/', blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """ This is to present the post in this case the title will be used but only 20 chars"""

    def __str__(self):
        return self.title[:20]

