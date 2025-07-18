from . import views
from django.urls import path

urlpatterns = [
    path('create_shipment', views.create_shipment, name='create_shipment'),
    path('track_shipment', views.track_shipment, name='track_shipment'),
    path('donate/', views.donate, name='donate'),
    path('donate_payment/', views.donate_payment, name='donate_payment'),
    path('donation_text/', views.donation_text, name='donation_text'),
]

