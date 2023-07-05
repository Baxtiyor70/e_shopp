from rest_framework.routers import DefaultRouter
from .views import FileView

router = DefaultRouter()
router.register('upload', FileView, basename='file')
