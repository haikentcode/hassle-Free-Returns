from django.shortcuts import render
from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
from home.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout ,authenticate
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url='/login/')
def logout(request):
     logout(request)


@login_required(login_url='/login/',redirect_field_name="/")
def index(request):
	email = authenticate()
	print email
        return render(request,'home/home.html',{'user':email})
         



@csrf_exempt
@login_required(login_url='/login/')
def getimei(request):
	if request.POST:
       	   oid=request.POST["oid"]
       	   try:
              order = Order.objects.get(orderid=oid)
              complained = Complaint.objects.get(order=order)
              request.session["orderid"]=oid
              if order:
                  return render(request,'home/getimei.html',{'order':order,'complained':complained})
           except:
              return HttpResponse("Invalid Order ID. Please re-enter")


@csrf_exempt
@login_required(login_url='/login/')
def getOrdeIdInfo(request):
       if request.POST:
       	   oid=request.POST["oid"]
       	   try:
              order=Order.objects.get(orderid=oid)
              request.session["orderid"]=oid
              if order:
                  return render(request,'home/orderinfo.html',{'order':order})
           except:
              return HttpResponse("Invalid Order ID. Please re-enter")


def ordercheck(request,orderid):
	    try:
	       orderid = request.session.get("orderid")
	       complainId="shopclues.cid."+str(orderid)
	       order=Order.objects.get(orderid=orderid) 
               return render(request,'home/ordercheck.html',{'complainId':complainId,'order':order})
            except:
               return HttpResponse("Invalid Order ID. Please re-enter")   

 
def complained(request):
	  if request.POST:
	       orderid = request.session.get("orderid")
	       complainId = "shopclues.cid."+str(orderid)
               wrongProduct = request.POST.get("wrongProduct",False)
               lookingFor =  request.POST.get("lookingFor",None)
               complained = Complaint()
               order = Order.objects.get(orderid=orderid)
               complained.order = order
               complained.wrongProduct = wrongProduct
               complained.lookingFor = lookingFor
               complained.ccid = "shopclues.cid."+str(orderid)
               complained.other = request.POST.get("othertext",None)
               complained.save()
               for variable in order.lcat.variables.all():
               	    if request.POST.get(variable.name,False):  
               	         complained.issue.add(variable)
               complained.save()
          return HttpResponse("Customer Complaint is Successfully Registered")              



def imeifulfillment(request):	
      if request.POST:
      	   orderid = request.session.get("orderid")
      	   order = Order.objects.get(orderid=orderid)
	   complainId = "shopclues.cid."+str(orderid)
	   complained = Complaint.objects.get(ccid=complainId)
	   pdv = eval(str(request.POST.get("Physical Damage",False)))
	   pnwv =eval(str(request.POST.get("Phone Not Working",False)))
           issue=[ x.name for x in complained.issue.all()]
	   pdc = "Physical Damage" in issue
	   pnwc = "Phone Not Working" in issue
	   
           print pdc,pdv,pnwc,pnwv
	   if pdc & pdv or  pnwv & pnwc :
	   	print "in 1"
	        return HttpResponse("RMA Approved")

	   if (not pdc) & pdv:
	   	 print "in 2"
	         return HttpResponse("RMA Not Approved")

	   if (not pnwc) & pnwv:
	   	 print "in 3"
	         return HttpResponse("RMA Not Approved")
           try :
	      issue.remove("Physical Damage")
	      issue.remove("Phone Not Working")
	   except:
	      pass   

	   for cond in issue:
	   	  print cond
	   	  if bool(request.POST.get(cond,False)) :
	   	  	 return HttpResponse("RMA Approved")

	   return HttpResponse("RMA Not Approved")	  


      return  render(request,'home/imeifulfillment.html',{})     


def wrongproduct(request):
	   orderid = request.session.get("orderid")
      	   order = Order.objects.get(orderid=orderid)
	   complainId = "shopclues.cid."+str(orderid)
	   complained = Complaint.objects.get(ccid=complainId)
	   x=eval(str(complained.wrongProduct))
	   if  x:
	   	print "hai"
	   	return HttpResponse("RMA Approved")
	   else:
	        return HttpResponse("RMA Not Approved") 	


