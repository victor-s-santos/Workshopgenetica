# Generated by Django 2.1.7 on 2019-03-21 00:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('graficos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='palestrante',
            name='data',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
