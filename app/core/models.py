from django.db import models
from core.choices import CATEGORY, CURRENCY


class Article(models.Model):
    """The article object."""
    date = models.DateField(auto_now_add=True)
    image = models.ImageField()
    text = models.TextField()
    title = models.CharField(max_length=255)


class Person(models.Model):
    """The person object."""
    image = models.ImageField()
    first_name = models.CharField(max_length=255)
    image = models.ImageField()
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'people'


class Project(models.Model):
    """The project object."""
    category = models.CharField(max_length=255, choices=CATEGORY)
    client = models.CharField(max_length=255)
    consulting_engingeer = models.CharField(max_length=255)
    contract_completion = models.DateField()
    contract_period = models.IntegerField()
    cost_engineer = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    image = models.ImageField()
    location = models.CharField(max_length=255)
    main_contractor = models.CharField(max_length=255)
    project_cost = models.IntegerField()
    project_cost_currency = models.CharField(max_length=255, choices=CURRENCY)
    project_manager = models.CharField(max_length=255)
    text = models.TextField()
    title = models.CharField(max_length=255)
