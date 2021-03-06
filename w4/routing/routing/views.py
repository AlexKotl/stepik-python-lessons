from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def simple_route(request):
    code = 200 if request.method == 'GET' else 405
    return HttpResponse(status=code)
    
def slug_route(request, slug):
    return HttpResponse(slug)

def sum_route(request, first, second):
    return HttpResponse(int(first) + int(second))
    
@require_http_methods(['GET'])
def sum_get_method(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    
    if not a.replace('-', '').isdigit() or not b.replace('-', '').isdigit():
        return HttpResponse(status=400)
    
    return HttpResponse(int(a) + int(b))
    
@require_http_methods(['POST'])
def sum_post_method(request):
    a = request.POST.get('a', '')
    b = request.POST.get('b', '')
    
    if not a.replace('-', '').isdigit() or not b.replace('-', '').isdigit():
        return HttpResponse(status=400)
    
    return HttpResponse(int(a) + int(b))