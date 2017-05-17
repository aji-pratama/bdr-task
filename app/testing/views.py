from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ArticleForm
from .models import Article
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    form = ArticleForm()
    # if request.POST:
    #     title = request.POST.get('title')
    #     body = request.POST.get('body')
    #     insert_data = Article(title=title, body=body)
    #
    #     insert_data.save()
    #     return HttpResponseRedirect('/testing')

    return render(request, 'testing/index.html', {'form': form})

def input_data(request):
    if request.POST:
        title = request.POST.get('title')
        body = request.POST.get('body')
        insert_data = Article(title=title, body=body)

        insert_data.save()
        return HttpResponse('/testing')
