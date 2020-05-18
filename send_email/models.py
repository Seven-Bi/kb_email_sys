#############################
# Author: Chen Bi
# Date: 18 May 2020
#############################

from django.db import models
from django.forms import ModelForm


class MarketingEmail(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField(max_length=254, primary_key=True)

	def __str__(self):
		return self.email