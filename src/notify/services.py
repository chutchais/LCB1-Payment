from django_q.tasks import async_task
from datetime import datetime

def sendNotify(notify):
	qrid 		= notify.qrid
	transdate 	= notify.transdate.strftime('%Y%m%d%H%M%S')
	bankref 	= notify.bankref
	print (f'Send Notify function,{qrid}--{transdate}--{bankref}')
	async_task('notify.services.postNotifyToePayment', qrid,transdate,bankref)
	# async_task('notify.services.postNotifyToBilling', qrid,transdate,bankref)
	# pass


def postNotifyToePayment(qrid,transdate,bankref):
	print('Task postNotifyToePayment')
	# url = 'http://192.168.1.113/order/api/update-payment' #Test server
	url = 'http://10.24.50.81/order/api/update-payment' #production
	payload = {
			"token":"(ixqqurv5j_oigrl(ggh(fbj(7f3@rw5dec%#e1k3-hbz&7o_8",
			"QRId" : qrid,
			"TransDate": transdate,
			"BankRef" : bankref
		}
	async_task('notify.services.postNotify', url,payload)

# def postNotifyToBilling(qrid,transdate,bankref):
# 	print('Task postNotifyToBilling')
# 	async_task('notify.services.postNotify', 'URL2')

def postNotify(url,payload):
	import json
	body = json.dumps(payload).encode('utf-8')
	import requests
	r = requests.post(url, json=payload)
	print(f'Post data to {url} --> {payload} -->Success')