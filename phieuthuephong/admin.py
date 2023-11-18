from django.contrib import admin
from .models import TinhtrangPT, Phieuthuephong
# Register your models here.
class PhieuthueAdmin(admin.ModelAdmin):
    list_display = ['id','Maphieudat', 'Ngayden', 'Ngaydi', 'tinhtrangPT']
    search_fields = ['Maphieudat','tinhtrangPT']


admin.site.register(Phieuthuephong, PhieuthueAdmin)
admin.site.register(TinhtrangPT)