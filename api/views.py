from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from api.serializers import SiswaSerializer, GuruSerializer, AbsensiSerializer, JadwalPelajaranSerializer
from api.models import Siswa, Guru, Absensi, JadwalPelajaran

class SiswaList(generics.ListCreateAPIView):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def siswa_detail(request, pk):
    try:
        siswa = Siswa.objects.get(pk=pk)
    except Siswa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SiswaSerializer(siswa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SiswaSerializer(siswa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        siswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GuruList(generics.ListCreateAPIView):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def guru_detail(request, pk):
    try:
        guru = Guru.objects.get(pk=pk)
    except Guru.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuruSerializer(guru, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GuruSerializer(guru, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guru.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AbsensiList(generics.ListCreateAPIView):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def absensi_detail(request, pk):
    try:
        absensi = Absensi.objects.get(pk=pk)
    except Absensi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AbsensiSerializer(absensi)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AbsensiSerializer(absensi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        absensi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JadwalPelajaranList(generics.ListCreateAPIView):
    queryset = JadwalPelajaran.objects.all()
    serializer_class = JadwalPelajaranSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def jadwal_detail(request, pk):
    try:
        jadwal = JadwalPelajaran.objects.get(pk=pk)
    except JadwalPelajaran.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JadwalPelajaranSerializer(jadwal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JadwalPelajaranSerializer(jadwal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        jadwal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
