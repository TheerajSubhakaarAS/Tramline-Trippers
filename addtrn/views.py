from django.shortcuts import render, HttpResponse
from addtrn.models import TrainDetails
# Create your views here.

trno =''
trname=''
fromstn=''
tostn=''
Deptime=''
arrtime=''
fare=''

def addtrain(request):
    
    resultsdisplay = TrainDetails.objects.all()
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="trno":
                trno=value
            if key=="trname":
                trname=value
            if key=="fromstn":
                fromstn=value
            if key=="tostn":
                tostn=value
            if key=="Deptime":
                Deptime=value
            if key=="arrtime":
                arrtime=value
            if key=="fare":
                fare=value
        
        newtrn = TrainDetails(trno = trno,trname=trname,fromstn=fromstn,tostn=tostn,Deptime=Deptime,arrtime=arrtime,fare=fare)
        newtrn.save()
        return HttpResponse('Train added Successfully')
        
                
    return render(request, 'addtrn.html')