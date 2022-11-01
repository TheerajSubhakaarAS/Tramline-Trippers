from django.shortcuts import render
from addtrn.models import TrainDetails
from addstn.models import Stationdetails
from django.db.models import Q


# Create your views here.
def chk_schedule(request):
    return render(request, 'schedule.html')

trname=''
        
def schedule(request):
    resultsdisplay = Stationdetails.objects.all()
    global trname
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="trname":
                trname=value
        if trname:
            resultsdisplay = resultsdisplay.filter(Q(trnamee__icontains = trname))
    
    return render(request,'trainschedule.html',{'details':resultsdisplay})
