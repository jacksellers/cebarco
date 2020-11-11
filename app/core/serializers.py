from rest_framework import serializers

from core.models import Article, Person, Project


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for the article object."""

    class Meta:
        model = Article
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    """Serializer for the person object."""

    class Meta:
        model = Person
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the project object."""

    class Meta:
        model = Project
        fields = '__all__'
