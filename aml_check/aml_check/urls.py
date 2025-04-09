from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('ethereum', include('ethereum.urls', namespace='ethereum')),
    path('tron', include('tron.urls', namespace='tron')),
    path('ton', include('ton.urls', namespace='ton')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)