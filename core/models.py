from django.db import models
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.core.files import File
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from image_cropping import ImageRatioField

from core.choices import CATEGORY, CURRENCY


#image compression method
def compress(image):
    im = Image.open(image)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image


class Affiliate(models.Model):
    """The affiliate object, can be a person or an organisation."""
    name = models.CharField(
        max_length=255,
        help_text='''
            This can be a person or an organisation
        ''',
        unique=True
    )
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()


class Article(models.Model):
    """The article object."""
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField()
    image_ratio = ImageRatioField('image', '1000x1000')
    date = models.DateField()
    cropped = models.BooleanField(default=False)
    intro = models.TextField()
    news_page = models.BooleanField(
        default=True,
        help_text='Should this be shown on the news page?'
    )
    source_link = models.URLField(blank=True)
    source_name = models.CharField(max_length=255, blank=True)
    text = MarkdownxField(
        help_text=mark_safe(
            '''
                You can use
                <a href="https://www.markdownguide.org/cheat-sheet/" 
                target="_blank">
                markdown</a> here to format the text 
            '''
        )
    )
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    def save(self):
        new_text = ''.join(
            BeautifulSoup(markdownify(self.text)).findAll(text=True)
        )
        self.intro = ' '.join(new_text.split()[:40]) + '...'
        self.slug = slugify(self.title)
        self.image = compress(self.image)
        if self.image_ratio:
            self.cropped = True
        super().save()


class Executive(models.Model):
    """The executive object, to be in included in the 'About' page."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField()
    image_ratio = ImageRatioField('image', '1000x1000')
    position = models.CharField(
        max_length=255,
        help_text='''
            Their position in Cebarco (e.g. 'Director')
        '''
    )
    rank = models.IntegerField(
        unique=True,
        help_text='''
            Their relative position on the 'About' page (i.e. 1, 2, 3, ...)
        '''
    )
    slug = models.SlugField(max_length=255)
    cropped = models.BooleanField(default=False)

    def save(self):
        self.slug = slugify(self.first_name + '_' + self.last_name)
        self.image = compress(self.image)
        if self.image_ratio:
            self.cropped = True
        super().save()

    class Meta:
        unique_together = ['first_name', 'last_name']


class GalleryImage(models.Model):
    """The image object, used in the galleries of projects and articles."""
    image = models.ImageField()
    image_ratio = ImageRatioField('image', '1000x1000')
    cropped = models.BooleanField(default=False)
    article = models.ForeignKey(
        'Article',
        related_name='gallery_images',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    project = models.ForeignKey(
        'Project',
        related_name='gallery_images',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def save(self):
        self.image = compress(self.image)
        if self.image_ratio:
            self.cropped = True
        super().save()


class GalleryVideo(models.Model):
    """The video object, used in the galleries of projects and articles."""
    video = models.TextField(
        blank=True,
        help_text='''
            1) Find it in Vimeo
            2) Click on the 'share' button
            3) Select </> [Get embed code]
            4) Select 'Copy' [we only want the <iframe></iframe>]

        '''
    )
    article = models.ForeignKey(
        'Article',
        related_name='gallery_videos',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    project = models.ForeignKey(
        'Project',
        related_name='gallery_videos',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def save(self):
        new_iframe = [
            attribute if attribute[:5] != 'width' else 'width="100%"'
            for attribute in self.video.split()
        ]
        new_iframe = []
        for attribute in self.video.split():
            if attribute[:5] == 'width':
                new_iframe.append('width="100%"')
            elif attribute[:6] == 'height':
                new_iframe.append('height="360"')
            else:
                new_iframe.append(attribute)
        self.video = ' '.join(new_iframe)
        super().save()


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
    image = models.ImageField()
    image_ratio = ImageRatioField('image', '1000x1000')
    category = models.CharField(max_length=255, choices=CATEGORY)
    client = models.ForeignKey(
        'Affiliate',
        related_name='projects_as_client',
        on_delete=models.PROTECT
    )
    consulting_engineer = models.ForeignKey(
        'Affiliate',
        related_name='projects_as_consulting_engingeer',
        on_delete=models.PROTECT
    )
    contract_completion = models.DateField(
        help_text='''
            yyyy-mm-dd (if the day is unknown, just put '01')
        '''
    )
    contract_period = models.IntegerField(help_text='months')
    contract_price = models.IntegerField(
        help_text='''
            US dollars
        '''
    )
    home_page = models.BooleanField(
        help_text='Should this be shown on the home page?'
    )
    projects_page = models.BooleanField(
        default=True,
        help_text='Should this be shown on the projects page?'
    )
    undisclosed = models.BooleanField(
        help_text='Should the contract price be hidden from the public?'
    )
    cropped = models.BooleanField(default=False)
    location = models.TextField(
        blank=True,
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
    slug = models.SlugField(max_length=255)
    text = MarkdownxField(
        blank=True,
        help_text=mark_safe(
            '''
                You can use
                <a href="https://www.markdownguide.org/cheat-sheet/" 
                target="_blank">
                markdown</a> here to format the text 
            '''
        )
    )

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        new_iframe = [
            attribute if attribute[:5] != 'width' else 'width="100%"'
            for attribute in self.location.split()
        ]
        self.location = ' '.join(new_iframe)
        self.image = compress(self.image)
        if self.image_ratio:
            self.cropped = True
        super().save()
