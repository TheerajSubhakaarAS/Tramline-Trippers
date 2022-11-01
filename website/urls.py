"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from home.views import homeaction
from admin_login.views import loginadmin
from addstn.views import addstation, addstn
from deletetrn.views import deletetrain
from addtrn.views import addtrain
from cancel.views import cncl_tkt
from chkpnr.views import chkpnr, printpnr
from chkschedule.views import chk_schedule,schedule
from search_bk.views import Search,Booking,Confirm
from contact.views import contact
from payment.views import payment

urlpatterns = [
    path('',homeaction),
    path('signup/',signaction),
    path('login/',loginaction),
    path('admin/', admin.site.urls),
    path('admin_login/',loginadmin),
    path('admin_login/addstn/',addstation),
    path('admin_login/deletetrn/', deletetrain),
    path('admin_login/addtrn/', addtrain),
    path('login/cancel/',cncl_tkt),
    path('login/chkpnr/',chkpnr),
    path('login/chkschedule/',chk_schedule),
    path('login/searchbk/', Search),
    path('admin_login/addstn/trstn/',addstn),
    path('login/searchbk/search/', Search),
    path('login/searchbk/search/book/', Booking),
    path('login/searchbk/search/book/confirm/', Confirm),
    path('login/chkschedule/schedule/',schedule),
    path('login/chkpnr/checkpnr/',printpnr),
    path('contact/',contact),
    path('payment/',payment),

]
