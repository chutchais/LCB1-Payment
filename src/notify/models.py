from django.db 				import models
from django.conf 			import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
class Bank(models.Model):
	name 			= models.CharField(primary_key= True,max_length=20,
						validators=[
									RegexValidator(
										regex='^[\w-]+$',
										message='Name does not allow special charecters',
									),
								])
	title 			= models.CharField(max_length=200)
	created		 	= models.DateTimeField(auto_now_add=True)
	modified		= models.DateTimeField(auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s' % (name))

	def get_absolute_url(self):
		return reverse('notify:bank-detail', kwargs={'pk': self.pk})


class Notify(models.Model):
	bank 			= models.ForeignKey(Bank,
									verbose_name='Bank',
									on_delete=models.CASCADE,
									blank=True,null=True,
									related_name='notifies')
	bankref 		= models.CharField(verbose_name='Bank Reference',max_length=100)
	billerno		= models.CharField(verbose_name='Biller number',max_length=20,blank=True,null=True)
	ref1	 		= models.CharField(verbose_name='Ref1',max_length=100)
	ref2 			= models.CharField(verbose_name='Ref2',max_length=100)
	qrid 			= models.CharField(verbose_name='QR id',max_length=100)
	payername		= models.CharField(verbose_name='Payer name',max_length=100)
	payerbank		= models.CharField(verbose_name='Payer Bank',max_length=100)
	amount			= models.FloatField(verbose_name='Amont',default=0)
	fee				= models.FloatField(verbose_name='Fee charge',default=0)
	resultcode		= models.CharField(verbose_name='Result Code',max_length=20,blank=True,null=True)
	resultdesc		= models.CharField(verbose_name='Result Describe',max_length=100,blank=True,null=True)
	transdate		= models.DateTimeField(verbose_name='Trans Date') 
	created		 	= models.DateTimeField(auto_now_add=True)
	modified		= models.DateTimeField(auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.bankref))

	def get_absolute_url(self):
		return reverse('notify:detail', kwargs={'pk': self.pk})