from django.contrib import admin
from .models import Brand, Mobile, Specification

# Customize the admin panel for Brands
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')  # Columns to display in the admin list view
    search_fields = ('name',)             # Enable search by brand name
    list_per_page = 10                    # Paginate after 10 entries

# Customize the admin panel for Mobiles
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price')  # Columns to display
    search_fields = ('name', 'brand__name')         # Search by mobile name and brand name
    list_filter = ('brand',)                        # Filter by brand
    list_per_page = 10                              # Paginate after 10 entries

# Customize the admin panel for Specifications
@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile', 'processor', 'ram', 'storage', 'battery', 'screen_size', 'camera', 'os')  # Columns to display
    search_fields = ('mobile__name', 'processor', 'os')  # Search by mobile name, processor, or OS
    list_per_page = 10                                   # Paginate after 10 entries
