
from django.contrib import admin
from django.urls import path, include

import monitoring
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('profile/', include('monitoring.urls'))
]
