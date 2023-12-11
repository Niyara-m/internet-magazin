from django.contrib import admin
from django.urls import path, include
from testapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.registration)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
