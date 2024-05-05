from django.db import models

# Create your models here.
class Siswa(models.Model):
    nama = models.CharField(max_length=255)
    npm = models.IntegerField(unique=True)
    kelas = models.CharField(max_length=255)
    def __str__(self):
        return self.nama

class Guru(models.Model):
    nama = models.CharField(max_length=255)
    nip = models.IntegerField()
    def __str__(self):
        return self.nama

class Absensi(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, related_name='absensi')
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, related_name='absensi')
    tanggal = models.DateField()
    hadir = models.BooleanField(default=True)

    def __str__(self):
        return self.siswa     

class JadwalPelajaran(models.Model):
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, related_name='jadwal')
    pelajaran = models.CharField(max_length=255)
    jam_mulai = models.CharField(max_length=255)
    jam_selesai = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)

    def __str__(self):
        return self.pelajaran