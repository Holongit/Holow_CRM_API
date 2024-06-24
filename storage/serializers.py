from rest_framework import serializers
from rest_framework.response import Response

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


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

