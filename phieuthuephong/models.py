from django.db import models
from phieudatphong.models import PhieuDatPhong

# Create your models here.
class TinhtrangPT(models.Model):
    tinhtrang=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.tinhtrang

class Phieuthuephong(models.Model):
    Maphieudat=models.ForeignKey(PhieuDatPhong,on_delete=models.CASCADE)
    Ngayden=models.DateField(null=False)
    Ngaydi=models.DateField(null=False)
    tinhtrangPT=models.ForeignKey(TinhtrangPT,on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.id)

