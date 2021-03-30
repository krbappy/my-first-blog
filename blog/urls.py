from django.urls import path
from . import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
