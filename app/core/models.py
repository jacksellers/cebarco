from django.db import models
from django.utils.text import slugify

from core.choices import CATEGORY, CURRENCY


class Affiliate(models.Model):
    """The affiliate object, can be a person or an organisation."""
    name = models.CharField(
        max_length=255,
        help_text='''
            This can be a person or an organisation
        ''',
        unique=True
    )
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()


class Article(models.Model):
    """The article object."""
    date = models.DateField()
    image = models.ImageField()
    intro = models.TextField()
    source_link = models.URLField(blank=True)
    source_name = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()

    def save(self):
        self.intro = ' '.join(self.text.split()[:40]) + '...'
        self.slug = slugify(self.title)
        super().save()


class Executive(models.Model):
    """The executive object, to be in included in the 'About' page."""
    first_name = models.CharField(max_length=255)
    image = models.ImageField()
    last_name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=255,
        help_text='''
            Their position in Cebarco (e.g. 'CEO')
        '''
    )
    slug = models.SlugField()

    def save(self):
        self.slug = slugify(self.first_name + '_' + self.last_name)
        super().save()

    class Meta:
        unique_together = ['first_name', 'last_name']


class Message(models.Model):
    """The message object, used in the contact form."""
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255)


class Project(models.Model):
    """The project object."""
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255, choices=CATEGORY)
    client = models.ForeignKey(
        'Affiliate',
        related_name='projects_as_client',
        on_delete=models.PROTECT
    )
    consulting_engingeer = models.ForeignKey(
        'Affiliate',
        related_name='projects_as_consulting_engingeer',
        on_delete=models.PROTECT
    )
    contract_completion = models.DateField(
        help_text='''
            yyyy-mm-dd (if the day is unknown, just put '01')
        '''
    )
    contract_currency = models.CharField(
        max_length=255, choices=CURRENCY, blank=True
    )
    contract_period = models.IntegerField(help_text='months')
    contract_price = models.IntegerField(blank=True, null=True)
    home_page = models.BooleanField(
        help_text='Should this be shown on the home page?'
    )
    projects_page = models.BooleanField(
        help_text='Should this be shown on the projects page?'
    )
    image = models.ImageField()
    location = models.TextField(
        help_text='''
            1) Find it in Google Maps
            2) Click on the 'share' button
            3) Select 'Embed a map'
            4) Select 'COPY HTML'

        '''
    )
    project_manager = models.ForeignKey(
        'Affiliate',
        related_name='projects_as_project_manager',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    slug = models.SlugField()
    text = models.TextField()

    def save(self):
        self.slug = slugify(self.name)
        old_iframe = self.location.split()
        new_iframe = [
            attribute if attribute[:5] != 'width' else 'width="100%"'
            for attribute in old_iframe
        ]
        self.location = ' '.join(new_iframe)
        super().save()
