from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions, mixins, status
from rest_framework.response import Response


class CategoryView(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        categories = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProductView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


