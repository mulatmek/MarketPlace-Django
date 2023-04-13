from django.shortcuts import render
import os
from item.models import Item, Category
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, os.path.join('core', 'index.html'),{
        'items': items,
        'categories': categories
    })


def contact(request):
    return render(request, os.path.join('core', 'contact.html'))