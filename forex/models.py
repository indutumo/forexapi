from django.db import models
from django.utils import timezone
from datetime import datetime


class ForexRate(models.Model):
	base_currency = models.CharField(max_length=5)
	target_currency = models.CharField(max_length=5)
	rate = models.DecimalField(default=0.00,max_digits=1000,decimal_places=2)
	datetime = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.target_currency
