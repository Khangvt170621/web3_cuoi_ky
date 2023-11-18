# Generated by Django 4.2.7 on 2023-11-17 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("quanlykhachhang", "0001_initial"),
        ("quanlyphong", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhieuDatPhong",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("NgayNhan", models.DateField()),
                ("NgayTra", models.DateField()),
                (
                    "MaKH",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quanlykhachhang.khachhang",
                    ),
                ),
                (
                    "MaPhong",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quanlyphong.phong",
                    ),
                ),
            ],
        ),
    ]
