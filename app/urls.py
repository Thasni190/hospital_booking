from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('departments/',views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact')
]
