from django.contrib import admin
from django.urls import path,include

from .import views


urlpatterns = [
    path('',views.store,name='store'),
    path('offers/',views.offer_register,name='off_reg'),
    path('category/<slug:category_slug>/',views.store,name='offers_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',views.offer_detail,name='offer_detail'),
    path('search/', views.search, name='search'),
]




























