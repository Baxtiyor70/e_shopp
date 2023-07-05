from rest_framework import mixins, status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import FileSerializer


class FileView(
       mixins.CreateModelMixin,
       mixins.RetrieveModelMixin,
       GenericViewSet):
    serializer_class = FileSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
