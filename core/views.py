from rest_framework import generics

from core.models import Affiliate, Article, Executive, Project
from core.serializers import AffiliateSerializer, ArticleSerializer, \
                             ExecutiveSerializer, ProjectSerializer


class RetrieveAffiliate(generics.RetrieveAPIView):
    """Retrieve an affiliate."""
    serializer_class = AffiliateSerializer
    lookup_field = 'slug'
    queryset = Affiliate.objects.all()


class RetrieveArticle(generics.RetrieveAPIView):
    """Retrieve an article."""
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    queryset = Article.objects.all()


class RetrieveExecutive(generics.RetrieveAPIView):
    """Retrieve an executive."""
    serializer_class = ExecutiveSerializer
    lookup_field = 'slug'
    queryset = Executive.objects.all()


class RetrieveProject(generics.RetrieveAPIView):
    """Retrieve a project."""
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    queryset = Project.objects.all()


class ListAffiliates(generics.ListAPIView):
    """List affiliates."""
    serializer_class = AffiliateSerializer
    queryset = Affiliate.objects.all()


class ListArticles(generics.ListAPIView):
    """List articles."""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-date')


class ListExecutives(generics.ListAPIView):
    """List executives."""
    serializer_class = ExecutiveSerializer
    queryset = Executive.objects.all().order_by('rank')


class ListProjects(generics.ListAPIView):
    """List projects."""
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('-contract_price')
