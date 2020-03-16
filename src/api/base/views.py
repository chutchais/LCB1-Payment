from rest_framework import viewsets
from notify.models import Notify
from .serializers import NotifySerializer

# import datetime

class NotifyViewSet(viewsets.ModelViewSet):
	queryset = Notify.objects.all()
	serializer_class = NotifySerializer

	# def get_serializer_class(self):
	# 	if self.request.version == 'v1':
	# 		return NotifySerializerVersion1
	# 	return NotifySerializer