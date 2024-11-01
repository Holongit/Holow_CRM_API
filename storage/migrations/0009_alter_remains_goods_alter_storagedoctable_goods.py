# Generated by Django 4.2.13 on 2024-08-01 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0008_remove_goods_category_remove_goods_name_commongoods_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remains',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='storage.goods', unique=True),
        ),
        migrations.AlterField(
            model_name='storagedoctable',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='storage.goods', unique=True),
        ),
    ]
