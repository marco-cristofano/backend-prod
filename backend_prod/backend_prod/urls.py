from django.contrib import admin
from django.urls import path
from api.api import PongView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', PongView.as_view(), name='ping'),
]
