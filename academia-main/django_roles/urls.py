from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('map.urls', namespace='map')),
   #path('accounts/', include('accounts.urls', namespace='accounts')),
    #path('', include('map.urls', namespace='map')), 
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

