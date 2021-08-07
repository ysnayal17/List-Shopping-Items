from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.core import management
from django.contrib import messages

# Create your views here.
def item_list(request):
    if request.method=="POST":
        form = ItemForm(request.POST or None)
        if form.is_valid:
            form.save()
            items = Item.objects.all()
            messages.success(request, "Item Added Successfully!")
            return render(request, 'home.html', {'items': items})
        else:
            form = ItemForm()
            items = Item.objects.all()
            return render(request, 'home.html', {'items': items})

    else:
        form = ItemForm()
        items = Item.objects.all()
        return render(request, 'home.html', {'items': items})

def mark_pending(request, item_id):
    item = Item.objects.get(itemid=item_id)
    item.bought = False
    item.save()
    return redirect('home')

def mark_done(request, item_id):
    item = Item.objects.get(itemid=item_id)
    item.bought = True
    item.save()
    return redirect('home')

def delete_item(request, item_id):
    item = Item.objects.get(itemid=item_id)
    item.delete()
    messages.success(request, "Item Deleted Successfully!")
    return redirect('home')

def remove_all(request):
    Item.objects.all().delete()
    Item.itemid = 0
    messages.success(request, "List Deleted!! Add items for next shopping")
    return redirect('home')



