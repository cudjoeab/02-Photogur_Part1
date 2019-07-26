from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from photogur.models import Picture, Comment

# def root_path(request):
#     return HttpResponseRedirect('')

def pictures(request):
    response = render(request, 'pictures.html')
    return HttpResponse(response)

