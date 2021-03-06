from rest_framework import serializers

from core.models import Affiliate, Article, Executive, Project


class AffiliateSerializer(serializers.ModelSerializer):
    """Serializer for the affiliate object."""

    class Meta:
        model = Affiliate
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for the article object."""

    class Meta:
        model = Article
        fields = '__all__'


class ExecutiveSerializer(serializers.ModelSerializer):
    """Serializer for the executive object."""

    class Meta:
        model = Executive
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the project object."""

    class Meta:
        model = Project
        fields = '__all__'
