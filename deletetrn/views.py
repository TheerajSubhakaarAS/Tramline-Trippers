from django.shortcuts import render, HttpResponse
from addtrn.models import TrainDetails
from django.db.models import Q
trname=''


# Create your views here.
def deletetrain(request):
    global trname
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="trname":
                trname=value
        try:
            resultsdisplay = TrainDetails.objects.all()
            traininfo = resultsdisplay.filter(Q(trname__icontains = trname))
            traininfo.delete()
            return HttpResponse("Train deleted successfully")
        
        except:
            return HttpResponse("Please enter a valid train")
    
    return render(request, 'deletetrn.html')