from django.urls import path
from .views import ProdukListCreateView, ProdukUpdateDestroyView, KategoriListView, StatusListView, CollectProductView

urlpatterns = [
  path('api/product', ProdukListCreateView.as_view(), name='produk-list-create'),
  path('api/product/<int:pk>', ProdukUpdateDestroyView.as_view(), name='produk-update-destroy'),
  path('api/category', KategoriListView.as_view(), name='kategori-list'),
  path('api/status', StatusListView.as_view(), name='status-list'),
  path('api/collect', CollectProductView.as_view(), name='collect-product'),
]