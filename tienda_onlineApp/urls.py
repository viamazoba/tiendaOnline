from django.urls import path

from tienda_onlineApp import views

urlpatterns = [
    
    path("", views.home, name = 'Home'),
    path("service/", views.service, name = 'Service'),
    path("store/", views.store, name = 'Store'),
    path("blog/", views.blog, name = 'Blog'),
    path("contact", views.contact, name = 'Contact'),
]