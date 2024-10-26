# Generated by Django 4.2.13 on 2024-10-09 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0012_alter_storagedoctable_goods_qnt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagedoc',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
