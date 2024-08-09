'''The `views.py` file in a Django project is responsible for rendering HTML 
web pages. When a user requests a specific URL (e.g., `/home`), Django maps the
 URL to a function in `views.py`. This function receives the request,
  processes it, and returns the appropriate HTML response.'''

from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string 
from django.template import TemplateDoesNotExist


import random


def home(request):
    # This function takes in a request and then returns HTML as Response
    try:
        article = Article()
        article.title = input('Enter the title: ')
        article.content = input('Enter content: ')
    except Article.DoesNotExist:
        # Handle the case where the article does not exist
        context = {
            "title": "Article Not Found",
            "content": "The article you are looking for does not exist.",
            "id": None  
        }
     
        html_string = render_to_string('myapp/base.html', context)


        return HttpResponse(html_string)
   
    context = {
        "title": article.title,
        "content": article.content,
        "id": article.id
    }

 
    return render(request,'myapp/base.html',context=context)


def abc(request):
    article = Article.objects.get(id=1)
    objects_queryset = Article.objects.all()
    context = {
        'objects': objects_queryset,
        "title" :article.title,
        "content" : article.content
    }

    try:
        return render(request, 'myapp/child.html', context)
    except TemplateDoesNotExist:
        return render(request, 'myapp/base.html',
        context=context)

