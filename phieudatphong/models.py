from django.db import models
from quanlykhachhang.models import Khachhang
from quanlyphong.models import Phong
# Create your models here.

class PhieuDatPhong(models.Model):
    MaKH=models.ForeignKey(Khachhang,on_delete=models.CASCADE)
    MaPhong=models.ForeignKey(Phong,on_delete=models.CASCADE )
    NgayNhan=models.DateField(null=False)
    NgayTra=models.DateField(null=False)

    def __str__ (self):
        return str(self.id)