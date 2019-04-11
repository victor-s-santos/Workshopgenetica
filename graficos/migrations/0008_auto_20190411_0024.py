# Generated by Django 2.1.7 on 2019-04-11 00:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graficos', '0007_auto_20190331_0436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pontuacao',
            options={'verbose_name': 'Pontuação', 'verbose_name_plural': 'Pontuações dos Palestrantes'},
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='limpeza',
            new_name='divulgacao',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='tema',
            new_name='indicacao',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='email',
        ),
        migrations.AddField(
            model_name='evento',
            name='open_lab',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='evento',
            name='palestras',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='evento',
            name='retorno',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
