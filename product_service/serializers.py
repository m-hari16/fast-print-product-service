from rest_framework import serializers
from .models import Kategori, Status, Produk

class KategoriSerializer(serializers.ModelSerializer):
  class Meta:
    model = Kategori
    fields = ('id_kategori', 'nama_kategori')

class StatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Status
    fields = ('id_status', 'nama_status')

class ProdukSerializer(serializers.ModelSerializer):
  kategori_id = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all(), write_only=True)
  status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), write_only=True)
  kategori = serializers.StringRelatedField(source='kategori.nama_kategori', read_only=True)
  status = serializers.StringRelatedField(source='status.nama_status', read_only=True)

  class Meta:
    model = Produk
    fields = ['id_produk', 'nama_produk', 'harga', 'kategori_id', 'status_id', 'kategori', 'status']

  def validate(self, data):
    if not data.get('nama_produk'):
      raise serializers.ValidationError({'nama_produk': 'Nama Produk cannot be blank.'})

    if data.get('harga') is None:
      raise serializers.ValidationError({'harga': 'Harga cannot be null.'})

    if not data.get('kategori_id'):
      raise serializers.ValidationError({'kategori_id': 'Kategori ID cannot be blank.'})

    if not data.get('status_id'):
      raise serializers.ValidationError({'status_id': 'Status ID cannot be blank.'})

    return data

  def to_representation(self, instance):
    return {
      'id_produk': instance.id_produk,
      'nama_produk': instance.nama_produk,
      'harga': instance.harga,
      'kategori': instance.kategori_id.nama_kategori if instance.kategori_id else None,
      'status': instance.status_id.nama_status if instance.status_id else None,
    }
