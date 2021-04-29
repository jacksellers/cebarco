from django.urls import path
from django.contrib import admin

from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/all/', views.projects_all, name='projects-all'),
    path('project/<slug>/', views.project, name='project'),
    path('news/', views.news, name='news'),
    path('article/<slug>/', views.article, name='article'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
]

admin.site.site_header = 'Cebarco Admin'
admin.site.site_title = 'Cebarco Admin Portal'
