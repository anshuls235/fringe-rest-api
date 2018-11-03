from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    url(r'',include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
