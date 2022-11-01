from django.shortcuts import render
from search_bk.models import BookingInfo
from django.db.models import Q


# Create your views here.
def chkpnr(request):
    return render(request, 'pnr.html')
pnr = ''
def printpnr(request):
    resultsdisplay = BookingInfo.objects.all()
    global pnr
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="pnr":
                pnr=value
        if pnr:
            resultsdisplay = resultsdisplay.filter(Q(pnr__icontains = pnr))
    
    return render (request,'pnrcheck.html',{'details':resultsdisplay})