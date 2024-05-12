from rest_framework import serializers
from api.models import Absensi, Guru, Siswa, JadwalPelajaran

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = '__all__'
class SiswaSerializer(serializers.ModelSerializer):
    absensi = AbsensiSerializer(many=True, read_only=True)
    class Meta:
        model = Siswa
        fields = ['id', 'nama', 'npm', 'kelas', 'absensi']


class GuruSerializer(serializers.HyperlinkedModelSerializer):
    absensi = serializers.HyperlinkedIdentityField(view_name='guru_detail')
    class Meta:
        model = Guru
        fields = ['id', 'nama', 'nip', 'absensi']


class JadwalPelajaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalPelajaran
        fields = '__all__'