from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Account

# Create your views here.
def index(request):
    account_list = Account.objects.order_by('account_name')
    context = {
        'account_list': account_list,
    }
    return render(request, 'accounts/index.html', context)

def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'accounts/detail.html', {'account': account})
