from typing import Any
from django.shortcuts import render
from .models  import *
# Create your views here.
from django.http import HttpResponse
from django import forms
from .forms import *
#from  django.views.generic import CreateView,ListView
from  django.views.generic.list import ListView



class Party_Orders_Reports(ListView):
    model = Party_details
    context_object_name='orders'
    template_name = "order_app/party_orders_search.html"
    
def party_search(request):

    name=request.GET.get('p_name')
    from_date=request.GET.get('from_date')
    to_date=request.GET.get('to_date')
    name2=Party_details.objects.filter(party_name=name).values()
    orders=New_Parent_Order.objects.filter(party_name__party_name=name,order_date__gte=from_date,order_date__lte=to_date).all()
    

    
    
    return render(request,'order_app/party_order_search_details.html',{'p_name':name,'name':name2,'orders':orders,'f_date':to_date})
    #return HttpResponse("search")








def add_order(request):
   if request.method=='GET':
      party_form=New_Parent_Order_Form(request.GET or None)
      child_form=child_formset(queryset=New_Child_Order.objects.none())
   elif request.method=='POST':
       party_form=New_Parent_Order_Form(request.POST)
       child_form=child_formset(request.POST)
       if party_form.is_valid() and child_form.is_valid():
             party_form=party_form.save()
             for x in child_form: 
                 form= x.save(commit=False)  
                 form.parent_order=party_form
                 form.save()
          
          

   return render(request,'order_app/add_order.html',{'party_form':party_form,'child_form':child_form})



def  add_party(request):
    
    context={}
    
    if request.method=='POST':
        #name=request.POST['party_name']
        party_form_data=Add_Party_Form(request.POST)
        if party_form_data.is_valid():
            party_form_data.save()
        return HttpResponse("your form have been submitted")
    else:
        context['form']=Add_Party_Form()

    return render(request,'order_app/add_party.html',context)



    

