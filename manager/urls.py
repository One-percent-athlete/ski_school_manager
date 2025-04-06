from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule/', views.schedule, name='schedule'),

    path('register_user/', views.register_user, name="register_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('delete_user/<int:user_id>/', views.delete_user, name="delete_user"),

    path('profile_list/', views.profile_list, name="profile_list"),
    path('update_profile/<int:profile_id>/', views.update_profile, name="update_profile"),

    path('add_lesson/', views.add_lesson, name="add_lesson"),
]
