from django.urls import path

from .views import see

app_name = "leads"

urlpatterns = [
    path('', see),
]