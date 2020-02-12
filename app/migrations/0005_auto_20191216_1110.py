# Generated by Django 2.2.8 on 2019-12-16 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191215_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineering',
            name='category',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('PUC', 'PUC'), ('Engineering', 'Engineering'), ('Masters', 'Masters')], max_length=20),
        ),
        migrations.AlterField(
            model_name='masters',
            name='category',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('PUC', 'PUC'), ('Engineering', 'Engineering'), ('Masters', 'Masters')], max_length=20),
        ),
        migrations.AlterField(
            model_name='puc',
            name='category',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('PUC', 'PUC'), ('Engineering', 'Engineering'), ('Masters', 'Masters')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslc',
            name='category',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('PUC', 'PUC'), ('Engineering', 'Engineering'), ('Masters', 'Masters')], max_length=20),
        ),
    ]