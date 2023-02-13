# Generated by Django 4.1.6 on 2023-02-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название задания')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('done', 'Выполнена')], default='new', max_length=15, verbose_name='Статус')),
                ('deadline', models.DateField(auto_now_add=True, null=True, verbose_name='Выполнить до')),
            ],
        ),
    ]