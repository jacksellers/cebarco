from django.db import models
from core.choices import CATEGORY, CURRENCY


class Article(models.Model):
    """The article object."""
    date = models.DateField()
    image = models.ImageField()
    intro = models.TextField()
    source_link = models.URLField(blank=True)
    source_name = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    title = models.CharField(max_length=255)

    def save(self):
        self.intro = ' '.join(self.text.split()[:40]) + '...'
        super().save()


class Message(models.Model):
    """The message object, used in the contact form."""
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255)


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
    contract_period = models.IntegerField(help_text='months')
    cost_engineer = models.CharField(max_length=255, blank=True)
    employer = models.CharField(max_length=255, blank=True)
    homepage = models.BooleanField(default=False)
    image = models.ImageField()
    location = models.TextField(help_text='Google Maps embed (iframe)')
    main_contractor = models.CharField(max_length=255)
    project_cost = models.IntegerField(blank=True, null=True)
    project_currency = models.CharField(
        max_length=255, choices=CURRENCY, blank=True
    )
    project_manager = models.CharField(max_length=255, blank=True)
    project_value = models.IntegerField(blank=True, null=True)
    text = models.TextField()
    title = models.CharField(max_length=255)

    def save(self):
        old_iframe = self.location.split()
        new_iframe = [
            attribute if attribute[:5] != 'width' else 'width="100%"'
            for attribute in old_iframe
        ]
        self.location = ' '.join(new_iframe)
        super().save()
