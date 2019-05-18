# Generated by Django 2.1.7 on 2019-02-28 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0031_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_type',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]