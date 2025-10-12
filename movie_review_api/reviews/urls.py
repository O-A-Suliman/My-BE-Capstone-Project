from rest_framework import routers
from .views import ReviewViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls