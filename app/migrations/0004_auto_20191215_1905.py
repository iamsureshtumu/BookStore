# Generated by Django 2.2.8 on 2019-12-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sslc_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineering',
            name='category',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('PUC', 'PUC'), ('Engineering', 'Engineering'), ('Masters', 'Masters')], default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='masters',
            name='category',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('PUC', 'PUC'), ('Engineering', 'Engineering'), ('Masters', 'Masters')], default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='puc',
            name='category',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('PUC', 'PUC'), ('Engineering', 'Engineering'), ('Masters', 'Masters')], default=True, max_length=20),
        ),
    ]