from django.contrib import admin
from django.urls import path, include
from myproject.mainapp import views

urlpatterns = [
    path('tipper_list/', views.tipper_list, name='tipper_list'),
    path('tipper_jar/<int:user_id>/', views.tipper_jar, name='tipper_jar'),
    path('tippee_jar/<int:user_id>/', views.tippee_jar, name='tippee_jar'),
    path('leave_tip/<int:user_id>/', views.leave_tip, name='leave_tip'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logintipper/', views.logintipper, name='logintipper'),
    path('logintippee/', views.logintippee, name='logintippee'),
    path('logout/', views.logout_view, name='logout'),
    path('signuptipper/', views.signuptipper, name='signuptipper'),
    path('signuptippee/', views.signuptippee, name='signuptippee'),
    path('tipper_homepage/', views.tipper_homepage, name='tipper_homepage'),
    path('tippee_homepage/', views.tippee_homepage, name='tippee_homepage'),
    path('delete_tip/<int:tip_id>/', views.delete_tip, name='delete_tip'),
]

 