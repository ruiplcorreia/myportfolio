from django import forms
from django.forms import ModelForm
from .models import Degree

from .models import Institution, Degree, Class, Teacher, Student, Post

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'

class DegreeForm(ModelForm):
    class Meta:
        model = Degree
        fields = '__all__'

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'