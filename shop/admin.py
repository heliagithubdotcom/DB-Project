from django.contrib import admin

from .models import Store, Product, StoreProduct, Review, Category, ProductCategory

# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(StoreProduct)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(ProductCategory)
