# versioned/v2/serializers.py

# import all our basic serializers

from api.base import serializers as base_serializers
from api.base.serializers import *

class NotifySerializer(base_serializers.NotifySerializer):

	class Meta(base_serializers.NotifySerializer.Meta):
		fields = ('__all__')

	def to_representation(self, instance):
		result = OrderedDict()
		result['BankRef'] 		= instance.bankref
		result['ResCode'] 		= instance.resultcode
		result['ResDesc'] 		= instance.resultdesc
		result['TransDate'] 	= instance.transdate.strftime('%Y%m%d%H%M%S')
		return result
