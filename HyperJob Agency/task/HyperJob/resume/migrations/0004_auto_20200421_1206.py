# Generated by Django 2.2 on 2020-04-21 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20200419_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
