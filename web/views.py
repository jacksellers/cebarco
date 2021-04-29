from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from random import shuffle

from core.forms import MessageForm
from core.models import Article, Executive, Message, Project


def index(request):
    projects = Project.objects.filter(home_page=True).order_by('?')[:12]
    articles = Article.objects.all().order_by('-date')[:3]
    return render(
        request, 'index.html', {'projects': projects, 'articles': articles}
    )


def about(request):
    executives = Executive.objects.filter(cropped=True).order_by('rank')
    return render(request, 'about.html', {'executives': executives})


def projects(request):
    projects = Project.objects.filter(
        projects_page=True, cropped=True
    ).order_by('-contract_price')
    return render(request, 'projects.html', {'projects': projects})


def projects_all(request):
    projects = Project.objects.all().order_by('name')
    return render(request, 'projects_all.html', {'projects': projects})


def project(request, slug):
    project = Project.objects.get(slug=slug)
    gallery_images = project.gallery_images.filter(cropped=True)
    gallery_videos = project.gallery_videos.all()
    return render(
        request,
        'project.html',
        {
            'project': project,
            'gallery_images': gallery_images,
            'gallery_videos': gallery_videos
        }
    )


def news(request):
    articles = Article.objects.filter(cropped=True).order_by('-date')
    return render(request, 'news.html', {'articles': articles})


def article(request, slug):
    article = Article.objects.get(slug=slug)
    gallery_images = article.gallery_images.filter(cropped=True)
    gallery_videos = article.gallery_videos.all()
    return render(
        request,
        'article.html',
        {
            'article': article,
            'gallery_images': gallery_images,
            'gallery_videos': gallery_videos
        }
    )


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data['phone']:
                message = 'Name: {}\nEmail: {}\nPhone: {}\nMessage: {}'.format(
                    form.cleaned_data['name'],
                    form.cleaned_data['email'],
                    form.cleaned_data['phone'],
                    form.cleaned_data['message']
                )
            else:
                message = 'Name: {}\nEmail: {}\nMessage: {}'.format(
                    form.cleaned_data['name'],
                    form.cleaned_data['email'],
                    form.cleaned_data['message']
                )
            send_mail(
                form.cleaned_data['subject'],
                message,
                'admin@cebarco.com',
                ['cebarco@kar-group.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')


def handler400(request, exception):
    return render(request, 'errors/400.html')


def handler403(request, exception):
    return render(request, 'errors/403.html')


def handler404(request, exception):
    return render(request, 'errors/404.html')


def handler500(request):
    return render(request, 'errors/500.html')
