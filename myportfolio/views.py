from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Institution, Degree, Class, Teacher, Student, Post
from .forms import InstitutionForm, DegreeForm, ClassForm, TeacherForm, StudentForm, PostForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myportfolio:home')
        else:
            error = 'Invalid login credentials'
            return render(request, 'myportfolio/login.html', {'error': error})
    else:
        return render(request, 'myportfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('myportfolio:home')


def homepage(request):

    return render(request, 'myportfolio/home.html')


def aboutme(request):

    return render(request, 'myportfolio/aboutme.html')


def education(request):
    institution = Institution.objects.all()
    return render(request, 'myportfolio/education.html', {'institution': institution})


def degree(request):
    degrees = Degree.objects.all()
    return render(request, 'myportfolio/degree.html', {'degrees': degrees})


""" @login_required """


def create_degree(request):
    if request.method == 'POST':
        form = DegreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myportfolio:education')
    else:
        form = DegreeForm()
    return render(request, 'myportfolio/create_degree.html', {'form': form})


def edit_degree(request, degree_id):
    try:
        degree = Degree.objects.get(id=degree_id)
    except Degree.DoesNotExist:
        return redirect('myportfolio:education')

    if request.method == 'POST':
        form = DegreeForm(request.POST, instance=degree)
        if form.is_valid():
            form.save()
            return redirect('myportfolio:education')
    else:
        form = DegreeForm(instance=degree)

    return render(request, 'myportfolio/edit_degree.html', {'form': form, 'degree': degree})


def delete_degree(request, degree_id):
    try:
        degree = Degree.objects.get(id=degree_id)
    except Degree.DoesNotExist:
        return redirect('myportfolio:education')

    if request.method == 'POST':
        degree.delete()
        return redirect('myportfolio:education')

    return render(request, 'myportfolio/delete_degree.html', {'degree': degree})

# EDUCATION PART
def create_education(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myportfolio:education')
    else:
        form = InstitutionForm()
    return render(request, 'myportfolio/create_education.html', {'form': form})


def edit_education(request, institution_id):
    try:
        institution = Institution.objects.get(id=institution_id)
    except Institution.DoesNotExist:
        return redirect('myportfolio:education')

    if request.method == 'POST':
        form = InstitutionForm(request.POST, instance=institution)
        if form.is_valid():
            form.save()
            return redirect('myportfolio:education')
    else:
        form = InstitutionForm(instance=institution)

    return render(request, 'myportfolio/edit_education.html', {'form': form, 'institution': institution})


def delete_education(request, institution_id):
    try:
        institution = Institution.objects.get(id=institution_id)
    except Institution.DoesNotExist:
        return redirect('myportfolio:education')

    if request.method == 'POST':
        institution.delete()
        return redirect('myportfolio:education')

    return render(request, 'myportfolio/delete_education.html', {'institution': institution})


def skills(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/skills.html', {'Institution': schools})


def interests(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/interests.html', {'Institution': schools})


def profexperience(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/profexperience.html', {'Institution': schools})


def collegeproj(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/collegeproj.html', {'Institution': schools})


def myprojects(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/myprojects.html', {'Institution': schools})


def finalprojects(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/finalprojects.html', {'Institution': schools})


def tfrontend(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/tfrontend.html', {'Institution': schools})


def tbackend(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/tbackend.html', {'Institution': schools})


def tlabs(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/tlabs.html', {'Institution': schools})


def tnews(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/tnews.html', {'Institution': schools})


def testimonials(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/testimonials.html', {'Institution': schools})


def cta(request):

    return render(request, 'myportfolio/cta.html')


def blog(request):
    posts = sorted(Post.objects.all(),
                   key=lambda objecto: objecto.created_at, reverse=True)
    return render(request, 'myportfolio/blog.html', {'posts': posts})



def atechnologies(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/atechnologies.html', {'schools': schools})


def astandards(request):
    schools = Institution.objects.all()
    return render(request, 'myportfolio/astandards.html', {'schools': schools})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myportfolio:blog')
    else:
        form = PostForm()
    return render(request, 'myportfolio/post_create.html', {'form': form})



def post_edit(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('myportfolio:blog')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('myportfolio:blog')
    else:
        form = PostForm(instance=post)

    return render(request, 'myportfolio/post_edit.html', {'form': form, 'institution': post})








def post_delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('myportfolio:blog')

    if request.method == 'POST':
        post.delete()
        return redirect('myportfolio:blog')

    return render(request, 'myportfolio/post_delete.html', {'post': post})


def sitemap(request):

    return render(request, 'myportfolio/sitemap.html')
