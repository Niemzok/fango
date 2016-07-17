from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Lookup table for ifferent Account Types such as Income, Assets,
# Expense etc.
@python_2_unicode_compatible
class Account_Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


# Accounts associate with costs and income
@python_2_unicode_compatible
class Account(models.Model):
    account_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    account_type = models.ForeignKey(Account_Type,
                                     on_delete=models.CASCADE)
    def __str__(self):
        return self.account_name
    def was_published_recently(self):
        return self.pub_date >= (timezone.now()
                                - datetime.timedelta(
                                days=1))
