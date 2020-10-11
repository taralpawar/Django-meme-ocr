
from django.urls import path
from .views import recognise
urlpatterns = [
    path('', recognise),
]
