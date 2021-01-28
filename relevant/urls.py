from django.urls import path
from . import views

app_name = 'relevant'

urlpatterns = [
    path('user/', views.UserList.as_view(), name='user_list'),
]