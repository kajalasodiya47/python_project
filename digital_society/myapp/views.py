from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.urls import reverse
"""
Django ORM

get() : fetch data from model and return an object but only single records
        it there are multiple records found with given condition it will thrown an exception

"""
# Create your views here.   
def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(userid = uid)
        context = {
               'uid' : uid,
               'cid' : cid
           }
        return render(request,"myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")

def login(request):
    if "email" in request.session:
       return HttpResponseRedirect(reverse("home"))
    else:
       if request.POST:
        try:
           p_email = request.POST["email"]
           p_password = request.POST["password"]
           print("------->> email ",p_email)
           uid = User.objects.get(email = p_email,password=p_password)
           print("===============>>>> Object ",uid)
           print("========>>>",uid.email)
           print("========>>>",uid.role)
           cid = Chairman.objects.get(userid = uid)
           print("========>>>firstname",cid.firstname)
           request.session['email'] = uid.email
           return HttpResponseRedirect(reverse("home"))
           #return render(request,"myapp/login.html")
           #context = {
           #    'uid' : uid,
           #    'cid' : cid
           #}
           #return render(request,"myapp/index.html",context)
        except Exception as e:
           print("=============>>>>>>> E",e)
           msg = "Invalid email or password"
           return render(request,"myapp/login.html",{'e_msg':msg})
       else:
         print("----> page loaded")
         return render(request,"myapp/login.html")
    
def logout(request):
   if "email" in request.session:
       del request.session['email'] 
       return HttpResponseRedirect(reverse("login"))
   else:
       return HttpResponseRedirect(reverse("login"))
   
def profile(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])
       cid = Chairman.objects.get(userid = uid)
       context = {
               'uid' : uid,
               'cid' : cid
           }  
       return render(request,"myapp\profile.html",context)
    else:
       return HttpResponseRedirect(reverse("login"))