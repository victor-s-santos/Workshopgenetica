# Generated by Django 2.1.7 on 2019-04-11 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graficos', '0011_auto_20190411_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicursos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pontuacaominicursos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]