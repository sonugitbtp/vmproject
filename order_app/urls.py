from django.urls import path
from .import views
from. views import add_party,Party_Orders_Reports
from .views import add_party,add_order,party_search
from  django.views.generic import CreateView,ListView
urlpatterns = [
    path('add_party',views.add_party, name='add_party'),
    
    
    
    path('add_order',views.add_order,name='add_order'),
    path('frm_orders',Party_Orders_Reports.as_view(),name='frm_orders'),
    path('party_search',views.party_search,name='party_search'),
    
]