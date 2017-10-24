from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from rango import views
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
]

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )