# trong file views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import KhachhangForm, SuaKhachHangForm
from .models import TinhTrang, Khachhang

def them_khach_hang(request):
    # Lấy thông tin khách hàng nếu có
    khachhang = None
    if request.user.is_authenticated:
        try:
            khachhang = Khachhang.objects.get(user=request.user)
        except Khachhang.DoesNotExist:
            pass

    if request.method == 'POST':
        form = KhachhangForm(request.POST)
        if form.is_valid():
            # Lưu khách hàng mới với tình trạng mặc định là "chưa có phòng"
            khachhang = form.save(commit=False)
            
            # Lấy hoặc tạo TinhTrang "chưa có phòng"
            tinhtrang_chua_co_phong, created = TinhTrang.objects.get_or_create(Tinhtrang='Chưa có phòng')
            
            khachhang.Tinhtrang = tinhtrang_chua_co_phong
            
            # Gán user là user đang đăng nhập
            khachhang.user = request.user if request.user.is_authenticated else None
            khachhang.save()
            return redirect('thongtinkh')
    else:
        form = KhachhangForm(instance=khachhang) if khachhang else KhachhangForm()

    return render(request, 'thongtinkh.html', {'form': form, 'khachhang': khachhang})

def sua_thong_tin_khach_hang(request):
    # khach_hang = get_object_or_404(Khachhang, Cccd=cccd)
    makh = request.GET.get('id')

    if request.method == 'POST':
        form = SuaKhachHangForm(request.POST)
        if form.is_valid():
            suatt=form.save(commit=False)
            suatt.save()
            return redirect('thongtinkh')
    else:
        form = SuaKhachHangForm(initial={'Cccd': makh})

    return render(request, 'suatt.html', {'form': form})