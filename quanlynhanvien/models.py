from django.db import models

# Create your models here.
class Nhanvien(models.Model):
    MaNV=models.CharField(primary_key=True, max_length=5)
    TenNV=models.CharField(max_length=50, null=False)
    Cccd=models.CharField(max_length=12, null=False, unique=True)
    Mst=models.CharField(max_length=10, null=False, unique=True)
    email=models.EmailField(null=False, unique=True)
    Sdt=models.CharField(max_length=10,null=False, unique=True)
    DiaChi=models.CharField(max_length=120,null=False)

    def __str__(self):
        return self.MaNV