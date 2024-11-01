from django.contrib.auth.models import User
from django.db import models


class Storages(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    def __str__(self):
        return self.name


class StorageClients(models.Model):
    name = models.CharField(max_length=128, unique=True)
    telephone = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    def __str__(self):
        return self.name


class StorageDoc(models.Model):
    type = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=32, default='open')
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    client = models.ForeignKey('StorageClients', on_delete=models.PROTECT, null=True)
    storage = models.ForeignKey('Storages', verbose_name='storage', on_delete=models.PROTECT)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    def __str__(self):
        return f'№{self.id} {self.storage}'


class CategoryGoods(models.Model):
    name = models.CharField(max_length=256)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name


class CommonGoods(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey('CategoryGoods', on_delete=models.PROTECT, null=True, blank=True)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    class Meta:
        verbose_name = "CommonGood"
        verbose_name_plural = "CommonGoods"

    def __str__(self):
        return self.name


class Goods(models.Model):
    price_in = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price_out = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    serial_number = models.CharField(max_length=128, null=True, blank=True)
    condition = models.CharField(max_length=256, null=True, blank=True)
    set = models.CharField(max_length=256, null=True, blank=True)
    parameters = models.CharField(max_length=256, null=True, blank=True)
    note = models.CharField(max_length=512, null=True, blank=True)
    common_goods = models.ForeignKey('CommonGoods', on_delete=models.CASCADE, null=True, blank=True)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    def __str__(self):
        return f'{self.common_goods.name} {self.parameters}'


class StorageDocTable(models.Model):
    storage_doc = models.ForeignKey('StorageDoc', on_delete=models.CASCADE)
    goods_qnt = models.IntegerField(default=1)
    goods = models.ForeignKey('Goods', on_delete=models.PROTECT, null=True, blank=True)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    def __str__(self):
        return self.storage_doc


class Remains(models.Model):
    goods = models.ForeignKey('Goods', on_delete=models.PROTECT, null=True, blank=True)
    qnt = models.IntegerField(default=1, null=True, blank=True)
    storage = models.ForeignKey('Storages', on_delete=models.PROTECT, null=True, blank=True)
    api_control = models.CharField(max_length=16, null=True, blank=True, default='no command')

    def __str__(self):
        return self.goods
