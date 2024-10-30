from django.urls import path
from myproject.mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
]
