from django.contrib import admin

from .models import Account
from .models import Account_Type
# Register your models here.

admin.site.register(Account)
admin.site.register(Account_Type)
