# Generated by Django 4.2.3 on 2023-08-01 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_garage_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garage',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='garage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.garage'),
            preserve_default=False,
        ),
    ]
