from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth

# Create your views here.
def login(request):
    print request.POST
    username=request.POST.get("username",'')
    password=request.POST.get("password",'')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect("/admin/")
    else:
        return HttpResponseRedirect("/")
