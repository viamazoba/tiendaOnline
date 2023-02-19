from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'tienda_onlineApp/home.html')


def service(request):
    return HttpResponse('servicios')


def store(request):
    return HttpResponse('tienda')


def blog(request):
    return HttpResponse('blog')


def contact(request):
    return HttpResponse('contato')
