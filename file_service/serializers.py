from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    size = serializers.FloatField()
    file = serializers.FileField(required=True)

    class Meta:
        model = File
        fields = ('name', 'size', 'file')
