from django.shortcuts import render,redirect
from .models import Product, Business, Transaction, Contribution
from .forms import ProductEditForm, NewProductForm
from django.shortcuts import get_object_or_404
from django.db.models import Sum

def home(request):
    return render(request, 'inventory/home.html', {})

def inventory_view(request):
    products = Product.objects.filter()
    hits = Product.objects.order_by('sales_count')
    hits = hits.reverse()[0:3]
    return render(request, 'inventory/inventory_view.html', {'products': products,'hits': hits})

def inventory_top_hits_view(request):
    products = Product.objects.order_by('sales_count')
    products = products.reverse()[0:3]
    return render(request, 'inventory/top_hits.html', {'products': products})

def product_new(request):
    if request.method == "POST":
        form = NewProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('inventory')
    else:
        form = NewProductForm()
    return render(request, 'inventory/new_product.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('inventory')
    else:
        form = ProductEditForm(instance=product)
    return render(request, 'inventory/product_edit.html', {'form': form})

def product_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('inventory')

def customers(request):
    return render(request, 'inventory/customers.html', {})

def contributions(request):
    contributions = Contribution.objects.all()
    total_contribution = Contribution.objects.aggregate(Sum('amount'))
    return render(request, 'inventory/contributions.html', {'contributions': contributions, 'total_contribution': total_contribution})

def profile(request):
    business = Business.objects.order_by('name')[0]
    return render(request, 'inventory/profile.html', {'business': business})

def presence(request):
    return render(request, 'inventory/presence.html', {})

def sales(request):
    transactions = Transaction.objects.order_by('timestamp')
    transactions = transactions.reverse()
    return render(request, 'inventory/sales.html', {'transactions': transactions})
