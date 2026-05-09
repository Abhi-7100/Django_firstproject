from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Registration
from .serializers import RegistrationSerializer
# Create your views here.

class RegistrationCreate(APIView):
    def post(self, request):
        Y = RegistrationSerializer(data=request.data)
        if Y.is_valid():
            Y.save()
            return Response(Y.data, status = status.HTTP_201_CREATED)
        return Response(Y.errors, status = status.HTTP_400_BAD_REQUEST)
    
class RegistrationGET(APIView):
    def get(self, request):
        X = Registration.objects.all()
        Y = RegistrationSerializer(X, many=True)
        return Response(Y.data, status = status.HTTP_202_ACCEPTED)
    
class RegistrationGETbyID(APIView):
    def get(self, request, id):
        try:
            x = Registration.objects.get(id=id)
            y = RegistrationSerializer(x)
            return Response(y.data, status = status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response("error:not found", status=status.HTTP_404_NOT_FOUND)
        
class RegistrationGETbyemail(APIView):
    def get(self, request, email):
        try:
            x = Registration.objects.get(email=email)
            y = RegistrationSerializer(x)
            return Response(y.data, status = status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response("error:Not Found", status = status.HTTP_404_NOT_FOUND)
        
class RegistrationUpdate(APIView):
    def put(self, request, id):
        try:
            x = Registration.objects.get(id=id)
            y = RegistrationSerializer(x, data=request.data)
            if y.is_valid():
                y.save()
                return Response(y.data, status=status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response("error:Not Found", status=status.HTTP_400_BAD_REQUEST)
        
class Registrationpatch(APIView):
    def patch(self, request, id):
        try:
            x = Registration.objects.get(id=id)
            y = RegistrationSerializer(x, data=request.data, partial=True)
            if y.is_valid():
                y.save()
                return Response(y.data, status=status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response("error:Not Found", status=status.HTTP_400_BAD_REQUEST)
        
class RegistrationDelete(APIView):
    def delete(self, request, id):
        try:
            x = Registration.objects.get(id =id)
            x.delete()
            return Response("Deleted successfully", status=status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response("error:Not Found", status=status.HTTP_400_BAD_REQUEST)
