from rest_framework import serializers
from collections import OrderedDict

from notify.models import Notify

class NotifySerializer(serializers.ModelSerializer):
	# YYYYMMDDHHMMSS -- 2020-03-11T14:19:30 , , read_only=True
	BankRef 		= serializers.CharField(source='bankref')
	BillerNo 		= serializers.CharField(source='billerno')
	Ref1 			= serializers.CharField(source='ref1')
	Ref2 			= serializers.CharField(source='ref2')
	QRId 			= serializers.CharField(source='qrid')
	Amoun 			= serializers.FloatField(source='amount')
	ResultCode 		= serializers.CharField(source='resultcode')
	ResultDesc 		= serializers.CharField(source='resultdesc')
	TransDate 		= serializers.DateTimeField(source='transdate',
							format='%Y%m%d%H%M%S',
							input_formats=['%Y%m%d%H%M%S', 'iso-8601'],
							required=True,read_only=False)
	Fee 			= serializers.CharField(source='fee',required=False,default=0)
	
	class Meta:
		model 	= Notify
		fields 	= ['BankRef','BillerNo','Ref1','Ref2','QRId','Amoun',
					'ResultCode','ResultDesc','TransDate','Fee']

	# def to_representation(self, instance):
	# 	result = OrderedDict()
	# 	result['BankRef'] 		= instance.bankref
	# 	result['ResCode'] 		= instance.resultcode
	# 	result['ResDesc'] 		= instance.resultdesc
	# 	result['TransDate'] 	= instance.transdate.strftime('%Y%m%d%H%M%S')
	# 	return result
