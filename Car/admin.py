from django.contrib import admin
from .models import Car, Image
from import_export.admin import ImportExportModelAdmin




class CarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ['title', 'year', 'fuel_type', 'price',]

admin.site.register(Car, CarAdmin)

admin.site.register(Image)

