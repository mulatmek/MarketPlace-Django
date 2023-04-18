from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })

@login_required
def item(request, item_id):
    item = Item.objects.get(pk=item_id)

    return render(request, 'dashboard/item.html', {
        'item': item,
    })
   