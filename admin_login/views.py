from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginadmin(request):
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
        
        c="select * from admin where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"admin.html")

    return render(request,'adminlogin.html')