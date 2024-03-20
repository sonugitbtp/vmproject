
from django.urls import path
from.import views
from .views import demo

urlpatterns = [
    path('demo',views.demo, name='demo'),
    
    
    
]