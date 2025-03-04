from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.swagger.schema import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("apps.users.urls")),
    path('auth/', include("apps.users.auth_urls")),
    path('', include("apps.main.urls"))
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

