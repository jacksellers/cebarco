from django.urls import path

from core import views


app_name = 'core'

urlpatterns = [
    path('article/<id>/', views.RetrieveArticle.as_view(), name='article'),
    path('person/<id>/', views.RetrievePerson.as_view(), name='person'),
    path('project/<id>/', views.RetrieveProject.as_view(), name='project'),
    path('articles/', views.ListArticles.as_view(), name='articles'),
    path('people/', views.ListPeople.as_view(), name='people'),
    path('projects/', views.ListProjects.as_view(), name='projects')
]
