from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),

]