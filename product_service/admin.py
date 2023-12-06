from django.contrib import admin
from .models import Produk, Kategori, Status

# Register your models here.
class ProdukAdmin(admin.ModelAdmin):
  list_display = ('id_produk', 'nama_produk', 'harga', 'formatted_kategori', 'formatted_status')

  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    return queryset.filter(status_id__id_status=1)

  def formatted_kategori(self, obj):
    return obj.kategori_id.nama_kategori if obj.kategori_id else None

  formatted_kategori.short_description = 'Kategori'

  def formatted_status(self, obj):
    return obj.status_id.nama_status if obj.status_id else None

  formatted_status.short_description = 'Status'

class KategoriAdmin(admin.ModelAdmin):
  list_display = ('id_kategori', 'nama_kategori')

class StatusAdmin(admin.ModelAdmin):
  list_display = ('id_status', 'nama_status')

admin.site.register(Produk, ProdukAdmin)
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Status, StatusAdmin)