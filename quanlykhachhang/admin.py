from django.contrib import admin
from .models import Khachhang,TinhTrang
# Register your models here.
class KhachhangAdmin(admin.ModelAdmin):
    list_display = ['Cccd','TenKhachHang', 'email', 'Sdt', 'DiaChi','Tinhtrang']
    search_fields = ['Cccd','TenKhachHang', 'Sdt']


admin.site.register(Khachhang, KhachhangAdmin)
admin.site.register(TinhTrang)
