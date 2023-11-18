# Generated by Django 4.2.7 on 2023-11-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("quanlyphong", "0004_alter_loaiphong_loaiphong_alter_phong_loaiphong"),
    ]

    operations = [
        migrations.CreateModel(
            name="SoGiuong",
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
                ("Sogiuong", models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="phong",
            name="Loaiphong",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="quanlyphong.loaiphong"
            ),
        ),
        migrations.AddField(
            model_name="phong",
            name="Sogiuong",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="quanlyphong.sogiuong",
            ),
        ),
    ]
