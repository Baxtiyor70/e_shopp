from rest_framework.routers import DefaultRouter
from .views import CategoryView,ProductView

router = DefaultRouter()
router.register('category',CategoryView, basename='category')
router.register('product', ProductView, basename='product')


