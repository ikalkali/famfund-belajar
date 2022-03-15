from django.db import models

# Create your models here.
class Asisten(models.Model):
    nim = models.CharField(max_length=30, primary_key=True, null=False)
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tagihan = models.IntegerField()

class Pembayaran(models.Model):
    nim = models.ForeignKey(Asisten, related_name="asisten", on_delete=models.CASCADE)
    nominal = models.IntegerField()
    tanggal_bayar = models.DateTimeField()
