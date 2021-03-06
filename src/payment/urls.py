"""payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from .routers import router
# from api.base.router import *
from api.base.router import api_urlpatterns as api_v1
from api.versioned.v2.router import api_urlpatterns as api_v2

# from api.versioned.v2.views import VerifySlipLocal
# from notify.views import VerifySlip,VerifySlipLocal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),
    path('api/v2/', include(api_v2)),
    # path('api/verifyslip/', VerifySlipLocal),
    # path('api/verifysliplocal/', VerifySlipLocal),
    # path('api/', include(router.urls)),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT},name='ssrfiles-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
admin.site.site_header = 'LCB1 Payment API.'
admin.site.site_title = 'LCB1 Payment API.'
