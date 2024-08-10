from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'storages', StoragesViewSet)
router.register(r'clients', StorageClientsViewSet)
router.register(r'catgoods', CategoryGoodsViewSet)
router.register(r'doc', StorageDocViewSet)
router.register(r'goods', GoodsViewSet)
router.register(r'doctable', StorageDocTableViewSet)
router.register(r'commongoods', CommonGoodsViewSet)
router.register(r'remains', RemainsVieSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('doctable', StorageDocTableView.as_view())
    # path('commongoods/', CommonGoodsListView.as_view()),
    # path('commongoods/<int:pk>/', CommonGoodsDetailView.as_view()),
    # path('goods/', GoodsListView.as_view()),
    # path('goods/<int:pk>/', GoodsDetailView.as_view()),
    # path('doc/', StorageDocListView.as_view()),
]
