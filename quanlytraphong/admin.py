from django.contrib import admin
from .models import Hoadon, TinhtrangTT
# Register your models here.

class HoadonAdmin(admin.ModelAdmin):
    list_display = ['id','MaKH', 'MaPT', 'MaNV', 'Ngaythanhtoan','Tienphong','Tinhtrang']
    search_fields = ['MaKH','MaPT', 'MaNV']
class TinhtrangTTAdmin(admin.ModelAdmin):
    list_display = ['id', 'Tinhtrang']

admin.site.register(Hoadon, HoadonAdmin)
admin.site.register(TinhtrangTT, TinhtrangTTAdmin)