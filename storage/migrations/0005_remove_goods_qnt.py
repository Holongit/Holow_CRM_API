# Generated by Django 4.2.13 on 2024-07-02 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_categorygoods_commongoods_goods_remains_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='qnt',
        ),
    ]
