from django.urls import path
from .views import *
urlpatterns = [

    path('', index, name='index'),
    path('category/', category, name='category'),
    path('add_category/', add_category, name='add_category'),
    path('update_category/<int:pk>/', update_category, name='update_category'),
    path('delete_category/<int:pk>/', delete_category, name='delete_category'),


    path('subcategory/', subcategory, name='subcategory'),
    path('add_subcategory/', add_subcategory, name='add_subcategory'),
    path('update_subcategory/<int:pk>/',update_subcategory, name='update_subcategory'),
    path('delete_subcategory/<int:pk>/', delete_subcategory, name='delete_subcategory'),

    path('product/', product, name='product'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),


    
   
]
