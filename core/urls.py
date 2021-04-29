from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core import views


app_name = 'core'

schema_view = get_schema_view(
    openapi.Info(
        title="Cebarco API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    url='https://cebarco.com/api/'
)

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
    path('projects/', views.ListProjects.as_view(), name='projects'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
