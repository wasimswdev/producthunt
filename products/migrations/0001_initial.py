# Generated by Django 2.2.9 on 2020-01-21 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=200)),
                ('hunt_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('url', models.TextField()),
                ('votes', models.IntegerField(default=1)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]