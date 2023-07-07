from rest_framework import mixins, status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import File
from .serializers import FileSerializer


class FileView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        size = request.data.get('size')
        file = request.data.get('file')
        file_m = File.objects.create(
            name=name,
            size=size,
            file=file
        )

        return Response({
            'message': 'File uploaded!',
            'id': file_m.id,
            'file_url': file_m.file.url
        })

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
