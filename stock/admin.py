from django.contrib import admin
from .models import Company, Seller, Product, StockMovement

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')
    search_fields = ('name', 'email')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'sku', 'price', 'stock_quantity', 'product_status', 'seller', 'company')
    list_filter = ('product_status', 'seller')
    search_fields = ('name_product', 'sku')

admin.site.register(StockMovement)