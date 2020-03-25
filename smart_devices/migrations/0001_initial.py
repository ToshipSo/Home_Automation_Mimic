# Generated by Django 3.0.4 on 2020-03-25 10:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('AC', 'AC'), ('TV', 'TV'), ('LIGHT', 'Light'), ('FAN', 'Fan'), ('LOCK', 'Lock'), ('ALARM', 'Alarm')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20)),
                ('room_type', models.CharField(choices=[('HALL', 'Hall'), ('KITCHEN', 'Kitchen'), ('BEDROOM', 'Bedroom')], default='BEDROOM', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('volume', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('input', models.CharField(choices=[('HDMI1', 'HDMI 1'), ('HDMI2', 'HDMI 2'), ('AV', 'AV'), ('PRIME', 'Amazon Prime'), ('NETFLIX', 'Netflix')], default='HDMI1', max_length=15)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='smart_devices.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(choices=[(True, 'Armed'), (False, 'Unarmed')])),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='smart_devices.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('brightness', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='smart_devices.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('speed', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='smart_devices.Device')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_devices.Room'),
        ),
        migrations.CreateModel(
            name='AC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('temperature', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(40)])),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='smart_devices.Device')),
            ],
        ),
    ]