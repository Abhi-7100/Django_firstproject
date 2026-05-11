from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Registration
from .serializers import RegistrationSerializer
# Create your views here.

class RegistrationCreate(APIView):
    def post(self, request):
        y = RegistrationSerializer(data = request.data)
        if y.is_valid():
            y.save()
            return Response(y.data, status=status.HTTP_200_OK)
        return Response(y.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegistrationGET(APIView):
    def get(self, request):
        x = Registration.objects.all()
        y = RegistrationSerializer(x, many=True)
        return Response(y.data, status = status.HTTP_202_ACCEPTED)

class RegistrationGETbyID(APIView):
    def get(self, request, id):
        try:
            x = Registration.objects.get(id=id)
            y=RegistrationSerializer(x)
            return Response(y.data, status=status.HTTP_202_ACCEPTED)
        except Registration.DoesNotExist:
            return Response("error: Registration not found",status=status.HTTP_404_NOT_FOUND)
        
class RegistrationGETbyName(APIView):
    def get(self, request, name):
        try:
            x = Registration.objects.get(name=name)
            y= RegistrationSerializer(x)
            return Response(y.data, status=status.HTTP_202_ACCEPTED)
        except Registration.DoesNotExist:
            return Response("error: Registration not found", status=status.HTTP_404_NOT_FOUND)

class RegistrationUpdate(APIView):
    def put(self, request, id):
        try:
            x = Registration.objects.get(id=id)
            y = RegistrationSerializer(x, data=request.data)
            if y.is_valid():
                y.save()
                return Response(y.data, status=status.HTTP_200_OK)
            return Response(y.errors, status=status.HTTP_400_BAD_REQUEST)
        except Registration.DoesNotExist:
            return Response("error: Registration not found", status=status.HTTP_404_NOT_FOUND)
        
class RegistrationDelete(APIView):
    def delete(self, request, id):
        try:
            x = Registration.objects.get(id=id)
            x.delete()
            return Response("Registration deleted successfully", status=status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response("error : Registration not found", status=status.HTTP_404_NOT_FOUND)
        
class RegistrationPatch(APIView):
    def patch(self, request, id):
        try:
            x = Registration.objects.get(id=id)
            y = RegistrationSerializer(x, data=request.data, partial=True)
            if y.is_valid():
                y.save()
                return Response(y.data, status=status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response("error : Registration not found", status=status.HTTP_404_NOT_FOUND)

