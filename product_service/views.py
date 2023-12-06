from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Kategori, Status, Produk
from .serializers import KategoriSerializer, StatusSerializer, ProdukSerializer
import requests

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
