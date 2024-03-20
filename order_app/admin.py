from django.contrib import admin

# Register your models here.
from .models import Party_details,Order_Reverted_By,Order_Assign_To,New_Parent_Order,New_Child_Order
admin.site.register(Party_details)
admin.site.register(Order_Reverted_By)
admin.site.register(Order_Assign_To)
admin.site.register(New_Parent_Order)
admin.site.register(New_Child_Order)

