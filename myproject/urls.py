from django.contrib import admin
from django.urls import path, include
from myproject.mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logintipper/', views.logintipper, name='logintipper'),
    path('logintippee/', views.logintippee, name='logintippee'),
    path('logout/', views.logout_view, name='logout'),
    path('signuptipper/', views.signuptipper, name='signuptipper'),
    path('signuptippee/', views.signuptippee, name='signuptippee'),
    path('tipper_homepage/', views.tipper_homepage, name='tipper_homepage'),
    path('tippee_homepage/', views.tipper_homepage, name='tippee_homepage'),
    path('tipper/<int:pk>/delete/', views.TipperDeleteView.as_view(), name='tipper_delete'),
    path('logout/', views.logout_view, name='logout'),
]
 