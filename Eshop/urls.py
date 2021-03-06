from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls import (
                                handler400,
                                handler403,
                                handler404,
                                handler500)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = 'store.views.views.bad_request'
handler403 = 'store.views.views.permission_denied'
handler404 = 'store.views.views.page_not_found'
handler500 = 'store.views.views.server_error'
