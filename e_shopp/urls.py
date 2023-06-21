from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from products.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('account.urls')),
    path('products/', include(router.urls))
    # path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    # path('api/token/verify/',TokenVerifyView.as_view(),name='token_verify'),
]
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]