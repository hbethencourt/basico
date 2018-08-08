from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from login.urls import login_patterns

urlpatterns = [
    path('',include('core.urls')),
    path('admin/', admin.site.urls),    
    path("login/",include(login_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

