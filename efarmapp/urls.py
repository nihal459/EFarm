from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('farmer_registration', views.farmer_registration, name='farmer_registration'),
    path('shop_registration', views.shop_registration, name='shop_registration'),
    path('farmer_login', views.farmer_login, name='farmer_login'),
    path('farmer_home', views.farmer_home, name='farmer_home'),
    path('farmer_profile/<int:pk>/', views.farmer_profile, name='farmer_profile'),
    path('view_shops', views.view_shops, name='view_shops'),
    path('viewshopsingle/<int:pk>/', views.viewshopsingle, name='viewshopsingle'),
    path('product_chart/<int:pk>/', views.product_chart, name='product_chart'),
    path('edit_productchart/<int:pk>/', views.edit_productchart, name='edit_productchart'),
    path('delete_productchart/<int:pk>/', views.delete_productchart, name='delete_productchart'),
    path('business/<int:pk>/', views.business, name='business'),
    path('farmer_business/<int:pk>/', views.farmer_business, name='farmer_business'),
    path('view_doctors', views.view_doctors, name='view_doctors'),
    path('update_farmerbusiness/<int:pk>/', views.update_farmerbusiness, name='update_farmerbusiness'),
    path('farmer_accept_business/<int:pk>/', views.farmer_accept_business, name='farmer_accept_business'),
    path('amount_received/<int:pk>/', views.amount_received, name='amount_received'),
    path('products_delivered/<int:pk>/', views.products_delivered, name='products_delivered'),

    path('delete_farmerbusiness/<int:pk>/', views.delete_farmerbusiness, name='delete_farmerbusiness'),




    
    path('SignOut', views.SignOut, name='SignOut'),

    path('shop_login', views.shop_login, name='shop_login'),
    path('shop_home', views.shop_home, name='shop_home'),
    path('shop_profile/<int:pk>/', views.shop_profile, name='shop_profile'),
    path('price_chart/<int:pk>/', views.price_chart, name='price_chart'),
    path('delete_pricechart/<int:pk>/', views.delete_pricechart, name='delete_pricechart'),
    path('edit_pricechart/<int:pk>/', views.edit_pricechart, name='edit_pricechart'),
    path('view_farmers', views.view_farmers, name='view_farmers'),
    path('shop_business/<int:pk>/', views.shop_business, name='shop_business'),
    path('update_shopbusiness/<int:pk>/', views.update_shopbusiness, name='update_shopbusiness'),
    path('shop_accept_business/<int:pk>/', views.shop_accept_business, name='shop_accept_business'),
    path('amount_paid/<int:pk>/', views.amount_paid, name='amount_paid'),
    path('products_received/<int:pk>/', views.products_received, name='products_received'),
    path('viewfarmersingle/<int:pk>/', views.viewfarmersingle, name='viewfarmersingle'),
    path('shop_business_request/<int:pk>/', views.shop_business_request, name='shop_business_request'),
    path('delete_shop_business/<int:pk>/', views.delete_shop_business, name='delete_shop_business'),
    path('manage_doctors', views.manage_doctors, name='manage_doctors'),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name='delete_doctor'),



    
    path('SignOut2', views.SignOut2, name='SignOut2'),


    
]