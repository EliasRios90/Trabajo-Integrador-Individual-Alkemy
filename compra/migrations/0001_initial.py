# Generated by Django 4.2.1 on 2023-05-08 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField(default=0.0)),
                ('stock_actual', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='compra.proveedor')),
            ],
        ),
    ]
