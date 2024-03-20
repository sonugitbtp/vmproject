from django.shortcuts import render
from django.http import HttpResponse
from .models import Prod_Category,Prod_Cat_Item_List
from django.views.generic.list import ListView


def order_pro_history(request):
   return HttpResponse("order process")





def index(request):
   
   return render(request,template_name='base.html')


def prodect_details(request):
   #return HttpResponse("products")
   prod_cat_list= Prod_Category.objects.all()
   #return render(request,template_name='Products\products.html')
   return render(request,'Products/products.html',context={'prod_cat_list':prod_cat_list})

class Items_List(ListView):
   model=Prod_Cat_Item_List
   context_object_name='items'