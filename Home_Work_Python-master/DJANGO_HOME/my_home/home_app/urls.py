from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.get_basic, name='base'),
    path('register/', views.register, name='register'),
    path('after_register/', views.after_register, name='after_register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('page-one/', views.page_one, name='page_one'),
    path('page-second/', views.page_second, name='page'),
]
