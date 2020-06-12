from django.contrib import admin

# Register your models here.
from .models import Bank,Notify

admin.site.register(Bank)


class NotifyAdmin(admin.ModelAdmin):
	search_fields           = ['bankref','ref1','ref2','billerno','payername','qrid']
	list_filter             = ['bank','resultcode']
	list_display            = ('bankref','transdate','billerno','qrid','ref1','ref2','amount','resultcode','created')
	readonly_fields         = ('created','modified','user')

	# save_as = True
	# save_as_continue = True
	# save_on_top =True

	fieldsets = [
		('Basic Information',{'fields': ['bankref','qrid','billerno','ref1','ref2',]}),
		('Payer Information',{'fields': ['payername','payerbank','amount','fee','transdate']}),
		('transaction Information',{'fields': ['resultcode','resultdesc']}),
		('System Information',{'fields':['user','created','modified']})
	]
	# resource_class          = RentalResource

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super(NotifyAdmin, self).save_model(request, obj, form, change)

admin.site.register(Notify,NotifyAdmin)