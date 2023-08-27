from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.core.cache.backends.locmem import _caches as cache

from appchat.views import index

urlpatterns = [
    path('', index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('appchat/', include('appchat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if cache and cache.get('sc', None):
    cache['sc'].clear()
