from django import forms
from .models import Khachhang

class KhachhangForm(forms.ModelForm):
    class Meta:
        model = Khachhang
        fields = ['Cccd', 'TenKhachHang', 'email', 'Sdt', 'DiaChi']

class SuaKhachHangForm(forms.ModelForm):
    class Meta:
        model = Khachhang
        fields = ['Cccd','TenKhachHang', 'email', 'Sdt', 'DiaChi']