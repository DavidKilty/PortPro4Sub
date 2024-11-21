from django.contrib import admin
from django.urls import path
from myproject.mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logintipper/', views.logintipper, name='logintipper'),
    path('logintippee/', views.logintippee, name='logintippee'),
    path('signuptipper/', views.signuptipper, name='signuptipper'),
    path('signuptippee/', views.signuptippee, name='signuptippee'),
    path('tipper/<int:pk>/delete/', views.TipperDeleteView.as_view(), name='tipper_delete'),
]
