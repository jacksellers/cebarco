from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from random import shuffle

from core.forms import MessageForm
from core.models import Article, Executive, Message, Project


def index(request):
    projects = Project.objects.filter(home_page=True).order_by('?')[:6]
    articles = Article.objects.all().order_by('-date')[:3]
    return render(
        request, 'index.html', {'projects': projects, 'articles': articles}
    )


def about(request):
    executives = Executive.objects.all()
    return render(request, 'about.html', {'executives': executives})


def projects(request):
    projects = Project.objects.filter(
        projects_page=True
    ).order_by('-contract_completion')
    return render(request, 'projects.html', {'projects': projects})


def project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'project.html', {'project': project})


def news(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'news.html', {'articles': articles})


def article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article.html', {'article': article})


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'From: {}\nMessage: {}'.format(
                form.cleaned_data['name'], form.cleaned_data['message']
            )
            send_mail(
                form.cleaned_data['subject'],
                message,
                form.cleaned_data['email'],
                ['jacksellers91@gmail.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
