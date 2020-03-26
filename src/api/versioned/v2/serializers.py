# versioned/v2/serializers.py

# import all our basic serializers

from api.base import serializers as base_serializers
from api.base.serializers import *

class NotifySerializer(base_serializers.NotifySerializer):
	BankRef 		= serializers.CharField(source='bankref')
	BillerNo 		= serializers.CharField(source='billerno')
	Ref1 			= serializers.CharField(source='ref1')
	Ref2 			= serializers.CharField(source='ref2')
	QRId 			= serializers.CharField(source='qrid')
	Amount 			= serializers.FloatField(source='amount')
	ResultCode 		= serializers.CharField(source='resultcode')
	ResultDesc 		= serializers.CharField(source='resultdesc')
	TransDate 		= serializers.DateTimeField(source='transdate',
							format='%Y%m%d%H%M%S',
							input_formats=['%Y%m%d%H%M%S', 'iso-8601'],
							required=True,read_only=False)
	Fee 			= serializers.CharField(source='fee',required=False,default=0)
	
	class Meta(base_serializers.NotifySerializer.Meta):
		fields 	= ['BankRef','BillerNo','Ref1','Ref2','QRId','Amount',
					'ResultCode','ResultDesc','TransDate','Fee']

	def to_representation(self, instance):
		result = OrderedDict()
		result['BankRef'] 		= instance.bankref
		result['ResCode'] 		= instance.resultcode
		result['ResDesc'] 		= instance.resultdesc
		result['TransDate'] 	= instance.transdate.strftime('%Y%m%d%H%M%S')
		return result

