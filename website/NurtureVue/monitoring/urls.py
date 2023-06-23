from django.urls import path, re_path
from .views import *
from main import views

urlpatterns = [
    path('',profile, name='profile' ),
    path('update-data/', update_data, name='update_data'),
    path('map-data/', map_data, name='map_data'),
    path('test/', test, name='test'),
    path('save_db/',save_db.as_view(),name='save_db')
]