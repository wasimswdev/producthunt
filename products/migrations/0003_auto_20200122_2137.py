# Generated by Django 2.2.9 on 2020-01-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200122_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='icon',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]