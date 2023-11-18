from django.contrib import admin
from .models import TinhTrangPhong, Phong, LoaiPhong,SoGiuong

# Register your models here.

class PhongAdmin(admin.ModelAdmin):
    list_display = ['Maphong', 'Loaiphong', 'Giaphong','Sogiuong', 'Anhphong','Tinhtrangphong']
    search_fields = ['Loaiphong', 'Giaphong']


admin.site.register(TinhTrangPhong)
admin.site.register(Phong, PhongAdmin)
admin.site.register(LoaiPhong)
admin.site.register(SoGiuong)