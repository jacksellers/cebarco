from django.urls import path

from core import views


app_name = 'core'

urlpatterns = [
    path(
        'afiliate/<slug>/', views.RetrieveAffiliate.as_view(), name='affiliate'
    ),
    path('article/<slug>/', views.RetrieveArticle.as_view(), name='article'),
    path(
        'executive/<slug>/',
        views.RetrieveExecutive.as_view(),
        name='executive'
    ),
    path('project/<slug>/', views.RetrieveProject.as_view(), name='project'),
    path('affiliates/', views.ListAffiliates.as_view(), name='affiliates'),
    path('articles/', views.ListArticles.as_view(), name='articles'),
    path('executives/', views.ListExecutives.as_view(), name='executives'),
    path('projects/', views.ListProjects.as_view(), name='projects')
]
