from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Phong
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def loadphong(request):
    f=Phong.objects.all()
    context={'fm': f}
    return render(request, 'anhphong/gallery.html', context)

def detail(request):
    pid= request.GET.get('id')
    print("2",pid)
    p = get_object_or_404(Phong, pk=pid)
    context = {'fm': p}
    return render(request, 'datphong/phongdetail.html', context)

