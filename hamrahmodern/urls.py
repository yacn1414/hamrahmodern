from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.site.site_header = "Mobile modern"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('',include('details.urls')),
    path('',include('Users.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
