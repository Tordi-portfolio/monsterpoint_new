from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'full_name', 'email', 'service', 'commodity', 'destination_country', 'status', 'created_at')
    list_filter = ('service', 'commodity', 'status', 'created_at')
    search_fields = ('tracking_id', 'full_name', 'email', 'destination_country')
    readonly_fields = ('tracking_id', 'created_at')
