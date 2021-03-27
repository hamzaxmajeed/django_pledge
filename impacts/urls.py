from django.urls import path
from . import views

app_name = 'impacts'

urlpatterns = [
    path('', views.home, name='home'),
    path('bills/', views.bills, name='bills'),
    path('veg/', views.veg, name='veg'),
]
