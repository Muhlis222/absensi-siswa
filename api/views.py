from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from api.serializers import SiswaSerializer
from api.models import Siswa

class SiswaList(generics.ListCreateAPIView):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer

class SiswaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer

