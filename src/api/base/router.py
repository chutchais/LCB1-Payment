from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'notify', views.NotifyViewSet)
# router.register(r'books', views.BookViewSet)

api_urlpatterns = router.urls

