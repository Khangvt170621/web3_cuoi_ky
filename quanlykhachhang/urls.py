from django.urls import path
from . import views

urlpatterns = [
    # Các url khác của ứng dụng
    path('', views.them_khach_hang, name='thongtinkh'),
    path('suattkh/', views.sua_thong_tin_khach_hang, name='suatt')
]
