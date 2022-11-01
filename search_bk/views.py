from glob import glob
from unittest import result
from django.shortcuts import render, HttpResponse
import mysql.connector as sql
from django.db.models import Q

from addtrn.models import TrainDetails
from search_bk.models import BookingInfo
from django import db
from random import randint

n=5
fromstn=''
tostn=''
z=[]
# Create your views here.
def Search(request):
    db.connections.close_all()
    resultsdisplay = TrainDetails.objects.all()
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="frstn":
                fromstn=value
            if key=="tostn":
                tostn=value
        if fromstn:
            resultsdisplay = resultsdisplay.filter(Q(fromstn__icontains = fromstn))
        
        if tostn:
            resultsdisplay = resultsdisplay.filter(Q(tostn__icontains = tostn))
            
        if fromstn:
            return render(request,"summasearch.html", {'details': resultsdisplay})
        else:
            return render(request,"error.html", {'details': resultsdisplay})
        
    
    return render(request, 'Search_book.html')

user=''
trname=''
seats=''
status='Confirmed'

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
pnr = random_with_N_digits(5)

def Booking(request):
      
    return render(request,'bookingpage.html')
        
def Confirm(request):
    global user, pnr, trname,seats,status
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="user":
                user=value
            if key=="trname":
                trname=value
            if key=="seats":
                seats=value
        
        newbook = BookingInfo(user=user,pnr=pnr,trname=trname,seats=seats,status=status)
        newbook.save()
    
    return render (request,'bookconfirm.html',{'details':pnr})
    
def Searchbook(request):
    
    global fromstn,tostn
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Kishore1912@?",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="frstn":
                fromstn=value
            if key=="tostn":
                tostn=value
                
        
        c="select train_name, train_no from trains where from_stn='{}' and to_stn='{}'".format(fromstn,tostn)
        cursor.execute(c)
        trai=cursor.fetchall()
        if trai==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html",{'names':trai})
    
    return render(request, 'Search_book.html')
