from __future__ import unicode_literals

from django.db import models



class Variable(models.Model):
       name = models.CharField(max_length=100,blank=True,null=True) 
       def __str__(self):
           return "%s" % (self.name)


class  Lcat(models.Model):
       name = models.CharField(max_length=100,blank=True,null=True)
       variables = models.ManyToManyField(Variable)
       def __str__(self):
          return "%s" % (self.name)


class Order(models.Model):
	orderid = models.CharField(max_length=100,blank=True,null=True)
	productName = models.CharField(max_length=100,blank=True,null=True)
	color = models.CharField(max_length=100,blank=True,null=True)
	imei = models.CharField(max_length=100,blank=True,null=True)
        lcat = models.ForeignKey(Lcat)
        def __str__(self):
            return "%s" % (self.orderid)



class  Complaint(models.Model):
	   order =  models.ForeignKey(Order)
	   ccid = models.CharField(max_length=100,blank=True,null=True)
	   issue = models.ManyToManyField(Variable)
	   wrongProduct = models.CharField(max_length=10,blank=True,null=True)
	   other = models.CharField(max_length=100,blank=True,null=True)
	   lookingFor = models.CharField(max_length=20,blank=True,null=True)







