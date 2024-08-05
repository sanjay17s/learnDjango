'''the goal of this file is to render html web pages
from my understanding we have some url say ..../home
when this is requested by the user
in django some file will catch this request,i mean some mapping will be 
there to service this kind of request
request will have some metadata 
and this function which acts as a receiver of this request routes this to views.py'''

from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    # This function takes in a request and then returns HTML as Response
    name = "sanjay"
    num = random.randint(10, 7899)
    HTML_STRING = f"""
    <h1>Hello {name.title()} - {num}</h1>"""
    return HttpResponse(HTML_STRING)

def abc(request):
    res = "hignkfs"
    return HttpResponse(res)
