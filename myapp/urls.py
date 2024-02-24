
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('gallery/', views.images),
    path('contact/', views.contact),
    path('about/', views.about),
    path('collection/', views.collection),
    path('assignment/', views.assignment),
]
