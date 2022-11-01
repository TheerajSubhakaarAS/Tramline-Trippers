from django.shortcuts import render, HttpResponse
from addtrn.models import TrainDetails
from addstn.models import Stationdetails
from django.db.models import Q


# Create your views here.
def addstation(request):
    return render(request, 'addstn.html')

trno =''
trname=''
fromstn=''
tostn=''
Deptime=''
arrtime=''
fare=''

def addstn(request):
    
    global trno, trname, fromstn, tostn, Deptime,arrtime,fare
    resultsdisplay = TrainDetails.objects.all()
    
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="trname":
                trname=value
            if key=="stname":
                tostn=value
            if key=="arrtime":
                arrtime=value
            if key=="fare":
                fare=value
        resultsdisplay = resultsdisplay.filter(Q(trname__icontains = trname))
        if resultsdisplay:
        
            newtrn = Stationdetails(trnamee = trname,stn=tostn,time=arrtime,fare=fare)
            newtrn.save()
            resulstsdisplay2 = Stationdetails.objects.all()
            resulstsdisplay2 = resulstsdisplay2.filter(Q(trnamee__icontains = trname))
        
        return render(request, 'dummy.html',{'details': resulstsdisplay2})
    
    
    