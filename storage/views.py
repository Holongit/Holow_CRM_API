from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.core.files.storage import Storage
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from storage.serializers import *
from storage.models import *
from storage.services import doc_close, doc_open


# from .models import Item, Category
# from .serializers import ItemSerializer


class StorageDocViewSet(viewsets.ModelViewSet):

    queryset = StorageDoc.objects.all()
    serializer_class = StorageDocSerializer


class StoragesViewSet(viewsets.ModelViewSet):
    queryset = Storages.objects.all()
    serializer_class = StoragesSerializer


class StorageClientsViewSet(viewsets.ModelViewSet):
    queryset = StorageClients.objects.all()
    serializer_class = StorageClientsSerializer


class CategoryGoodsViewSet(viewsets.ModelViewSet):
    queryset = CategoryGoods.objects.all()
    serializer_class = CategoryGoodsSerializer



class GoodsViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return GoodsGetSerializer
        return GoodsSerializer

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CommonGoodsViewSet(viewsets.ModelViewSet):
    queryset = CommonGoods.objects.all()
    serializer_class = CommonGoodsSerializer


class StorageDocTableViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return StorageDocTableGetSerializer
        return StorageDocTableSerializer

    queryset = StorageDocTable.objects.all()
    serializer_class = StorageDocTableSerializer



class RemainsVieSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return RemainsGetSerializer
        return RemainsSerializer

    queryset = Remains.objects.all()
    serializer_class = RemainsSerializer


# class StorageDocTableView(APIView):
#     def get(self, request):
#         queryset = StorageDocTable.objects.all()
#         serializer = StorageDocTableGetSerializer(queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = StorageDocTableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response({'status': f'Incorrect data'}, status=400)

# class CommonGoodsListView(APIView):
#     def get(self, request):
#         common_good_list = CommonGoods.objects.all()
#         serializer = CommonGoodsSerializer(common_good_list, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = CommonGoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response({'status': f'Incorrect data'}, status=400)
#
#
# class CommonGoodsDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             common_good = CommonGoods.objects.get(id=pk)
#             serializer = CommonGoodsSerializer(common_good)
#             return Response(serializer.data)
#         except:
#             return Response({'status': f'Not found'}, status=404)
#
#     def delete(self, request, pk):
#         try:
#             common_good = CommonGoods.objects.get(id=pk)
#             common_good.delete()
#             return Response({'status': f'{common_good.name} success deleted'}, status=200)
#         except:
#             return Response({'status': f'Not found'}, status=404)
#
#     def put(self, request, pk):
#         try:
#             common_good = CommonGoods.objects.get(id=pk)
#             serializer = CommonGoodsSerializer(data=request.data)
#             if serializer.is_valid():
#                 common_good.name = serializer.validated_data['name']
#                 common_good.category = serializer.validated_data['category']
#                 common_good.save()
#                 return Response(serializer.data, status=201)
#             else:
#                 return Response({'status': f'Incorrect data'}, status=400)
#         except:
#             return Response({'status': f'Not found'}, status=404)


# class GoodsListView(APIView):
#     def get(self, request):
#         goods_list = Goods.objects.all()
#         serializer = GoodsSerializer(goods_list, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response({'status': f'Incorrect data'}, status=400)
#
#
# class GoodsDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             goods = Goods.objects.get(id=pk)
#             serializer = GoodsSerializer(goods)
#             return Response(serializer.data, status=200)
#         except:
#             return Response({'status': f'Not found'}, status=404)
#
#     def delete(self, request, pk):
#         try:
#             goods = Goods.objects.get(id=pk)
#             goods.delete()
#             return Response({'status': f'{goods.common_goods} success deleted'}, status=200)
#         except:
#             return Response({'status': f'Not found'}, status=404)
#
#     def put(self, request, pk):
#         try:
#             goods = Goods.objects.get(id=pk)
#             serializer = GoodsSerializer(data=request.data)
#             if serializer.is_valid():
#                 goods.price_in = serializer.validated_data['price_in']
#                 goods.price_out = serializer.validated_data['price_out']
#                 goods.serial_number = serializer.validated_data['serial_number']
#                 goods.condition = serializer.validated_data['condition']
#                 goods.set = serializer.validated_data['set']
#                 goods.parameters = serializer.validated_data['parameters']
#                 goods.note = serializer.validated_data['note']
#                 goods.common_goods = serializer.validated_data['common_goods']
#                 goods.save()
#                 return Response(serializer.data, status=201)
#             else:
#                 return Response({'status': f'Incorrect data'}, status=400)
#         except:
#             return Response({'status': f'Not found'}, status=404)


# class StorageDocListView(APIView):
#     def get(self, request):
#         storage_doc_list = StorageDoc.objects.all()
#         serializer = StorageDocSerializer(storage_doc_list, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StorageDocSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response({'status': f'Incorrect data'}, status=400)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class StorageViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     # permission_classes = (IsAuthenticatedOrReadOnly,)

# class StorageApiView(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
# class StoragePutDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class StorageApiView(APIView):
#     def get(self, request):
#         items = Item.objects.all()
#         return Response({'items': ItemSerializer(items, many=True).data})
#
#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'item': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method PUT not allowed"})
#
#         try:
#             instance = Item.objects.get(pk=pk)
#         except:
#             return Response({'error': "Item does not exist"})
#
#         serializer = ItemSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method DELETE not allowed"})
#
#         try:
#             instance = Item.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Item does not exist'})
#
#         instance.delete()
#
#         return Response({'success': "delete item: " + str(pk)})
#
