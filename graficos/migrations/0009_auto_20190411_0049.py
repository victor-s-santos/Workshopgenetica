# Generated by Django 2.1.7 on 2019-04-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graficos', '0008_auto_20190411_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontuacaominicursos',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='pontuacaominicursos',
            unique_together={('minicurso', 'nome')},
        ),
    ]
