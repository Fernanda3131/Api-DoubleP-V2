from django.urls import path
from .views import login_view, register_view

urlpatterns = [
    path('register/', register_view.register_user, name='api_register'),
    path('login/', login_view.login_user, name='api_login'),
    path('logout/', login_view.logout_user, name='api_logout'),
]