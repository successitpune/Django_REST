from django.contrib import admin
from django.db import IntegrityError
from django.contrib import messages
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'date', 
        'customer_name', 
        'contact_no', 
        'alternate_no', 
        'address', 
        'company_name', 
        'model_no', 
        'physical_condition', 
        'estimated_price', 
        'imei_1', 
        'imei_2'
    ]

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except IntegrityError as e:
            messages.error(request, f"Error saving customer: {e}")
            return super().changeform_view(request, None, form_url='', extra_context=None)
