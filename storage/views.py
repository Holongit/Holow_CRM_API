from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item, Category
from .serializers import ItemSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

# class StorageApiView(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
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
