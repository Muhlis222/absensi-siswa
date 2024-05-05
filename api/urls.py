
from django.urls import path
from api.views import SiswaList, GuruList, AbsensiList, JadwalPelajaranList, siswa_detail, guru_detail

urlpatterns = [
    path('siswa/', SiswaList.as_view()),
    path('siswa/<int:pk>/', siswa_detail),
    path('guru/', GuruList.as_view()),
    path('guru/<int:pk>/', guru_detail, name='guru_detail'),
    path('absensi/', AbsensiList.as_view()),
    path('absensi/<int:pk>/', siswa_detail, name='absensi_detail'),
    path('jadwal/', JadwalPelajaranList.as_view()),
    path('jadwal/<int:pk>/', siswa_detail),

]