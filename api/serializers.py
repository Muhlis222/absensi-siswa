from rest_framework import serializers
from api.models import Absensi, Guru, Siswa, JadwalPelajaran

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'


    