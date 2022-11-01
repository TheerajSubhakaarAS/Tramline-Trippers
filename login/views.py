from django.shortcuts import render
from login.models import Logininfo
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
#def loginprint(request):
#    resultsdisplay = Logininfo.objects.all()
#    return render(request,"index.html",{'logindetails': resultsdisplay})
    

def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Kishore1912@?",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"user.html")

    return render(request,'login_page.html')