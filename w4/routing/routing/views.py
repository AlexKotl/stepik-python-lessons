from django.shortcuts import render
from django.http import HttpResponse

def simple_route(request):
    code = 200 if request.method == 'GET' else 405
    return HttpResponse('', status=code)
    
def slug_route(request, slug):
    return HttpResponse(slug)

def sum_route(request, first, second):
    return HttpResponse(int(first) + int(second))