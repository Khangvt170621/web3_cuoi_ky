from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TinhTrang(models.Model):
    Tinhtrang=models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.Tinhtrang

class Khachhang(models.Model):
    Cccd=models.CharField(max_length=12, primary_key=True)
    TenKhachHang=models.CharField(max_length=50,null=False)
    email=models.EmailField(null=False, unique=True)
    Sdt=models.CharField(max_length=10,null=False, unique=True)
    DiaChi=models.CharField(max_length=120,null=False)
    Tinhtrang=models.ForeignKey(TinhTrang, on_delete=models.CASCADE)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Cccd