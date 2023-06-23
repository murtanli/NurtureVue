from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('about/',About.as_view(), name='about'),
    path('contact/',Contact.as_view(), name='contact'),
    path('login/',LoginUser.as_view(), name='login'),
    path('logout/',logout_user, name='logout'),
    path('Signup/',RegisterUser.as_view(), name='signup'),
    path('AddGreenHouse',addgrhs.as_view(), name='addgrhs'),
]