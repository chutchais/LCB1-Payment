# versioned/v2/views.py
from api.base.views import *
from api.base import views as base_views
from . import serializers as v2_serializers


class NotifyViewSet(base_views.NotifyViewSet):
	# pass
    serializer_class = v2_serializers.NotifySerializer