from django  import forms
from .models import *
from django.forms import inlineformset_factory

class Add_Party_Form(forms.ModelForm):
    class Meta:
         model=Party_details
         fields='__all__'

class New_Parent_Order_Form(forms.ModelForm):
     class Meta:
          model=New_Parent_Order
          fields='__all__'

class New_Chiid_Order_Form(forms.ModelForm):
     class Meta:
          cmodel=New_Child_Order
          fields='__all__'

child_formset=inlineformset_factory(New_Parent_Order,New_Child_Order,form= New_Chiid_Order_Form, extra=1,fields='__all__',can_delete=True,fk_name='parent_order')
          