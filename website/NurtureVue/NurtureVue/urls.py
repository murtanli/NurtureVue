
from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
]
