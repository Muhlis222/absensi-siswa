from rest_framework import serializers
from api.models import Absensi, Guru, Siswa, JadwalPelajaran

class AbsensiSerializer(serializers.ModelSerializer):
    # siswa = SiswaSerializer(read_only=True)
    # guru = GuruSerializer(read_only=True)
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

    #absensi = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='guru_detail')
    # absensi = AbsensiSerializer(many=True, read_only=True)
    class Meta:
        model = Guru
        fields = ['id', 'nama', 'nip', 'absensi']


class JadwalPelajaranSerializer(serializers.ModelSerializer):
    # guru = GuruSerializer(read_only=True)
    class Meta:
        model = JadwalPelajaran
        fields = '__all__'