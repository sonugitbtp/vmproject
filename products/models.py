from django.db import models
from datetime import date

class Prod_Category(models.Model):
    prod_cat_name = models.CharField(max_length=255)
    prod_cat_img=models.ImageField(upload_to='prod_cat_images/')
    prod_cat_desc=models.CharField(max_length=255)
    
    def __str__(self):
          return self.prod_cat_name

class Prod_Cat_Item_List(models.Model):
    item_name=models.CharField(max_length=255,blank=True)
    item_price=models.IntegerField(blank=True)
    item_image=models.ImageField(upload_to='items_images/')
    item_rec_qty=models.IntegerField(blank=True)
    item_rec_date=models.DateField(default=date.today)
    item_price=models.IntegerField(blank=True)
    Hsn_code=models.IntegerField(blank=True)
    prod_cate=models.ForeignKey(Prod_Category,on_delete=models.CASCADE)
    
    def __str__(self):
          return self.item_name