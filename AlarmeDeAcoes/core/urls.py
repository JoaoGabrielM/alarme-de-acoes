from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
]
