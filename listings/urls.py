from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'), 
    path('all_listings',views.all_listings,name='all_listings')  
]
