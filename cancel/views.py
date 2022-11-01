from django.http import HttpResponse
from django.shortcuts import render
from search_bk.models import BookingInfo

# Create your views here.
pnr=''
def cncl_tkt(request):
    if request.method =='POST':
        d=request.POST
        for key,value in d.items():
            if key=="pnr":
                pnr=value
        try:
            userinfo = BookingInfo.objects.get(pnr = pnr)
            userinfo.delete()
            return HttpResponse("ticket cancelled successfully")
        
        except:
            return HttpResponse("Please enter a valid pnr")
    return render(request, 'cancel.html')