from django.db import models

# Create your models here.
class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=255)
    tingkat = models.IntegerField()

class Siswa(models.Model):
    nama = models.CharField(max_length=255)
    nisn = models.CharField(max_length=20, unique=True)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)

class Absensi(models.Model):
    tanggal = models.DateField()
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    status_kehadiran = models.CharField(max_length=10)
    catatan = models.TextField(blank=True)