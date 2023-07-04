from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import OrderSerializer, OrderDetailSerializer


class OrderDetailViewset(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderDetailSerializer


class OrderViewset(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer
