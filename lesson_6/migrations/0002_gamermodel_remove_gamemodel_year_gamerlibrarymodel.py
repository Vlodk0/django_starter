# Generated by Django 4.1.7 on 2023-07-21 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_6', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='gamemodel',
            name='year',
        ),
        migrations.CreateModel(
            name='GamerLibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('game', models.ManyToManyField(to='lesson_6.gamemodel')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_6.gamermodel')),
            ],
        ),
    ]
