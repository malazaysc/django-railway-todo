from django.contrib import admin
from django.urls import path, include
from boards import urls as boards_urls
from core import urls as core_urls
from django.conf import settings

IS_DEVELOPMENT = settings.IS_DEVELOPMENT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include(boards_urls)),
    path('', include(core_urls))
]

development_urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
]

# Development only urls
if IS_DEVELOPMENT:
    urlpatterns += development_urlpatterns