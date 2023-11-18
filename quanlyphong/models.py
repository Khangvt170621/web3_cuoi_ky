from django.db import models

# Create your models here.
class TinhTrangPhong(models.Model):
    Tinhtrang=models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.Tinhtrang

class LoaiPhong(models.Model):
    Loaiphong=models.CharField(max_length=150, null=False, unique=True)

    def __str__(self):
        return self.Loaiphong
    
class SoGiuong(models.Model):
    Sogiuong=models.CharField(max_length=150, null=False, unique=True)

    def __str__(self):
        return self.Sogiuong

class Phong(models.Model):
    Maphong=models.CharField(max_length=5, primary_key=True)
    Loaiphong=models.ForeignKey(LoaiPhong,on_delete=models.CASCADE, null=False)
    Sogiuong=models.ForeignKey(SoGiuong,on_delete=models.CASCADE, null=True)
    Giaphong=models.IntegerField(null=False)
    Anhphong=models.ImageField(upload_to='uploads/phong/', default=None)
    Tinhtrangphong=models.ForeignKey(TinhTrangPhong, on_delete=models.CASCADE, related_name='phong', null=False)
    describe=models.TextField(null=True)

    def __str__(self):
        return self.Maphong


