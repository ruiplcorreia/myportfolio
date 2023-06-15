from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myportfolio'

urlpatterns = [path('', views.homepage, name='homepage'),
               path('home/', views.homepage, name='home'),

               path('login/', views.login_view, name='login'),
               path('logout/', views.logout_view, name='logout'),

#               path('aboutme/', views.edit_degree, name='aboutme'),
               path('aboutme/degree/', views.degree, name='degree'),
               path('aboutme/degree/create/',views.create_degree, name='create_degree'),
               path('aboutme/degree/edit/<int:degree_id>',views.edit_degree, name='adedit'),
               path('aboutme/degree/delete/<int:degree_id>',views.delete_degree, name='delete_degree'),

               path('aboutme/education/', views.education, name='education'),
               path('aboutme/education/create/',views.create_education, name='create_education'),
               path('aboutme/education/edit/<int:institution_id>',views.edit_education, name='aeedit'),
               path('aboutme/education/delete/<int:institution_id>',views.delete_education, name='delete_education'),

               path('aboutme/skills/', views.skills, name='skills'),
               path('aboutme/interests/', views.interests, name='interests'),
               path('aboutme/profexperience/',views.profexperience, name='profexperience'),

               path('projects/collegeproj', views.collegeproj, name='collegeproj'),
               path('projects/myprojects', views.myprojects, name='myprojects'),
               path('projects/finalprojects',views.finalprojects, name='finalprojects'),

               path('pw/technologies/tfrontend', views.tfrontend, name='tfrontend'),
               path('pw/technologies/tbackend', views.tbackend, name='tbackend'),
               path('pw/tlabs', views.tlabs, name='tlabs'),
               path('pw/tnews', views.tnews, name='tnews'),

               path('testimonials/', views.testimonials, name='testimonials'),
               path('cta/', views.cta, name='cta'),

               # Blog section
               path('blog/', views.blog, name='blog'),
               path('blog/newpost/', views.new_post, name='new_post'),
               path('blog/edit/<int:post_id>', views.post_edit, name='post_edit'),
               path('blog/delete/<int:post_id>', views.post_delete, name='post_delete'),               

               # About this site
               path('aboutthissite/atechnologies', views.atechnologies, name='atechnologies'),
               path('aboutthissite/astandards', views.astandards, name='astandards'),
               path('sitemap', views.sitemap, name='sitemap'),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
