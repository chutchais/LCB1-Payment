# versioned/v2/views.py
from api.base.views import *
from api.base import views as base_views
from . import serializers as v2_serializers

from django_filters.rest_framework import DjangoFilterBackend


class NotifyViewSet(base_views.NotifyViewSet):
	# pass
    serializer_class = v2_serializers.NotifySerializer


class VerifySlipLocal(base_views.NotifyViewSet):
	serializer_class 	= v2_serializers.VerifySlipSerializer
	filter_backends 	= [DjangoFilterBackend]
	filterset_fields 	= ['qrid', 'ref1']