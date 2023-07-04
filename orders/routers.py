from rest_framework.routers import DefaultRouter
from .views import OrderDetailViewset, OrderViewset

router = DefaultRouter()
router.register('order', OrderViewset, basename='order')
router.register('order_detail', OrderDetailViewset, basename='order_detail')
