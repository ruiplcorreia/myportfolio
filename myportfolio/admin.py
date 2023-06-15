from django.contrib import admin
from .models import Institution, Degree, Class, Teacher, Student, Post


# Register your models here.
admin.site.register(Institution)
admin.site.register(Degree)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Post)

