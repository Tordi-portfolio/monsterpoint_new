from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('sell', views.sell, name='sell'),
    path('payment', views.payment, name='payment'),
    path('how_to_pay', views.how_to_pay, name='how_to_pay'),
]
