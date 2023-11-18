from django.db import models
from quanlynhanvien.models import Nhanvien
from phieuthuephong.models import Phieuthuephong
from quanlykhachhang.models import Khachhang
# Create your models here.
class TinhtrangTT(models.Model):
    Tinhtrang=models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.Tinhtrang


class Hoadon(models.Model):
    MaKH=models.ForeignKey(Khachhang,on_delete=models.CASCADE)
    MaPT=models.ForeignKey(Phieuthuephong,on_delete=models.CASCADE)
    MaNV=models.ForeignKey(Nhanvien, on_delete=models.CASCADE)
    Ngaythanhtoan=models.DateField(auto_now_add=True, null=False)
    Tienphong=models.IntegerField(null=False)
    Tinhtrang=models.ForeignKey(TinhtrangTT,on_delete=models.CASCADE)

