from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule/', views.schedule, name='schedule'),

    path('login_user/', views.login_user, name="login_user"),
]
