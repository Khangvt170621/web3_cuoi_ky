from django.urls import path
from . import views

urlpatterns=[
    path('', views.loadphong, name="gallery"),
    path('detail', views.detail,name="detail"),
]