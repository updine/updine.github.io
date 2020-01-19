from django.contrib import admin
from .models import Product, Business, Transaction, Contribution

admin.site.register(Product)
admin.site.register(Business)
admin.site.register(Transaction)
admin.site.register(Contribution)
