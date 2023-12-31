# Generated by Django 4.2.7 on 2023-11-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Nhanvien",
            fields=[
                (
                    "MaNV",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
                ("TenNV", models.CharField(max_length=50)),
                ("Cccd", models.IntegerField(max_length=12, unique=True)),
                ("Mst", models.IntegerField(max_length=10, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("Sdt", models.IntegerField(max_length=10, unique=True)),
                ("DiaChi", models.CharField(max_length=120)),
            ],
        ),
    ]
