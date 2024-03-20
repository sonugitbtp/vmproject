from django.db import models
from products.models import Prod_Category,Prod_Cat_Item_List
from datetime import date

class  Order_Assign_To(models.Model):
     emp_name=models.CharField(max_length=50,blank=True,default=None)

     def __str__(self):
          return self.emp_name
class Order_Reverted_By(models.Model):
     rev_emp_name=  models.CharField(max_length=50,blank=True,default=None) 
     def __str__(self):
          return self.rev_emp_name


class Party_details(models.Model):
    party_name=models.CharField(max_length=255,blank=True)
    party_GST=models.CharField(max_length=15,blank=True)
    party_address=models.CharField(max_length=255,blank=True)
    party_city=models.CharField(max_length=50,blank=True)
    party_state=models.CharField(max_length=50,blank=True)
    party_mobile=models.IntegerField(blank=True)

    def __str__(self):
          return  self.party_name
        









    


    
    
    