# views.py
from django.shortcuts import render, redirect
from .forms import DatPhongForm
from .models import PhieuDatPhong

def dat_phong(request):
    ma_phong = request.GET.get('id')
    print(ma_phong)
    if not ma_phong:
        # Xử lý trường hợp không có giá trị MaPhong được truyền vào
        return redirect('index')  # Chẳng hạn, chuyển hướng về trang chủ

    # Lấy thông tin người dùng đăng nhập và mã khách hàng
    if request.user.is_authenticated:
        ma_khach_hang = request.user.khachhang.Cccd
    else:
        # Xử lý trường hợp người dùng không đăng nhập
        return redirect('login')  # Chẳng hạn, chuyển hướng đến trang đăng nhập

    if request.method == 'post':
        form = DatPhongForm(request.POST)
        if form.is_valid():
            phieu_dat_phong = form.save(commit=False)
            phieu_dat_phong.save()
            return redirect('phieudat')
    else:
        form = DatPhongForm(initial={'MaPhong': ma_phong, 'MaKH': ma_khach_hang})

    return render(request, 'datphong/datphong.html', {'form': form})


def phieu(request):
    user = request.user
    if hasattr(user, 'khachhang'):
        ma_khach_hang = user.khachhang.Cccd

        # Lấy danh sách phiếu đặt của khách hàng đó
        phieu_dat_list = PhieuDatPhong.objects.filter(MaKH=ma_khach_hang)

        return render(request, 'datphong/dsphieu.html', {'phieu': phieu_dat_list})
    else:
        # Xử lý trường hợp user không có khách hàng liên kết
        return render(request, 'thongtinuser/thongtinkh.html')