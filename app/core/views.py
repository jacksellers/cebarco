from rest_framework import generics

from core.models import Article, Person, Project
from core.serializers import ArticleSerializer, PersonSerializer, \
                             ProjectSerializer


class RetrieveArticle(generics.RetrieveAPIView):
    """Retrieve an article."""
    serializer_class = ArticleSerializer
    lookup_field = 'id'
    queryset = Article.objects.all()


class RetrievePerson(generics.RetrieveAPIView):
    """Retrieve a person."""
    serializer_class = PersonSerializer
    lookup_field = 'id'
    queryset = Person.objects.all()


class RetrieveProject(generics.RetrieveAPIView):
    """Retrieve a project."""
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    queryset = Project.objects.all()


class ListArticles(generics.ListAPIView):
    """List articles."""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ListPeople(generics.ListAPIView):
    """List people."""
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class ListProjects(generics.ListAPIView):
    """List projects."""
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()