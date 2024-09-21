from django.urls import path
from . import views

urlpatterns = [
    path('',views.speak_hindi, name='speak_hindi'),
]
