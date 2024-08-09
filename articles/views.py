from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article


# Create your views here.

def articles_home(request):
    obj_qs = Article.objects.all
    article = Article()
    article.title = 'huroki'
    article.content = 'naka'

    context = {
        'title' : article.title,
        'content' : article.content,
        'objects' : obj_qs
    }
    return render(request,'myapp/base.html',context=context)
