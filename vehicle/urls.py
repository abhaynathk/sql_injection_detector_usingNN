
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path,include


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('',include('vehicleapp.urls')),
]
