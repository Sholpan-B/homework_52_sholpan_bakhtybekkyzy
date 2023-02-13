# Generated by Django 4.1.6 on 2023-02-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, max_length=16, null=True, verbose_name='Выполнить до'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('in process', 'В процессе'), ('done', 'Сделано')], default='new', max_length=15, verbose_name='Статус'),
        ),
    ]
