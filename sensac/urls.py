from django.urls import path

from sensac.views import home

urlpatterns = [
    path('', home),
]
 