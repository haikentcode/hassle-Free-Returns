from django.contrib import admin
from home.models import *


class Order_Admin(admin.ModelAdmin):
    list_display=['orderid']

class Variable_Admin(admin.ModelAdmin):
      list_display = ['name']

class Lcat_Admin(admin.ModelAdmin):
      list_display = ['name']          


class Complaint_Admin(admin.ModelAdmin):
       list_display = ['order']

admin.site.register(Order,Order_Admin)
admin.site.register(Variable,Variable_Admin)
admin.site.register(Lcat,Lcat_Admin)
admin.site.register(Complaint,Complaint_Admin)

