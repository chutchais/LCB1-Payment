from rest_framework import routers
# from . import views
from .views import NotifyViewSet,VerifySlip,VerifySlipLocal,Testing

router = routers.DefaultRouter()

router.register(r'notify', NotifyViewSet,basename='notify')
router.register(r'verifyslip', VerifySlip,basename='verifyslip') # Direct to TMB
router.register(r'verifyslip-local', VerifySlipLocal,basename='verifyslip-local') #On local Host)
router.register(r'testing', Testing,basename='testing') #On local Host)

# router.register(r'books', views.BookViewSet)

# urlpatterns = [
#     url(r'verifyslip', VerifySlip),
# ]

api_urlpatterns =  router.urls