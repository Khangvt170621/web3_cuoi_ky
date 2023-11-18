from django.contrib import admin
from .models import Nhanvien
# Register your models here.

class NhanvienAdmin(admin.ModelAdmin):
    list_display = ['MaNV','TenNV', 'Cccd', 'Mst', 'email','Sdt','DiaChi']
    search_fields = ['MaNV','TenNV', 'Cccd']

admin.site.register(Nhanvien, NhanvienAdmin)