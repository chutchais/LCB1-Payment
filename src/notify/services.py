from django_q.tasks import async_task

def sendNotify(notify):
	qrid 		= notify.qrid
	transdate 	= notify.transdate
	bankref 	= notify.bankref
	print (f'Send Notify function,{qrid}--{transdate}--{bankref}')
	async_task('notify.services.postNotifyToePayment', qrid,transdate,bankref)
	async_task('notify.services.postNotifyToBilling', qrid,transdate,bankref)
	# pass


def postNotifyToePayment(qrid,transdate,bankref):
	print('Task postNotifyToePayment')
	async_task('notify.services.postNotify', 'URL1')

def postNotifyToBilling(qrid,transdate,bankref):
	print('Task postNotifyToBilling')
	async_task('notify.services.postNotify', 'URL2')

def postNotify(url):
	print('Task postNotify')
	print(url)