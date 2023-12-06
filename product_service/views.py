from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Kategori, Status, Produk
from .serializers import KategoriSerializer, StatusSerializer, ProdukSerializer
import requests
import hashlib

# Create your views here.

class ProdukListCreateView(generics.ListCreateAPIView):
  queryset = Produk.objects.all()
  serializer_class = ProdukSerializer

class ProdukUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Produk.objects.all()
  serializer_class = ProdukSerializer

class KategoriListView(generics.ListAPIView):
  queryset = Kategori.objects.all()
  serializer_class = KategoriSerializer

class StatusListView(generics.ListAPIView):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer

class CollectProductView(APIView):
  def post(self, request, *args, **kwargs):
    # Make a request to the third-party API to collect data
    api_url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    api_username = request.data.get('username')
    api_password = request.data.get('password')
    hashedPass = hashlib.md5(api_password.encode('utf-8')).hexdigest()

    response = requests.post(api_url, data={'username': api_username, 'password': hashedPass})
    
    if response.status_code != 200:
      return Response({'error': 'Failed to fetch data from the third-party API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Extract data from the response
    data = response.json()

    # Group and save data to the database
    self.save_data_to_database(data['data'])

    return Response({'success': 'Data collected and saved successfully'}, status=status.HTTP_200_OK)

  def save_data_to_database(self, data):
    # Group kategori and status data
    kategori_data = set(item['kategori'] for item in data)
    status_data = set(item['status'] for item in data)

    # Save kategori and status to the database
    self.save_kategori_data(kategori_data)
    self.save_status_data(status_data)

    # Save produk data with kategori_id and status_id
    self.save_produk_data(data)

  def save_kategori_data(self, kategori_data):
    for nama_kategori in kategori_data:
      Kategori.objects.get_or_create(nama_kategori=nama_kategori)

  def save_status_data(self, status_data):
    for nama_status in status_data:
      Status.objects.get_or_create(nama_status=nama_status)

  def save_produk_data(self, produk_data):
    for item in produk_data:
      kategori, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
      status, _ = Status.objects.get_or_create(nama_status=item['status'])

      Produk.objects.create(
        nama_produk=item['nama_produk'],
        harga=item['harga'],
        kategori_id=kategori,
        status_id=status
      )