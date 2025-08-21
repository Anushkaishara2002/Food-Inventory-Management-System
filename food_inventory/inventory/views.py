from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def dashboard(request):
    items = Item.objects.all()
    return render(request, 'inventory/dashboard.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/edit_item.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return render(request, 'inventory/delete_item.html', {'item': item})
