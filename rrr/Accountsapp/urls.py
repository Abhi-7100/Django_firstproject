from django.urls import path
from .views import *
urlpatterns = [
    path('register/',RegistrationCreate.as_view()),
    path('registerget/',RegistrationGET.as_view()),
    path('registergetid/<int:id>/',RegistrationGETbyID.as_view()),
    path('registergetemail/<str:email>/',RegistrationGETbyemail.as_view()),
    path('registerupdate/<int:id>/',RegistrationUpdate.as_view()),
    path('registerpatch/<int:id>/',Registrationpatch.as_view()),
    path('registerdelete/<int:id>/',RegistrationDelete.as_view()),
    ]