from django.db import models
from datetime import date
from products.models import Prod_Category,Prod_Cat_Item_List
# Create your models here.
class Party_details(models.Model):
    party_name=models.CharField(max_length=255,blank=True)
    party_GST=models.CharField(max_length=15,blank=True)
    party_address=models.CharField(max_length=255,blank=True)
    party_city=models.CharField(max_length=50,blank=True)
    party_state=models.CharField(max_length=50,blank=True)
    party_mobile=models.IntegerField(blank=True)

    def __str__(self):
          return  self.party_name
    
class  Order_Assign_To(models.Model):
     emp_name=models.CharField(max_length=50,blank=True,default=None)

     def __str__(self):
          return self.emp_name
     
class Order_Reverted_By(models.Model):
     rev_emp_name=  models.CharField(max_length=50,blank=True,default=None) 
     def __str__(self):
          return self.rev_emp_name

class New_Parent_Order(models.Model):
    party_name = models.ForeignKey(Party_details, on_delete=models.CASCADE,related_name="parent")
    order_rev_emp_name=models.ForeignKey(Order_Reverted_By,on_delete=models.PROTECT,null=True,default=None,related_name="rev_emp")
    order_assign_emp_name=models.ForeignKey(Order_Assign_To,on_delete=models.PROTECT,null=True,default=None,related_name="assign_emp")
    order_date=models.DateField(default=date.today)

    def __str__(self):
          return str(self.id)
class New_Child_Order(models.Model):
    parent_order=models.ForeignKey(New_Parent_Order,on_delete=models.CASCADE,related_name="New_Parent",blank=True)
    Prod_cat=models.ForeignKey(Prod_Category,on_delete=models.CASCADE,related_name="child_prod_cat",blank=True)
    Prod_cat_list=models.ForeignKey(Prod_Cat_Item_List,on_delete=models.CASCADE,related_name="child_cat_list",blank=True)
    prod_qty=models.IntegerField()
    prod_price=models.IntegerField()
    
    order_value=models.IntegerField()
    gst_rate= models.IntegerField()
    gst = models.FloatField()
    total_value=models.FloatField()

    def __str__(self):
         return  str(self.id)