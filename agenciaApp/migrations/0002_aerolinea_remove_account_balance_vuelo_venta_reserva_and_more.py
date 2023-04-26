# Generated by Django 4.1.1 on 2022-09-12 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenciaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aerolinea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Aerolinea')),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='balance',
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('destino', models.CharField(max_length=50, verbose_name='Destino')),
                ('fecha', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=3, max_digits=11)),
                ('aerolinea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vuelo', to='agenciaApp.aerolinea')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vuelo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('valor_reserva', models.DecimalField(decimal_places=3, max_digits=11)),
                ('destino_reserva', models.CharField(max_length=50, verbose_name='Destino')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserva', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('producto', models.CharField(max_length=50, verbose_name='Producto')),
                ('valor_producto', models.DecimalField(decimal_places=3, max_digits=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to=settings.AUTH_USER_MODEL)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to='agenciaApp.venta')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='facturas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='agenciaApp.factura'),
        ),
        migrations.AddField(
            model_name='account',
            name='reservas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='agenciaApp.reserva'),
        ),
    ]