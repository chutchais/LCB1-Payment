from django.shortcuts import render
from django.conf 			import settings
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
# {
#      "BillerNo":"011554701016180",
#      "QRId":"DLCMDN200000027"
# }
# def VerifySlip(request):
# 	context ={}
# 	if request.method == 'POST':
#     	context = json.loads(request.body)
	
# 	return JsonResponse(context, safe=False)
@csrf_protect
def VerifySlip(request):
	import urllib3
	http = urllib3.PoolManager()
	context ={}
	# context = json.loads(request.body)
	if request.method == 'GET':
		# body = json.loads(request.body)
		# 1) body =json.dumps(request.body).encode('utf-8') --Notwork
		body 		= json.loads(request.body)
		billerId 	= body['BillerNo']
		biller 		= 'LCB' if billerId =='010553811088480' else 'LCM'
		body 		= json.dumps(body).encode('utf-8')

		url 		= f'{settings.TMB_NOTIFY_URL}{biller}'
		print(url)
		
		# print(settings.TMB_NOTIFY_URL)
		r = http.request('POST',
			url,
			body =body,
			headers={'Content-Type': 'application/json'})
		# if r.status ==200 :
		context = r.data.decode('utf-8')
		# print(context)
		# Call TMB VerifySlip function
	return HttpResponse(context)#JsonResponse(context, safe=False)