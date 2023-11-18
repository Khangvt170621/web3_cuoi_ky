from django.shortcuts import render
from .forms import RegistrationForm
from quanlyphong.models import Phong
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    phong_trong = Phong.objects.filter(Tinhtrangphong=2)
    return render(request, 'login/index.html', {'phong_trong': phong_trong})

def register(request):
    form=RegistrationForm()
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'login/register.html',{'form':form})