from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('offer',)}
    list_display = ('offer', 'starting_date', 'ending_date')

admin.site.register(Product,ProductAdmin)