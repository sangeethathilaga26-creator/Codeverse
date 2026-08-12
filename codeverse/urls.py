from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
path('', views.home, name='home'),
path('signup/', views.signup_view, name='signup'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('update-status/<int:topic_id>/', views.update_status, name='update_status'),
]