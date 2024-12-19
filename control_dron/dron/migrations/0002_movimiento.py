# Generated by Django 5.1.4 on 2024-12-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dron', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comando', models.CharField(max_length=20)),
                ('posicion_x', models.IntegerField()),
                ('posicion_y', models.IntegerField()),
                ('posicion_z', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
