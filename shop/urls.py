from django.urls import path
from shop.views import *


urlpatterns = [
    path('', index, name='index'),
   
]
