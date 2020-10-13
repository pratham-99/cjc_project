from django.contrib import admin
from .models import Customer, AllOrder


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cname', 'caddr', 'cemail', 'cphone']
admin.site.register(Customer,CustomerAdmin)


class AllOrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'batch_no', 'qty', 'price', 'seller']
admin.site.register(AllOrder, AllOrderAdmin)
