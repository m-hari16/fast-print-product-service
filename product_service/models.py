from django.db import models

# Create your models here.

class Kategori(models.Model):
  id_kategori = models.AutoField(primary_key=True)
  nama_kategori = models.CharField(max_length=50)

class Status(models.Model):
  id_status = models.AutoField(primary_key=True)
  nama_status = models.CharField(max_length=30)

class Produk(models.Model):
  id_produk = models.AutoField(primary_key=True)
  nama_produk = models.CharField(max_length=255)
  harga = models.CharField(max_length=15)
  kategori_id = models.ForeignKey(Kategori, on_delete = models.CASCADE)
  status_id = models.ForeignKey(Status, on_delete = models.CASCADE)
  
