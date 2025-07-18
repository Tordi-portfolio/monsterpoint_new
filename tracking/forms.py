from django import forms
from .models import Shipment


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        exclude = ['user', 'tracking_id', 'status', 'created_at']
