from communicator_api.ports import rest as rs
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'short_url', rs.ShortUrlViewSet, basename='short_url')

urlpatterns = [
    *router.urls
]
