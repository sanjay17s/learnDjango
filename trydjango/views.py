'''The `views.py` file in a Django project is responsible for rendering HTML 
web pages. When a user requests a specific URL (e.g., `/home`), Django maps the
 URL to a function in `views.py`. This function receives the request,
  processes it, and returns the appropriate HTML response.'''

from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
import random


def home(request):
    # This function takes in a request and then returns HTML as Response
    try:
        article = Article.objects.get(id=3)
    except Article.DoesNotExist:
        # Handle the case where the article does not exist
        context = {
            "title": "Article Not Found",
            "content": "The article you are looking for does not exist.",
            "id": None  
        }
        return render(request, 'myapp/some_file.html', context)
   
    context = {
        "title": article.title,
        "content": article.content,
        "id": article.id
    }
 
    return render(request, 'myapp/some_file.html', context)


def abc(request):
    res = "hignkfs"
    return HttpResponse(res)
