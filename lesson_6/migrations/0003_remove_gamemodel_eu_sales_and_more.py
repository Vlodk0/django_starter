# Generated by Django 4.1.7 on 2023-07-21 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_6', '0002_gamermodel_remove_gamemodel_year_gamerlibrarymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemodel',
            name='eu_sales',
        ),
        migrations.RemoveField(
            model_name='gamemodel',
            name='global_sales',
        ),
        migrations.RemoveField(
            model_name='gamemodel',
            name='jp_sales',
        ),
        migrations.RemoveField(
            model_name='gamemodel',
            name='na_sales',
        ),
        migrations.RemoveField(
            model_name='gamemodel',
            name='other_sales',
        ),
    ]
