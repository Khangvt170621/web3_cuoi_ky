# trong file forms.py
from django.utils import timezone
from django import forms
from .models import PhieuDatPhong
from django.forms import DateField 

class DatPhongForm(forms.ModelForm):
    class Meta:
        model = PhieuDatPhong
        fields = ['MaPhong', 'MaKH', 'NgayNhan', 'NgayTra']
        widgets = {
        'NgayNhan': forms.DateInput(attrs={'type': 'date', 'min': str(timezone.now() + timezone.timedelta(hours=7)).split()[0]}),
        'NgayTra': forms.DateInput(attrs={'type': 'date','min': str(timezone.now() + timezone.timedelta(hours=7)).split()[0]}),
        }

    def clean(self):
        cleaned_data = super().clean()
        ngay_nhan = cleaned_data.get('NgayNhan')
        ngay_tra = cleaned_data.get('NgayTra')

        if ngay_nhan and ngay_tra and ngay_tra <= ngay_nhan:
            raise forms.ValidationError('Ngày trả phải sau ngày nhận ít nhất một ngày.')

        return cleaned_data
