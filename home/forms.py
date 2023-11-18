from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from quanlyphong.models import Phong
import re

class CustomPasswordInput(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs['class'] = 'form-control'
        kwargs['attrs'] = attrs
        super().__init__(*args, **kwargs)

class RegistrationForm(forms.Form):
    username=forms.CharField(label="Tài khoản", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    firstname=forms.CharField(label="First name ", max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname=forms.CharField(label="Last name ", max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label="Mật khẩu", widget=CustomPasswordInput())
    password2=forms.CharField(label="Nhập lại mật khẩu", widget=CustomPasswordInput())
    
    def clean(self):
        cleaned_data = super().clean() 
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password!=password2:
            raise forms.ValidationError("Mật khẩu không hợp lệ")
        return cleaned_data
    
    def clean_username(self):
        username=self.cleaned_data['username']

        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],first_name=self.cleaned_data['firstname'],last_name=self.cleaned_data['lastname'],
                                 email= self.cleaned_data['email'], password=self.cleaned_data['password2'])
        
class LoadPhong(forms.Form):
    class Meta():
        model= Phong()