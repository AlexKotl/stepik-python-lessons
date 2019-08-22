from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def echo(request):
    # print(request.GET)
    return render(request, 'echo.html', {
        'statement': request.META.get('X-Print-Statement', ''),
        'get': request.GET.items(),
        'post': request.POST.items()
    })


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
