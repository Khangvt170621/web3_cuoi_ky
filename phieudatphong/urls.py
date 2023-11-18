from django.urls import path
from . import views

urlpatterns=[
    path('', views.dat_phong, name="datphong"),
    path('phieu/', views.phieu, name="phieudat")
]