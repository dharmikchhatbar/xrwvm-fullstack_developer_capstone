from django.contrib import admin
from .models import CarMake, CarModel

# Inline CarModel inside CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra forms shown

# Admin for CarMake with CarModel inline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'country', 'established_year']

# Admin for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'dealer_id', 'type', 'year']
    list_filter = ['type', 'year']
    search_fields = ['name']

# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)