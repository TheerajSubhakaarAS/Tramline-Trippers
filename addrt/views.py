from django.shortcuts import render

# Create your views here.
def addroute(request):
    return render(request, 'addrt.html')