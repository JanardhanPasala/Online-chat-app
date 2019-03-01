from . import views
from django.urls import path

urlpatterns=[
        path('', views.login_view, name='login'),
        path('register', views.register, name='register'),
        path('user', views.all_user, name='all_user'),
        path('chat/<id>', views.chat, name='chat'),
        path('logout', views.login_view, name='logout'),
        path('com', views.com, name= 'com'),
        path('receive_data', views.receive_data, name='receive_data'),
        ]