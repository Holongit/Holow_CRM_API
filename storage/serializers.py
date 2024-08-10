from rest_framework import serializers
# from django.core.files.storage import Storage
# from drf_writable_nested import WritableNestedModelSerializer
# from tutorial.quickstart.serializers import UserSerializer
# from rest_framework.response import Response

from storage.models import *
# from .models import Item


class StoragesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storages
        fields = '__all__'


class StorageClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageClients
        fields = '__all__'


class CategoryGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryGoods
        fields = '__all__'


class CommonGoodsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=CategoryGoods.objects.all())

    class Meta:
        model = CommonGoods
        fields = '__all__'


class GoodsGetSerializer(serializers.ModelSerializer):
    common_goods = serializers.StringRelatedField()

    class Meta:
        model = Goods
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StorageDocSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='name', queryset=StorageClients.objects.all())
    storage = serializers.SlugRelatedField(slug_field='name', queryset=Storages.objects.all())
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = StorageDoc
        fields = '__all__'


class StorageDocTableGetSerializer(serializers.ModelSerializer):
    storage_doc = serializers.StringRelatedField()
    goods = serializers.StringRelatedField()

    class Meta:
        model = StorageDocTable
        fields = '__all__'


class StorageDocTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = StorageDocTable
        fields = '__all__'


class RemainsGetSerializer(serializers.ModelSerializer):
    goods = serializers.StringRelatedField()
    storage = serializers.StringRelatedField()

    class Meta:
        model = Remains
        fields = '__all__'


class RemainsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Remains
        fields = '__all__'

# class StorageDocSerializer(serializers.ModelSerializer):
#     client = serializers.SlugRelatedField(slug_field='name', queryset=StorageClients.objects)
#     storage = serializers.SlugRelatedField(slug_field='name', queryset=Storages.objects)
#     user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)
#
#     class Meta:
#         model = StorageDoc
#         fields = '__all__'

# class CommonGoodsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
#     category = CategoryGoodsSerializer(read_only=False)
#
#     class Meta:
#         model = CommonGoods
#         fields = '__all__'

# class GoodsSerializer(serializers.ModelSerializer):
#     storage_doc = StorageDocSerializer(read_only=True)
#     common_goods = CommonGoodsSerializer(read_only=True)
#
#     class Meta:
#         model = Goods
#         fields = '__all__'




# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'

# class ItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=128)
#     price = serializers.DecimalField(max_digits=9, decimal_places=2)
#     categorise_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Item.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.price = validated_data.get('price', instance.price)
#         instance.categorise_id = validated_data.get('categorise_id', instance.categorise_id)
#         instance.save()
#         return instance
