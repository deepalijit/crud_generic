from django.contrib import admin
from .models import Laptop

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id','lname','lcompany','lram','lrom','lprocessor','lweight']

admin.site.register(Laptop,LaptopAdmin)
