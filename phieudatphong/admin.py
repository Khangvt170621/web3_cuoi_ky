from django.contrib import admin
from .models import PhieuDatPhong
# Register your models here.

class PhieudatAdmin(admin.ModelAdmin):
    list_display = ['id','MaKH', 'MaPhong', 'NgayNhan', 'NgayTra']
    search_fields = ['MaKH']

admin.site.register(PhieuDatPhong,PhieudatAdmin)