from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import krieva.settings as settings
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teams.urls')),
    path('', include('events.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
