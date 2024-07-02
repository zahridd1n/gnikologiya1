from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Gnikologiya API Documentation",
      default_version='v1',
      description="FARGENIUS GROUP TARAFIDAN",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('vaqtinchalik.urls')),

    path('api/', include([
        path('api28/', include('client_panel.urls')),
        path('dashboard/', include('admin_panel.urls')),
        path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
