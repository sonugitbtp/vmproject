from django.views.generic import ListView

from django.urls import path
from.import views
from .views import index,Items_List

urlpatterns = [
    path('',views.index,name='index'),
    path('products/',views.prodect_details,name='products'),
    path('items_list/',Items_List.as_view(template_name='Products/items_list.html'),name='items_list')
]