from django.urls import path
from django.contrib import admin

from web import views


app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('project/<id>/', views.project, name='project'),
    path('news/', views.news, name='news'),
    path('article/<id>/', views.article, name='article'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks')
]

admin.site.site_header = 'Cebarco Admin'
admin.site.site_title = 'Cebarco Admin Portal'
