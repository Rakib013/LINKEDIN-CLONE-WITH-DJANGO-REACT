# Generated by Django 3.2.8 on 2021-11-06 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkedin', '0002_auto_20211106_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedin.post'),
        ),
    ]
