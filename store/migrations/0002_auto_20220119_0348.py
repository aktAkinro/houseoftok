# Generated by Django 3.2.9 on 2022-01-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcolor',
            name='color',
        ),
        migrations.RemoveField(
            model_name='itemcolor',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('BLU', 'BLUE'), ('BLK', 'BLACK'), ('RED', 'RED'), ('GLD', 'GOLD'), ('SIL', 'SILVER')], default='RED', max_length=10),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='ItemColor',
        ),
    ]
