'''the goal of this file is to render html web pages
from my understanding we have some url say ..../home
when this is requested by the user
in django some file will catch this request,i mean some mapping will be 
there to service this kind of request
request will have some metadata 
and this function which acts as a receiver of this request routes this to views.py'''

from django.shortcuts import render
from django.http import HttpResponse

HTML_STRING="""
<h1>Hello World</h1>"""

def home(request):
# this function takes in a request and then returns a html as Response
    return HttpResponse(HTML_STRING)
