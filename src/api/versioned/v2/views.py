# versioned/v2/views.py
from api.base.views import *
from api.base import views as base_views
from . import serializers as v2_serializers

from django_filters.rest_framework import DjangoFilterBackend

import json
from rest_framework import viewsets
from rest_framework import generics
from django.conf	import settings
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from notify.models import Notify
from .serializers import VerifySlipSerializer

class NotifyViewSet(base_views.NotifyViewSet):
	# pass
	serializer_class = v2_serializers.NotifySerializer
	filter_backends 	= [DjangoFilterBackend]
	filterset_fields 	= ['qrid', 'ref1']
	def create(self, request):
		print ('Create--Notify',request.data)
		serializer = v2_serializers.NotifySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			print('Create--Notify--Save',serializer.data)
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# Created on Aug 25,2020 -- To change create status response from 201 to 200 (follow TMB Standard)

# Verify on Local Database
# class VerifySlipLocal(base_views.NotifyViewSet):
class VerifySlipLocal(viewsets.ModelViewSet):
	queryset 			= Notify.objects.all()
	serializer_class 	= VerifySlipSerializer #v2_serializers.VerifySlipSerializer
	filter_backends 	= [DjangoFilterBackend]
	filterset_fields 	= ['qrid', 'ref1']


# Verify direct to TMB 
class VerifySlip(generics.RetrieveAPIView,base_views.NotifyViewSet):
	queryset = Notify.objects.all()
	serializer_class = v2_serializers.VerifySlipSerializer

	def list(self, request):
		# Default LCB1 = 010553811088480
		billerId 	= self.request.query_params.get('billerid', None) #011554701016180(LCM) or 010553811088480(LCB)
		qrid 		= self.request.query_params.get('QRid', None)
		# ref1 		= self.request.query_params.get('ref1', None)
		print(billerId,qrid)

		# billerId 	= '011554701016180'
		biller 		= 'LCB' if billerId =='010553811088480' else 'LCM'
		print(biller)
		url 		= f'{settings.TMB_NOTIFY_URL}{biller}'
		print(url)
		body 		= {
							 "BillerNo": biller,
							 "QRId":qrid
						}
		body 		= json.dumps(body).encode('utf-8')
		import urllib3
		http = urllib3.PoolManager()
		context ={}
		r = http.request('POST',
			url,
			body =body,
			headers={'Content-Type': 'application/json'})

		context = r.data.decode('utf-8')
		print(context)
		return JsonResponse(json.loads(context), safe=False)

# Added on July 22,2020
# For IT Testing 
class Testing(generics.RetrieveAPIView,base_views.NotifyViewSet):
	queryset = Notify.objects.all()
	serializer_class = v2_serializers.VerifySlipSerializer

	def list(self, request):
		context = {
			"data":"Testing API on 10.24.50.80",
			"ip" :get_client_ip(request)
		}
		return JsonResponse(context, safe=False)

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip