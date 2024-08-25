from .views import *
from django.urls import path, include

urlpatterns = [
    path('',
         BlogView.as_view(),
         name='blog'),
]
