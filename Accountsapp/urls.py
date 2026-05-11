from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationCreate.as_view()),
    path('registerget/',RegistrationGET.as_view()),
    path('registergetbyid/<int:id>/', RegistrationGETbyID.as_view()),
    path('registergetbyname/<str:name>/', RegistrationGETbyName.as_view()),
    path('registerupdate/<int:id>/', RegistrationUpdate.as_view()),
    path('registerdelete/<int:id>/', RegistrationDelete.as_view()),
    path('registerpatch/<int:id>/', RegistrationPatch.as_view()),
]