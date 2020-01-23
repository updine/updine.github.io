from django.shortcuts import render,redirect
from .models import Product, Business, Transaction, Contribution
from .forms import ProductEditForm, NewProductForm
from django.shortcuts import get_object_or_404
from django.db.models import Sum
import folium
from folium import plugins
from folium.plugins import HeatMap

def home(request):
    hits = (Product.objects.order_by('sales_count')).reverse()[0:3]
    total_contribution = Contribution.objects.aggregate(Sum('amount'))
    total_sales = Transaction.objects.aggregate(Sum('amount'))
    user_count = Transaction.objects.count()
    contributions = Contribution.objects.all()[0:20]
    transactions = (Transaction.objects.order_by('timestamp')).reverse()[0:20]

    dict = {
        'hits': hits,
        'total_contribution': total_contribution,
        'total_sales': total_sales,
        'user_count' : user_count,
        'contributions': contributions,
        'transactions': transactions,

    }
    return render(request, 'inventory/home.html', dict)

def inventory_view(request):
    products = Product.objects.filter()
    hits_up = Product.objects.order_by('sales_count')[0:3]
    hits_down_all = Product.objects.order_by('sales_count')
    hits_down = hits_down_all.reverse()[0:3]
    return render(request, 'inventory/inventory_view.html', {'products': products,'hits_up': hits_up, 'hits_down': hits_down})

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

def get_user_locations(request):
    all_lat = Transaction.objects.values('lat')
    all_long = Transaction.objects.values('long')
    location = [(all_lat[i], all_long[i]) for i in range(0, len(all_lat))] 
    return JsonResponse(location, safe=False)

def customers(request):
    starting_Lat = 40.712742
    starting_Long = -74.013382
    map_hooray = folium.Map(location=[starting_Lat, starting_Long],
                        tiles = "Stamen Toner",
                        zoom_start = 11,
                        max_zoom = 11,
                        )
    all_lat = Transaction.objects.values('lat')
    all_long = Transaction.objects.values('long')
    heat_data = [[all_lat[i].get('lat'), all_long[i].get('long'), 75] for i in range(len(all_lat))]
    HeatMap(heat_data, 
            min_opacity = 0.01, 
            max_val = 1.5, 
            blur = 20,
        ).add_to(map_hooray)
    folium.plugins.Fullscreen(position='topright',
                        title='Full Screen',
                        title_cancel='Exit Full Screen',
                        force_separate_button=True
                        ).add_to(map_hooray)
    context = {'map': map_hooray._repr_html_()}
    return render(request, 'inventory/customers.html', context)

def contributions(request):
    contributions = Contribution.objects.all()
    total_contribution = Contribution.objects.aggregate(Sum('amount'))
    top_months = Contribution.objects.order_by('amount')
    top_months = top_months.reverse()[0:3]
    return render(request, 'inventory/contributions.html', {'contributions': contributions, 'total_contribution': total_contribution, 'top_months': top_months})

def profile(request):
    business = Business.objects.order_by('name')[0]
    return render(request, 'inventory/profile.html', {'business': business})

def presence(request):
    return render(request, 'inventory/presence.html', {})

def sales(request):
    transactions = Transaction.objects.order_by('timestamp')
    transactions = transactions.reverse()
    total_sales = Transaction.objects.aggregate(Sum('amount'))
    return render(request, 'inventory/sales.html', {'transactions': transactions, 'total_sales': total_sales})
