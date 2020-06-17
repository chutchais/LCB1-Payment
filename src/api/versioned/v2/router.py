from rest_framework import routers
# from . import views
from .views import NotifyViewSet,VerifySlip

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'notify', NotifyViewSet)
# router.register(r'verifyslip', VerifySlip.as_view()) # Direct to TMB
# router.register(r'verifyslip-local', views.VerifySlipLocal) #On local Host

# router.register(r'books', views.BookViewSet)

# urlpatterns = [
#     url(r'verifyslip', VerifySlip.as_view()),
# ]

api_urlpatterns =  router.urls