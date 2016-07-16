from __future__ import unicode_literals

from django.db import models

# Accounts associate with costs and income


class Account_Type(models.Model):
    name = models.CharField(max_length=200)

class Account(models.Model):
    account_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    account_type = models.ForeignKey(Account_Type,
                                     on_delete=models.CASCADE)
