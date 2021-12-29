import random
import requests
import json
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from json import dumps
from django.shortcuts import render ,redirect
from django.shortcuts import (render_to_response)
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from rapido.models import Category,Location,Vendor,Vehicle,Chauffeur,Company,Bookings,Dutyslip,ClientInvoice,Chauffeur_vehicel,Smsforothers,Billingsummary

from rapido.models import City,Slab,Vendortype,Bookingstatus,Dutyslipstatus,Invoicestatus,Servicetype,Billingbase,Companytype,Vehicle_varient,Category,Travelservicetype,Vendortype,Bookingsms,Dutyslipsms,Cancelsms
from rapido.models import Location,Vendor,Vehicle,Chauffeur,Company,Bookings,Dutyslip,VendorInvoice,Bookingstatus,Dutyslipstatus,Invoicestatus,Billingbase,City_ratecard,Outstation_ratecard,Airport_ratecard,Company_city_ratecard,Company_outstation_ratecard,Company_airport_ratecard

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer,Airport_ratecardSerializer

from rapido.forms import CategoryForm,UserForm
from django.http import Http404
# Create your views here.
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string, get_template

import datetime
import urllib
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from rest_framework import viewsets
from datetime import datetime, date, time
import xlrd
import django_excel as excel

data = [
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],]




@login_required
def check_booking_present(request):
    context = RequestContext(request)
    context_dict = {}
    data = request.data
    # date=data['pickup_date_time']
    # hrs= data['pickup_date_time']
    # d2= datetime.datetime.strptime(u'date_in', '%Y-%m-%d')
    # createddate =i.created_date.strftime("%d-%b-%Y")

    try:
        booking = Bookings.objects.get(guest_name = data['guest_name'],guest_phoneno= data['guest_phoneno'], pickup_date_time__contains=date, pickup_date_time__contains_hrs=hrs, pick_up_location= data['pick_up_location'])
        data= {'status':1,'bookingid':booking.bookingid}
    except Exception, e:
        x = e
        data= {'status':0, 'message':"Booking not yet created"}


    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type="application/json")


#
def bookingsms(request,bookingid):
    try:
        booking = Bookings.objects.get(pk=bookingid)
        created_by = request.user
        booking_sms = Bookingsms(created_by=created_by,booking=booking)
        booking_sms.save()
    except Exception, e:
        x = e
    return HttpResponse(" booking_sms created")

def dutyslipsms(request,tripid):
    try:
        dutyslip = Dutyslip.objects.get(pk=bookingid)
        created_by = request.user
        dutyslip_sms = Dutyslipsms(created_by=created_by,dutyslip=dutyslip)
        dutyslip_sms.save()
    except Exception, e:
        x = e
    return HttpResponse("dutyslip_sms created")

#-------------------------------------------------------------------------------------
def sendbookingemail(request,bookingid):
    booking = Bookings.objects.get(pk=bookingid)  
    print "books email ge bantu"
    context = {'booking': booking}

    html_content = render_to_string('rapido/bookingemail.html', context=context).strip()
    guest_email = booking.guest_email
    booker_email = booking.booking_email

    company_email = booking.company.company_email
    company_manager_email = booking.company.company_manager_email

    subject = 'RapidoTravels: Booking Confirmation: for Guest:'+booking.guest_name+' and Booking ID: RTIPL-'+booking.servicing_city.city_code+'-'+booking.booking_id
    from_email = 'bookings@rapidotravels.co.in'
    reply_to = ['bookings@rapidotravels.co.in']
    # to = ['manju24j@gmail.com']
    # cc =[]
    to = [guest_email,booker_email]
    cc =['pramod.cr@rapidotravels.co.in','bookings@rapidotravels.co.in','jins@rapidotravels.co.in']
    bcc =['manju24.rymec@gmil.com']

    msg = EmailMultiAlternatives(subject, html_content, to=to, from_email=from_email, reply_to=reply_to, bcc=bcc, cc=cc)  
    msg.content_subtype = 'html'  # Main content is text/html  
    msg.mixed_subtype = 'related'  # This is critical, otherwise images will be displayed as attachments!
    msg.send()
    try:
        booking = Bookings.objects.get(pk=bookingid)
        updated_by = request.user
        booking_sms = Bookingsms.objects.get(booking=booking)
        booking_sms.emailsent = True
        booking_sms.updated_by = updated_by
        booking_sms.save()
    except Exception, e:
        booking = Bookings.objects.get(pk=bookingid)
        created_by = request.user
        booking_sms = Bookingsms(created_by=created_by,booking=booking)
        booking_sms.emailsent = True 
        booking_sms.save()
    print "email sent aytu"
    print msg
    return HttpResponse(msg)

def sendbookingsms(request,bookingid):
    booking = Bookings.objects.get(pk=bookingid)  
    print "booking sms"
    bookingno = "RTIPL-"+booking.servicing_city.city_code+"-"+ booking.booking_id
    guest_phoneno = booking.guest_phoneno
    guest_name = booking.guest_name
    client = booking.company

    address = booking.pick_up_location
    print address
    address = urllib.quote_plus(address)

    print address
    #below is used for sms readable format querystring to percentage encoding like %26
    address =  urllib.quote(address, safe='')
    print address

    client=str(client)
    client = urllib.quote(client, safe='') 
    print client

    pickuptime =booking.pickup_date_time
    date = pickuptime.date()
    date = str(date)
    time = pickuptime.time()
    time = str(time)

    # userbookingsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+guest_phoneno+'&sender=RAPIDO&message=Greetings+from+RapidoTravels:+Hi'+guest_name+',+we+have+received+booking+from,'+client+'pickup@:'+date+',+'+time+',and+keep+this+Id+for+further+reference+'+bookingno+'&flash=0&unicode=0')
    userbookingsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+guest_phoneno+'&sender=RAPIDO&message=Greetings+from+RapidoTravels:+Hi+'+guest_name+',+we+have+received+booking+pickup:@:'+date+',+'+time+',+and+keep+this+Id+for+further+reference+'+bookingno+'&flash=0&unicode=0')
    print userbookingsms
    if userbookingsms.status_code == 200:
        try:
            booking = Bookings.objects.get(pk=bookingid)
            updated_by = request.user
            booking_sms = Bookingsms.objects.get(booking=booking)
            booking_sms.smssent = True
            booking_sms.updated_by = updated_by
            booking_sms.save()
        except Exception, e:
            booking = Bookings.objects.get(pk=bookingid)
            created_by = request.user
            booking_sms = Bookingsms(created_by=created_by,booking=booking)
            booking_sms.smssent = True 
            booking_sms.save()
    print "message send aytu"
    return HttpResponse(userbookingsms)



@csrf_exempt
def sendbookingsmsforothers(request,bookingid):
    booking = Bookings.objects.get(pk=bookingid)  
    phoneno = request.POST['phoneno']

    bookingno = "RTIPL-"+booking.servicing_city.city_code+"-"+ booking.booking_id
    guest_name = booking.guest_name
    client = booking.company

    address = booking.pick_up_location
    address = urllib.quote_plus(address)

    #below is used for sms readable format querystring to percentage encoding like %26
    address =  urllib.quote(address, safe='')

    client=str(client)
    client = urllib.quote(client, safe='') 

    pickuptime =booking.pickup_date_time
    date = pickuptime.date()
    date = str(date)
    time = pickuptime.time()
    time = str(time)

    # userbookingsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+guest_phoneno+'&sender=RAPIDO&message=Greetings+from+RapidoTravels:+Hi'+guest_name+',+we+have+received+booking+from,'+client+'pickup@:'+date+',+'+time+',and+keep+this+Id+for+further+reference+'+bookingno+'&flash=0&unicode=0')
    userbookingsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+phoneno+'&sender=RAPIDO&message=Greetings+from+RapidoTravels:we+have+received+booking+for+guest:+'+guest_name+'+and+pickup:@:'+date+',+'+time+',+and+keep+'+bookingno+'+Id+for+further+reference&flash=0&unicode=0')
    print userbookingsms
    message = "Greetings from RapidoTravels: we have received booking for guest: "+guest_name+" and pickup:@:"+date+","+time+"and keep "+bookingno+" Id for further reference"
    if userbookingsms.status_code == 200:
        created_by = request.user
        booking_sms = Smsforothers(created_by=created_by,phoneno=phoneno,booking_id=booking.booking_id,message=message)
        booking_sms.smssent = True 
        booking_sms.save()
    print "message send aytu"
    return HttpResponse(userbookingsms)


@csrf_exempt
def sendtripdetailsmsforothers(request,tripid):
    phoneno = request.POST['phoneno']
    print " tripdetailemail ge bantu"
    booking = Dutyslip.objects.get(pk=tripid)
    allocated_vehicle=booking.allocated_vehicle
    vehicle_no = booking.vehicle_no
    chauffeur_name = booking.chauffeur_name
    chauffeur_phoneno = booking.chauffeur_phoneno
    bookingno= "RTIPL-"+booking.booking.servicing_city.city_code+"-"+ booking.booking.booking_id
    guest_name = booking.booking.guest_name
    guest_phoneno = phoneno

    usertripsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+guest_phoneno+'&sender=RAPIDO&message=Hi+,In+Reference+with+your+Booking+no:'+bookingno+',+for+guest:+'+guest_name+',+'+allocated_vehicle+'+('+vehicle_no+')+and+Chauffeur:'+chauffeur_name+'+('+chauffeur_phoneno+')+has+been+allocated+,+contact+driver+for+onward+Journey+&flash=0&unicode=0')
    print usertripsms
    print guest_phoneno
    print usertripsms.status_code
    message = "Hi In Reference with your Booking no:"+bookingno+"for guest: "+guest_name+', '+allocated_vehicle+"("+vehicle_no+") and Chauffeur:"+chauffeur_name+"("+chauffeur_phoneno+")has been allocated,contact driver for onward Journey"
    if usertripsms.status_code == 200:
        created_by = request.user
        booking_sms = Smsforothers(created_by=created_by,phoneno=phoneno,booking_id=booking.booking.booking_id,message=message)
        booking_sms.smssent = True 
        booking_sms.save()
    print "message send aytu"
    return HttpResponse(usertripsms)


def sendtripdetailemail(request,tripid):
  
    print " tripdetailemail ge bantu "
    booking = Dutyslip.objects.get(pk=tripid)  
    context = {'booking': booking}
    
    html_content = render_to_string('rapido/tripemail.html', context=context).strip()
    
    company_email = booking.booking.company.company_email
    company_manager_email = booking.booking.company.company_manager_email
    guest_email = booking.booking.guest_email
    booker_email = booking.booking.booking_email

    subject = 'RapidoTravels: Vehicle And Chauffeur Details'+'RTIPL-'+booking.booking.servicing_city.city_code+'-'+booking.booking.booking_id
    from_email = 'bookings@rapidotravels.co.in'
    reply_to = ['bookings@rapidotravels.co.in']
    to = [guest_email,booker_email]
    cc =['pramod.cr@rapidotravels.co.in','bookings@rapidotravels.co.in','jins@rapidotravels.co.in']
    bcc =['manju24.rymec@gmil.com']

    msg = EmailMultiAlternatives(subject, html_content, to=to, from_email=from_email, reply_to=reply_to, bcc=bcc, cc=cc)  
    msg.content_subtype = 'html'  # Main content is text/html  
    msg.mixed_subtype = 'related'  # This is critical, otherwise images will be displayed as attachments!
    msg.send()

    
    print msg

    try:
        dutyslip = Dutyslip.objects.get(pk=tripid)
        updated_by = request.user
        dutyslip_sms = Dutyslipsms.objects.get(dutyslip=dutyslip)
        dutyslip_sms.emailsent = True
        dutyslip_sms.updated_by = updated_by
        dutyslip_sms.save()
    except Exception, e:
        dutyslip = Dutyslip.objects.get(pk=tripid)
        created_by = request.user
        dutyslip_sms = Dutyslipsms(created_by=created_by,dutyslip=dutyslip)
        dutyslip_sms.emailsent = True
        dutyslip_sms.save()

    return HttpResponse(msg)

#-------------------------------------------------

def sendcancelemail(request,bookingid):
    booking = Bookings.objects.get(pk=bookingid)
    context = {'booking': booking}
    
    html_content = render_to_string('rapido/cancelemail.html', context=context).strip()
    
    guest_email = booking.guest_email
    booker_email = booking.booking_email

    subject = 'Cancellation of Booking:'+'RTIPL-'+booking.servicing_city.city_code+'-'+booking.booking_id
    from_email = 'bookings@rapidotravels.co.in'
    reply_to = ['bookings@rapidotravels.co.in']
    to = [guest_email,booker_email]
    cc =['pramod.cr@rapidotravels.co.in','bookings@rapidotravels.co.in','jins@rapidotravels.co.in']
    bcc =['manju24.rymec@gmil.com']

    msg = EmailMultiAlternatives(subject, html_content, to=to, from_email=from_email, reply_to=reply_to, cc=cc,bcc=bcc)  

    msg.content_subtype = 'html'  # Main content is text/html  
    msg.mixed_subtype = 'related'  # This is critical, otherwise images will be displayed as attachments!
    msg.send()

    print msg

    try:
        updated_by = request.user
        cancel_sms = Cancelsms.objects.get(booking=booking)
        cancel_sms.useremailsent = True
        cancel_sms.updated_by = updated_by
        cancel_sms.save()
    except Exception, e:
        created_by = request.user
        cancel_sms = Cancelsms(created_by=created_by,booking=booking)
        cancel_sms.useremailsent = True
        cancel_sms.save()

    return HttpResponse(msg)

def sendcancelsms(request,bookingid):
  
    booking = Bookings.objects.get(pk=bookingid)  
    bookingno = "RTIPL-"+booking.servicing_city.city_code+"-"+ booking.booking_id
    print " cancel1"

    cityname = str(booking.servicing_city.name)
    guest_phoneno = booking.guest_phoneno
    guest_name = booking.guest_name

    pickuptime =booking.pickup_date_time
    date = pickuptime.date()
    date = str(date)
    time = pickuptime.time()
    time = str(time)
    userbookingsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+guest_phoneno+'&sender=RAPIDO&message=Dear+Customer,+As+per+your+request,+pickup:@:'+date+',+'+time+',in+('+cityname+'),+for+a+booking+Id:+'+bookingno+'+Has+been+cancelled.+Helpline+call:08026595567+&flash=0&unicode=0')
    print userbookingsms
    # userbookingsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+guest_phoneno+'&sender=RAPIDO&message=RapidoTravels:we+have+cancelled+booking+for+guest:+'+guest_name+'+and+pickup:@:'+date+',+'+time+',in+('+cityname+'),+as+per+guest+request+for+:a+booking+Id:+'+bookingno+'Helpline+call:08026595567+&flash=0&unicode=0')
    if userbookingsms.status_code == 200:
        try:
            updated_by = request.user
            cancel_sms = Cancelsms.objects.get(booking=booking)
            cancel_sms.usersmssent = True
            cancel_sms.updated_by = updated_by
            # print userbookingsms,"15"
            cancel_sms.save()
            # print userbookingsms,"16"
        except Exception, e:
            created_by = request.user
            cancel_sms = Cancelsms(created_by=created_by,booking=booking)
            cancel_sms.usersmssent = True
            # print userbookingsms,"23"
            cancel_sms.save()
            # print userbookingsms,"24"
    print "message send aytu"
    return HttpResponse(userbookingsms)





#---------------------------------------------------


def sendtripdetailsmsforuser(request,tripid):

    print "sendtripdetailsmsforuser"
    print tripid
    booking = Dutyslip.objects.get(pk=tripid)
    print booking
    allocated_vehicle=booking.allocated_vehicle
    print "sendtripdetailsmsforuser1"
    vehicle_no = booking.vehicle_no
    chauffeur_name = booking.chauffeur_name
    chauffeur_phoneno = booking.chauffeur_phoneno
    bookingno= "RTIPL-"+booking.booking.servicing_city.city_code+"-"+ booking.booking.booking_id
    print "sendtripdetailsmsforuser"
    guest_name = booking.booking.guest_name
    guest_phoneno = booking.booking.guest_phoneno
    print "sendtripdetailsmsforuser"

    print guest_phoneno
    usertripsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+guest_phoneno+'&sender=RAPIDO&message=Hi+'+guest_name+',+In+Reference+with+your+Booking+no:'+bookingno+',+'+allocated_vehicle+'+('+vehicle_no+')+and+Chauffeur:'+chauffeur_name+'+('+chauffeur_phoneno+')+has+been+allocated+,+contact+driver+for+onward+Journey+&flash=0&unicode=0')
    print usertripsms
    print usertripsms.status_code

    print "message send aytu"
    if usertripsms.status_code == 200:
        try:
            print " try olagade bantu"
            dutyslip = Dutyslip.objects.get(pk=tripid)
            updated_by = request.user
            dutyslip_sms = Dutyslipsms.objects.get(dutyslip=dutyslip)
            dutyslip_sms.usersmssent = True
            dutyslip_sms.updated_by = updated_by
            dutyslip_sms.save()
        except Exception, e:
            created_by = request.user
            dutyslip = Dutyslip.objects.get(pk=tripid)
            dutyslip_sms = Dutyslipsms(created_by=created_by,dutyslip=dutyslip)
            dutyslip_sms.usersmssent = True
            dutyslip_sms.save()

    return HttpResponse(usertripsms)

def sendtripdetailsmsfordriver(request,tripid):

    print " tripdetailemail ge bantu"
    booking = Dutyslip.objects.get(pk=tripid)
    allocated_vehicle=booking.allocated_vehicle
    vehicle_no = booking.vehicle_no
    chauffeur_name = booking.chauffeur_name
    chauffeur_phoneno = booking.chauffeur_phoneno
    bookingno= "RTIPL-"+booking.booking.servicing_city.city_code+"-"+ booking.booking.booking_id
    guest_name = booking.booking.guest_name
    guest_phoneno = booking.booking.guest_phoneno

    address = booking.booking.pick_up_location
    address = urllib.quote_plus(address)

    #below is used for sms readable format querystring to percentage encoding like %26
    address =  urllib.quote(address, safe='')
    # this map url is used to send map link in sms and appending pickup address as argement 
    map = "https://www.google.com/maps/search/?api=1%26query="
    # we have made %26 in place of & since character encoding in sms is ASCII format
    mapaddress= str(map+address)
    pickuptime=booking.booking.pickup_date_time

    date = pickuptime.date()
    date = str(date)
    time = pickuptime.time()
    time = str(time)


    drivertripsms = requests.get('http://alerts.variforrm.in/api?method=sms.normal&api_key=be11a90d4253db04b38acd817998b56ba88a494b&to='+chauffeur_phoneno+'&sender=RAPIDO&message=Hi+'+chauffeur_name+',+your+Trip+no:+'+booking.booking.booking_id+'+Guest+name:'+guest_name+'+('+guest_phoneno+')+pickup+time:'+date+',+'+time+',+Location:+'+mapaddress+'+&flash=0&unicode=0')
    print drivertripsms

    if drivertripsms.status_code == 200:
        try:
            created_by = request.user
            dutyslip = Dutyslip.objects.get(pk=tripid)
            dutyslip_sms = Dutyslipsms.objects.get(dutyslip=dutyslip)
            dutyslip_sms.driversmssent = True
            dutyslip_sms.updated_by = created_by
            dutyslip_sms.save()
        except Exception, e:
            dutyslip = Dutyslip.objects.get(pk=tripid)
            dutyslip_sms = Dutyslipsms(created_by=created_by,dutyslip=dutyslip)
            dutyslip_sms.driversmssent = True
            dutyslip_sms.save()
    print " driver ge sms hoytu"

    return HttpResponse(drivertripsms)

def activatecompanyemail(request,cid):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    company = Company.objects.get(pk=cid)
    count=0
    company_airport_price = Company_airport_ratecard.objects.filter(company=company)
    company_outstation_price = Company_outstation_ratecard.objects.filter(company=company)
    company_cityusage_price = Company_city_ratecard.objects.filter(company=company)
    if company_airport_price is None:
        if company_outstation_price is None:
            if company_cityusage_price is None:
                count=1 
            end 
        end 

    if count==1:
        cat_list = Category.objects.all()
        city_list = City.objects.all()
        slab_list=Slab.objects.all()
        travelservice_type_list = Travelservicetype.objects.all()
        vehicle_model = Vehicle_varient.objects.all()
        context_dict['vehicle_model']=vehicle_model
        context_dict['cat_list'] = cat_list
        context_dict['city_list']= city_list
        context_dict['slab_list']=slab_list
        context_dict['travelservice_type_list']=travelservice_type_list
        context_dict['company']=company
        context_dict['message']="you have not set ratecard for this company set ratecard first "
        return render_to_response('rapido/master/company_detail.html',context,context_dict)
    else:
        company = Company.objects.get(pk=cid)
        context = {'company': company}
        html_content = render_to_string('rapido/activatecompanyemail.html', context=context).strip()
        subject = 'RapidoTravels: Client Activation'  
        to = ['manju24j@gmail.com','']
        # to = ['company.company_email ','company.company_manager_email']
        # from_email = 'manju24.rymec@gmail.com'
        # reply_to = ['manju24.rymec@gmail.com']
        from_email = 'bookings@rapidotravels.co.in'
        reply_to = ['bookings@rapidotravels.co.in']

        msg = EmailMultiAlternatives(subject, html_content, to=to, from_email=from_email, reply_to=reply_to)  
        msg.content_subtype = 'html'  # Main content is text/html  
        msg.mixed_subtype = 'related'  # This is critical, otherwise images will be displayed as attachments!
        # msg.send()
        company.status=True
        company.save()
        context_dict['message']="client is activated "

    cat_list = Category.objects.all()
    city_list = City.objects.all()
    slab_list=Slab.objects.all()
    travelservice_type_list = Travelservicetype.objects.all()
    vehicle_model = Vehicle_varient.objects.all()
    context_dict['vehicle_model']=vehicle_model
    context_dict['cat_list'] = cat_list
    context_dict['city_list']= city_list
    context_dict['slab_list']=slab_list
    context_dict['travelservice_type_list']=travelservice_type_list
    context_dict['company']=company
    context = RequestContext(request)
    return render_to_response('rapido/master/company_detail.html',context_dict,context)
    # return render_to_response('rapido/master/bookingemail.html',context)


def sendSimpleEmail(request,emailto):
   res = send_mail("hello Client", "Thank you for registering with us updates will get soon from rapido", "rapido@gmail.com", [emailto])
   return HttpResponse('%s'%res)

def sendEmail(request,message,emailto):
   res = send_mail("hello Client", message, "rapido@gmail.com", [emailto])
   return HttpResponse('%s'%res)

def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

#---------------- Page code------------------------------

def index(request):
    context = RequestContext(request)
    context_dict={}
    # email = EmailMessage('Subject', 'Body', to=['def@domain.com'])
    # email.send()

    return render_to_response('rapido/index.html', context_dict, context)

def user_login(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                	return HttpResponseRedirect('/rapido/master/')
                if user.is_staff:
                	return HttpResponseRedirect('/rapido/staff/')
                else:
                	return HttpResponseRedirect('/rapido/company/')

            else:
                return HttpResponse("Your rapido account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('rapido/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rapido/login/')


@login_required
def company(request):
    context = RequestContext(request)
    context_dict = {}
    companycount = Company.objects.all().count()
    bookings_count = Bookings.objects.all().count()
    dutyslip_count = Dutyslip.objects.all().count()
    ontrip = Dutyslip.objects.filter(status_id=2).count()
    return render_to_response('rapido/company/company.html',context)

@login_required
def matser(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    # total_bookings_tillnow = Bookings.objects.all().count()
    # total_pending_booking = Bookings.objects.filter(status_id=1).count()
    # total_pending_dispatch = Dutyslip.objects.filter(status_id=1).count()
    # total_ontrip = Dutyslip.objects.filter(status_id=2).count()
    # total_canceled = Bookings.objects.filter(status_id=6).count()
    # total_pendingtoclose = Dutyslip.objects.filter(status_id=3).count()
    # total_closed_trips = Dutyslip.objects.filter(status_id=4).count()
    # context_dict = { 'total_bookings_tillnow':total_bookings_tillnow,
    #                  'total_ontrip':total_ontrip,
    #                  'total_pendingtoclose':total_pendingtoclose,
    #                  'total_closed_trips':total_closed_trips,
    #                  'total_canceled':total_canceled,
    #                  'total_pending_booking':total_pending_booking,
    #                  'total_pending_dispatch':total_pending_dispatch }
    return render_to_response('rapido/master/master.html', context_dict, context)

def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__startswith=starts_with)
    else:
        cat_list = Category.objects.all()

    if max_results > 0:
        if (len(cat_list) > max_results):
            cat_list = cat_list[:max_results]

    for cat in cat_list:
        cat.url = encode_url(cat.name)
    
    return cat_list

@csrf_exempt
@login_required
def mastercategory(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    top_category_list = Category.objects.order_by('name')

    for category in top_category_list:
        category.url = encode_url(category.name)

    context_dict = {'categories': top_category_list}

    cat_list = Category.objects.all()
    context_dict['cat_list'] = cat_list

    vehicle_list = Vehicle.objects.order_by('category')
    context_dict['vehicle_list'] = vehicle_list

    return render_to_response('rapido/master/mastercategory.html',context_dict,context)


def category_details(request,category_name_url):
    # Request our context
    context = RequestContext(request)
    category_name = decode_url(category_name_url)
    context_dict = {}
    context_dict =totalcount(request)
    context_dict = {'category_name': category_name, 'category_name_url': category_name_url}
    try:
        # Find the category with the given name.
        category = Category.objects.get(name__iexact=category_name)
        context_dict['category'] = category
    except Category.DoesNotExist:
        # get here if the category does not exist.
        # Will trigger the template to display the 'no category' message.
        pass
    # Go render the response and return it to the client.
    return render_to_response('rapido/master/category_details.html', context_dict, context)


@csrf_exempt
@login_required
def add_category(request):
    # Get the context from the request.
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    
    # A HTTP POST?
    if request.method == 'POST':
        name = request.POST['name']
        if 'picture' in request.FILES:
            picture = request.FILES['picture']
        user= request.user
        cat=Category(name=name,picture=picture,created_by=user)
        cat.save()
            # Now call the index() view.
            # The user will be shown the homepage.
        return mastercategory(request)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    context_dict['form'] = form
    return render_to_response('rapido/master/add_category.html',context_dict,context)

def update_category(request,category_id):
    #Get the context from the request.
    context = RequestContext(request)    
    # A HTTP POST?
    context_dict={}
    if request.method == 'POST':
        name = request.POST['name']
        status = request.POST['status']
        cat=Category.objects.get(id=category_id)
        if 'picture' in request.FILES:
            picture = request.FILES['picture']
        else: picture=cat.picture.url
        cat.name=name
        if status == "True":
            cat.is_active=True
        else:
            cat.is_active=False
        cat.picture=picture
        cat.save()
        category = Category.objects.get(id=category_id)
        context_dict['category'] = category
        return render_to_response('rapido/master/category_details.html', context_dict, context)

    category = get_category_list()
    context_dict['category'] = cat_list
    return render_to_response('rapido/master/category_details.html', context_dict, context)


@login_required
@csrf_exempt
def vendor_master(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    vendor_list = Vendor.objects.all()
    context_dict['vendor_list']=vendor_list
    return render_to_response( 'rapido/master/vendor.html',context_dict,context)

@login_required
@csrf_exempt
def add_vendor_master(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    vendor_type_list= Vendortype.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    context_dict['vendor_type_list']= vendor_type_list
    if request.method == 'POST':
        vendor_type = request.POST['vendor_type']
        vendor_name = request.POST['vendor_name']
        vendor_phoneno = request.POST['vendor_phoneno']
        vendor_joined_date = request.POST['vendor_joined_date']
        vendor_payment_type = request.POST['vendor_payment_type']
        vendor_agreement_start_date = request.POST['vendor_agreement_start_date']
        vendor_agreement_end_date = request.POST['vendor_agreement_end_date']
        bank_name = request.POST['bank_name']
        beneficiary_account_name=request.POST['beneficiary_account_name']
        accountno = request.POST['accountno']
        vendor_email = request.POST['vendor_email']
        ifsc = request.POST['ifsc']

        user= request.user
        if 'vendor_documents' in request.FILES:
            vendor_documents  = request.FILES['vendor_documents']
        else:
            vendor_documents =""

        if 'vendor_picture' in request.FILES:
            vendor_picture = request.FILES['vendor_picture']
        else:
            vendor_picture = ""
        vendor_type = Vendortype.objects.get(id=vendor_type)

        street_address= request.POST['street_address']
        landmark = request.POST['landmark']
        area = request.POST['area']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        address=Location(created_by=user, street_address=street_address,landmark=landmark,area=area,city=city,state=state,pincode=pincode,country=country)
        address.save()

        vendor = Vendor(created_by=user, vendor_type=vendor_type,vendor_name=vendor_name,vendor_email=vendor_email,vendor_phoneno=vendor_phoneno,vendor_joined_date=vendor_joined_date,vendor_payment_type=vendor_payment_type,vendor_agreement_start_date=vendor_agreement_start_date,vendor_agreement_end_date=vendor_agreement_end_date,vendor_picture=vendor_picture,vendor_documents=vendor_documents,bank_name=bank_name,beneficiary_account_name=beneficiary_account_name,accountno=accountno,ifsc=ifsc)
        vendor.vendor_address=address
        vendor.save()
        context_dict['message']="new Vendor has been added "

    vendor_list = Vendor.objects.all()
    context_dict['vendor_list']=vendor_list
    return render_to_response( 'rapido/master/add_vendor.html',context_dict,context)

@login_required
@csrf_exempt
def vendor_details(request,vendor_id):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    vendor = Vendor.objects.get(id=vendor_id)
    chauffeur_vehicel_list = Chauffeur_vehicel.objects.filter(vendor= vendor)
    cat_list = Category.objects.all()
    city_list = City.objects.all()
    slab_list=Slab.objects.all()
    travelservice_type_list = Travelservicetype.objects.all()
    vehicle_model = Vehicle_varient.objects.all()
    context_dict['vehicle_model']=vehicle_model
    context_dict['cat_list'] = cat_list
    context_dict['city_list']= city_list
    context_dict['slab_list']=slab_list
    context_dict['travelservice_type_list']=travelservice_type_list

    context_dict['vendor']=vendor
    context_dict['chauffeur_vehicel_list']=chauffeur_vehicel_list
    return render_to_response( 'rapido/master/vendor_details.html',context_dict,context)

def update_vendor(request,vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    if request.method == 'POST':
        vendor_type = request.POST['vendor_type']
        vendor_name = request.POST['vendor_name']
        vendor_phoneno = request.POST['vendor_phoneno']
        vendor_joined_date = request.POST['vendor_joined_date']
        vendor_payment_type = request.POST['vendor_payment_type']
        vendor_agreement_start_date = request.POST['vendor_agreement_start_date']
        vendor_agreement_end_date = request.POST['vendor_agreement_end_date']
        bank_name = request.POST['bank_name']
        beneficiary_account_name=request.POST['beneficiary_account_name']
        accountno = request.POST['accountno']
        vendor_email = request.POST['vendor_email']
        ifsc = request.POST['ifsc']

        if 'vendor_picture' in request.FILES:
            vendor_picture = request.FILES['vendor_picture']
        else:
            vendor_picture = vendor.vendor_picture

        if 'vendor_documents' in request.FILES:
            vendor_documents  = request.FILES['vendor_documents']
        else:
            vendor_documents = vendor.vendor_documents
            

        street_address= request.POST['street_address']
        landmark = request.POST['landmark']
        area = request.POST['area']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']

        address = Location.objects.get(id=vendor.vendor_address_id)
        print address
        user= request.user
        address=Location(street_address=street_address,landmark=landmark,area=area,city=city,state=state,pincode=pincode,country=country,created_by=user)
        address.save()

        vendor = Vendor(vendor_type_id=vendor_type,vendor_name=vendor_name,vendor_email=vendor_email,vendor_phoneno=vendor_phoneno,vendor_joined_date=vendor_joined_date,vendor_payment_type=vendor_payment_type,vendor_agreement_start_date=vendor_agreement_start_date,vendor_agreement_end_date=vendor_agreement_end_date,vendor_picture=vendor_picture,vendor_documents=vendor_documents,bank_name=bank_name,beneficiary_account_name=beneficiary_account_name,accountno=accountno,ifsc=ifsc)
        vendor.vendor_address=address
        vendor.save()
    vendor = Vendor.objects.get(id=vendor_id)
    chauffeur_vehicel_list = Chauffeur_vehicel.objects.filter(vendor= vendor)
    context_dict['vendor']=vendor
    context_dict['chauffeur_vehicel_list']=chauffeur_vehicel_list
    return render_to_response( 'rapido/master/vendor_details.html',context_dict,context)

@login_required
@csrf_exempt
def vehicle_master(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    vendor_list = Vendor.objects.all()
    vehicle_model_list= Vehicle_varient.objects.all()
    context_dict['vendor_list']=vendor_list
    context_dict['cat_list'] = cat_list
    context_dict['vehicle_model_list']=vehicle_model_list
    vehicle_list = Vehicle.objects.all()
    context_dict['vehicle_list']=vehicle_list
    return render_to_response( 'rapido/master/vehicle.html',context_dict,context)



@login_required
@csrf_exempt
def add_vehicle_master(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    vendor_list = Vendor.objects.all()
    context_dict['vendor_list']=vendor_list
    context_dict['cat_list'] = cat_list
    vehicle_model_list= Vehicle_varient.objects.all()
    context_dict['vehicle_model_list']=vehicle_model_list

    if request.method == 'POST':
        category_id = request.POST['category']        
        vehicle_belongsto = request.POST['vehicle_belongsto']
        vehicle_model_name = request.POST['vehicle_model_name']
        vehicle_no = request.POST['vehicle_no']
        vehicle_ownername = request.POST['vehicle_ownername']
        vehicle_owner_phoneno = request.POST['vehicle_owner_phoneno']
        seat_capacity = request.POST['seat_capacity']
        insurance_expire_date = request.POST['insurance_expire_date']
        tax_expire_date = request.POST['tax_expire_date']
        vehicle_engine_no  = request.POST['engineno']
        vehicle_colour = request.POST['vehicle_colour']

        user = request.user

       # Retrieve the associated Category object so we can add it.
        cat = Category.objects.get(id=category_id)
        vendor= Vendor.objects.get(id=vehicle_belongsto)
        vehicle_model= Vehicle_varient.objects.get(id=vehicle_model_name)

        if 'vehicle_picture' in request.FILES:
            vehicle_picture = request.FILES['vehicle_picture']

        vehicle = Vehicle(created_by=user, vehicle_modelname=vehicle_model,vehicle_belongsto=vendor,vehicle_no=vehicle_no,vehicle_ownername=vehicle_ownername,vehicle_owner_phoneno=vehicle_owner_phoneno,seat_capacity=seat_capacity,tax_expire_date=tax_expire_date,insurance_expire_date=insurance_expire_date,vehicle_engine_no=vehicle_engine_no,vehicle_picture=vehicle_picture,vehicle_colour=vehicle_colour)
        vehicle.save()
        context_dict['message']="new vehicle has been added "

    vehicle_list = Vehicle.objects.all()
    context_dict['vehicle_list']=vehicle_list
    return render_to_response( 'rapido/master/add_vehicle.html',context_dict,context)

@login_required
@csrf_exempt
def chauffeur_master(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    vendor_list = Vendor.objects.all()
    context_dict['vendor_list']=vendor_list
    context_dict['cat_list'] = cat_list
    if request.method == 'POST':

        chauffeur_name = request.POST['chauffeur_name']
        chauffeur_type = request.POST['chauffeur_type']
        chauffeur_phoneno = request.POST['chauffeur_phoneno']

        chauffeur_drivinglicense = request.POST['chauffeur_drivinglicense']
        chauffeur_drivinglicense_expire_date = request.POST['chauffeur_drivinglicense_expire_date']
        chauffeur_badgeno = request.POST['chauffeur_badgeno']
        chauffeur_badge_expired_date = request.POST['chauffeur_badge_expired_date']
        
        #Retrieve the associated Category object so we can add it.
        if 'chauffeur_picture' in request.FILES:
            chauffeur_picture = request.FILES['chauffeur_picture']
        else:
            chauffeur_picture = ""
        user= request.user
        street_address= request.POST['street_address']
        landmark = request.POST['landmark']
        area = request.POST['area']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        address=Location(created_by=user,street_address=street_address,landmark=landmark,area=area,city=city,state=state,pincode=pincode,country=country)
        address.save()

        chauffeur_type = Vendor.objects.get(id=chauffeur_type)
        driver = Chauffeur(created_by=user, chauffeur_name=chauffeur_name,chauffeur_belongsto=chauffeur_type,chauffeur_phoneno=chauffeur_phoneno,chauffeur_drivinglicense=chauffeur_drivinglicense,chauffeur_drivinglicense_expire_date=chauffeur_drivinglicense_expire_date,chauffeur_badgeno=chauffeur_badgeno,chauffeur_badge_expired_date=chauffeur_badge_expired_date,chauffeur_picture=chauffeur_picture)
        driver.chauffeur_address=address
        driver.save()

    chauffeur_list = Chauffeur.objects.all()
    context_dict['chauffeur_list']=chauffeur_list

    return render_to_response( 'rapido/master/chauffeur.html',context_dict,context)

@login_required
@csrf_exempt
def company_client_master(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list

    company_client_list = Company.objects.all()
    context_dict['company_client_list']=company_client_list    
    return render_to_response( 'rapido/master/company.html',context_dict,context)

@login_required
@csrf_exempt
def add_company_client_master(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    company_type_list = Companytype.objects.all()
    context_dict['company_type_list']= company_type_list

    if request.method == 'POST':
        company_name = request.POST['company_name']
        company_type = request.POST['company_type']
        # company_website = request.POST['company_website']
        company_phoneno = request.POST['company_phoneno']
        company_email = request.POST['company_email']

        company_manager_name = request.POST['company_manager_name']
        company_manager_mobileno=request.POST['company_manager_mobileno']
        company_manager_email = request.POST['company_manager_email']
        company_payment_type = request.POST['company_payment_type']
        
        company_agreement_start_date = request.POST['company_agreement_start_date']
        company_agreement_end_date = request.POST['company_agreement_end_date']
        
        travelling_time_treshhold = request.POST['travelling_time_treshhold']
        gst= request.POST['gst']
        pan = request.POST['pan']

        if 'company_documents' in request.FILES:
            company_documents  = request.FILES['company_documents']
        else:
            company_documents =""

        if 'company_logo' in request.FILES:
            company_logo = request.FILES['company_logo']

        # cuser=User(username=company_name,email=company_email)
        # cuser.set_password("abc123")
        # cuser.save()

        user= request.user
        company_type= Companytype.objects.get(id=company_type)

        street_address= request.POST['street_address']
        landmark = request.POST['landmark']
        area = request.POST['area']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        address=Location(created_by=user, street_address=street_address,landmark=landmark,area=area,city=city,state=state,pincode=pincode,country=country)
        address.save()

        company = Company(created_by=user, company_name=company_name,company_type=company_type,company_phoneno=company_phoneno,company_email=company_email,company_manager_name=company_manager_name,company_manager_mobileno=company_manager_mobileno,company_manager_email=company_manager_email,company_payment_type=company_payment_type,company_agreement_start_date=company_agreement_start_date,company_agreement_end_date=company_agreement_end_date,travelling_time_treshhold=travelling_time_treshhold,company_logo=company_logo,company_documents=company_documents,gst=gst,pan=pan)
        cuser=User(username=company_name,email=company_email)
        cuser.set_password("abc123")
        cuser.save()

        company.user=cuser
        company.company_address=address
        company.save()
        context_dict['message']="new company has been added "

    company_client_list = Company.objects.all()
    context_dict['company_client_list']=company_client_list    
    return render_to_response( 'rapido/master/add_company.html',context_dict,context)


# @login_required
@csrf_exempt
def set_client_rate_card(request,client_id):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user= User.objects.get(id=client_id)
    company=Company.objects.get(user=user)
    try:
        if request.method == 'POST':
            service_type = request.POST['service_type']
            category = request.POST['category']
            category = Category.objects.get(id=category)
            if service_type == "Airport_Transfer":
                slab="Airport_Transfer"
                base_rate = request.POST['base_rate']
                rate_card = Company_client_rate_card(company_client=company,company_user=user,service_type=service_type,category=category,slab=slab,base_rate=base_rate,unit = "Rs")
                rate_card.save()

            if service_type == "Outstation":
                slab = "Outstation"
                base_rate= request.POST['base_rate']
                per_km_rate = request.POST['per_km_rate']
                batta = request.POST['batta']
                rate_card = Company_client_rate_card(company_client=company,company_user=user,service_type=service_type,category=category,slab=slab,base_rate=base_rate,unit="Km",per_km_rate=per_km_rate,batta=batta)
                rate_card.save()

            if service_type == "City_Usage":
                slab = request.POST['slab']
                base_rate =request.POST['base_rate']
                per_km_rate = request.POST['extrakm']
                per_hr_rate = request.POST['extrahrs']
                rate_card = Company_client_rate_card(company_client=company,company_user=user,service_type=service_type,category=category,slab=slab,base_rate=base_rate, per_km_rate=per_km_rate,per_hr_rate=per_hr_rate)
                rate_card.save()

        company_rate_card_list = Company_client_rate_card.objects.filter(company_user=user)
        context_dict['company_rate_card_list']=company_rate_card_list   
        context_dict['company']=company
        return render_to_response('rapido/master/company_client_rate_card.html',context_dict,context)
    except Exception, e:
        message="this category price is already set"
        # company_rate_card_list = Company_client_rate_card.objects.filter(company_user=user)
        # context_dict['company_rate_card_list']=company_rate_card_list   
        context_dict['company']=company
        context_dict['message']=message

    return render_to_response('rapido/master/company_client_rate_card.html',context_dict,context)


@login_required
@csrf_exempt
def admin_companydetail(request,company_id):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    cat_list = Category.objects.all()
    city_list = City.objects.all()
    slab_list=Slab.objects.all()
    travelservice_type_list = Travelservicetype.objects.all()
    vehicle_model = Vehicle_varient.objects.all()
    context_dict['vehicle_model']=vehicle_model
    context_dict['cat_list'] = cat_list
    context_dict['city_list']= city_list
    context_dict['slab_list']=slab_list
    context_dict['travelservice_type_list']=travelservice_type_list
    company=Company.objects.get(id=company_id)
    context_dict['company']=company
    return render_to_response('rapido/master/company_detail.html',context_dict,context)

# Client company Bookings

@login_required
@csrf_exempt
def company_view_ratecard(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    city_list = City.objects.all()
    slab_list=Slab.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['city_list']= city_list
    context_dict['slab_list']=slab_list
    user = request.user
    company=Company.objects.get(user=user)
    company_rate_card_list = Company_airport_ratecard.objects.filter(company=company)
    context_dict['company_rate_card_list']=company_rate_card_list   
    context_dict['company']=company
    return render_to_response('rapido/company/company_view_ratecard.html',context_dict,context)


@login_required
@csrf_exempt
def company_bookcab(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['service_place']=service_place
    user = request.user
    company=Company.objects.get(user=user)
    if request.method == "POST":
    	service_type = request.POST["service_type"]
    	category = request.POST["category"]
    	booking_from = request.POST["booking_from"]
    	booking_phoneno = request.POST["booking_phoneno"]
    	booking_email = request.POST["booking_email"]
    	guest_name = request.POST["guest_name"]
        guest_gender = request.POST["gender"]
    	guest_phoneno = request.POST["guest_phoneno"]
    	guest_email = request.POST["guest_email"]
    	pickup_date_time = request.POST["pick_up_date"]
        pickup_address= request.POST["pickup_address"]
        drop_address = request.POST["drop_address"]

        category = Category.objects.get(id=category)

        requested_vehicle_model = request.POST["requested_vehicle_model"]
        billing_base = request.POST["billing_base"]
        comment = request.POST["comment"]
        city = request.POST["city"]
        add_booking = Bookings(company=company, booking_from=booking_from,booking_email=booking_email,booking_phoneno=booking_phoneno,guest_name=guest_name,guest_gender=guest_gender,guest_email=guest_email,guest_phoneno=guest_phoneno,pickup_date_time=pickup_date_time,service_type_id=service_type,category=category,requested_vehicle_model=requested_vehicle_model,billing_base_id=billing_base,comment=comment,pick_up_location=pickup_address,drop_location=drop_address,created_by=user,status_id=1,servicing_city_id=city)
        add_booking.save()
        context_dict['message']="booking has been done and mail sent to registered company id"
        # sending mail
        # subject, from_email, to = 'hello Client', 'rapido@gmail.com', add_booking.guest_email
        # text_content = 'Thank you for Booking A trip .'
        # html_content = '<p>Your Booking ID is <strong>'+add_booking.booking_id+'</strong><br>booked category:' +add_booking.category.name+"<br>Guest name:"+add_booking.guest_name+ "<br> Phone no" +add_booking.guest_phoneno+ "<br> pick up date and time:"+add_booking.pick_up_date+"&"+ add_booking.pick_up_time+'<br> you will reveive updates Once vehicle is allocated you thank you</p>'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()

        # message="<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Rapido Travels</title></head><body><div id="header"><h1>Rapido Travels</h1></div>Thank you for Booking , your Booking Id is:{{add_booking.booking_id}}<br>Guest name:{{add_booking.guest_name}}<br> Guest Phnone no:{{add_booking.guest_phoneno}}<br> pick_up_date:{{add_booking.pick_up_date}} & pick_up_time: {{add_booking.pick_up_time}} </body></html>"
        # msg="thanking for booking your trip and Your Booking Id is" +add_booking.booking_id+ " <br>" "booked category:" +add_booking.category.name+"<br>Guest name:"+add_booking.guest_name+ "<br> Phone no" +add_booking.guest_phoneno+ "<br> pick up date and time:"+add_booking.pick_up_date+"&"+ add_booking.pick_up_time+""
        
        # print message
        # res=sendEmail(request,message,add_booking.guest_email)
        # print " email Response"
        # print msg
    context_dict['company']=company
    return render_to_response('rapido/company/company_book_cab.html',context_dict,context)


@login_required
def company_viewbooking_detail(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    cat_list = Category.objects.all()
    context_dict = {}
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['service_place']=service_place
    context_dict['booking']= booking
    return render_to_response('rapido/company/viewbooking_detail.html',context_dict,context)


@login_required
@csrf_exempt
def invoice_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    company=Company.objects.get(user=user)
    booking_list= Bookings.objects.filter(company=company,status=5)
    # dutyslip_list= Dutyslip.objects.filter(booking.company=company,status_id=4)

    context_dict['booking_list'] = booking_list
    # context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/company/invoice_list.html',context_dict,context)



@login_required
@csrf_exempt
def booking_history(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    print user
    company =Company.objects.get(user = user)
    booking_list= Bookings.objects.filter(company = company)

    print booking_list

    context_dict['booking_list'] = booking_list
    # context_dict['company_rate_card_list']=company_rate_card_list   
    context_dict['company']=company
    return render_to_response('rapido/company/booking_history.html',context_dict,context)


@login_required
@csrf_exempt
def view_invoice(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    return render_to_response('rapido/staff/view_invoice.html',context_dict,context)

#----------------- STAFF -----------------------

@login_required
def staff(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    # total_bookings_tillnow = Bookings.objects.all().count()
    # total_pending_booking = Bookings.objects.filter(status_id=1).count()
    # total_pending_dispatch = Dutyslip.objects.filter(status_id=1).count()
    # total_ontrip = Dutyslip.objects.filter(status_id=2).count()
    # total_canceled = Bookings.objects.filter(status_id=6).count()
    # total_pendingtoclose = Dutyslip.objects.filter(status_id=3).count()
    # total_closed_trips = Dutyslip.objects.filter(status_id=4).count()
    # context_dict = { 'total_bookings_tillnow':total_bookings_tillnow,
    #                  'total_ontrip':total_ontrip,
    #                  'total_pendingtoclose':total_pendingtoclose,
    #                  'total_closed_trips':total_closed_trips,
    #                  'total_canceled':total_canceled,
    #                  'total_pending_booking':total_pending_booking,
    #                  'total_pending_dispatch':total_pending_dispatch }
    return render_to_response('rapido/staff/staff.html', context_dict, context)

@csrf_exempt
def create_booking(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['company_list']= company_list
    user = request.user
    
    if request.method == "POST":
        company=request.POST["company"]
        service_type = request.POST["service_type"]
        category = request.POST["category"]
        booking_from = request.POST["booking_from"]
        booking_phoneno = request.POST["booking_phoneno"]
        booking_email = request.POST["booking_email"]
        guest_name = request.POST["guest_name"]
        guest_phoneno = request.POST["guest_phoneno"]
        guest_email = request.POST["guest_email"]
        pick_up_date = request.POST["pick_up_date"]
        pick_up_time = request.POST["pick_up_time"]
        pickup_address= request.POST["pickup_address"]
        drop_address = request.POST["drop_address"]

        category = Category.objects.get(id=category)
        company= Company.objects.get(id=company)
        requested_vehicle_model = request.POST["requested_vehicle_model"]
        billing_base = request.POST["billing_base"]
        comment = request.POST["comment"]
        add_booking = Bookings(booking_from=booking_from,booking_email=booking_email,booking_phoneno=booking_phoneno,guest_name=guest_name,guest_email=guest_email,guest_phoneno=guest_phoneno,pick_up_date=pick_up_date,pick_up_time=pick_up_time,service_type=service_type,category=category,requested_vehicle_model=requested_vehicle_model,billing_base=billing_base,comment=comment,pick_up_location=pickup_address,drop_location=drop_address,user=user,status="pending")
        add_booking.save()
        # sending mail
        subject, from_email, to = 'hello Client', 'rapido@gmail.com', add_booking.guest_email
        text_content = 'Thank you for Booking A trip .'
        html_content = '<p>Your Booking ID is <strong>'+add_booking.booking_id+'</strong><br>booked category:' +add_booking.category.name+"<br>Guest name:"+add_booking.guest_name+ "<br> Phone no" +add_booking.guest_phoneno+ "<br> pick up date and time:"+add_booking.pick_up_date+"&"+ add_booking.pick_up_time+'<br> you will reveive updates Once vehicle is allocated you thank you</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        context_dict['message']="booking has been done and mail sent to client/user"
    return render_to_response('rapido/staff/create_booking.html',context_dict,context)

@login_required
@csrf_exempt
def booking_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    booking_list= Bookings.objects.filter(status="pending")

    context_dict['booking_list'] = booking_list

    return render_to_response('rapido/staff/booking_list.html',context_dict,context)

#=============== Admin activites Start ================


@csrf_exempt
def admin_createbooking(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place
    
    if request.method == "POST":
        company=request.POST["company"]
        service_type = request.POST["service_type"]
        category = request.POST["category"]
        booking_from = request.POST["booking_from"]
        booking_phoneno = request.POST["booking_phoneno"]
        booking_email = request.POST["booking_email"]
        guest_name = request.POST["guest_name"]
        guest_phoneno = request.POST["guest_phoneno"]
        guest_email = request.POST["guest_email"]
        guest_gender = request.POST["gender"]
        pickup_date_time = request.POST["pick_up_date"]
        pickup_address= request.POST["pickup_address"]
        drop_address = request.POST["drop_address"]

        service_type=Servicetype.objects.get(id=service_type)
        category = Category.objects.get(id=category)
        company= Company.objects.get(id=company)
        user = User.objects.get(id=company.user_id)
        requested_vehicle_model = request.POST["requested_vehicle_model"]
        billing_base = request.POST["billing_base"]
        comment = request.POST["comment"]
        city = request.POST["city"]
        billing_base = Billingbase.objects.get(id=billing_base)
        add_booking = Bookings(company=company ,booking_from=booking_from,booking_email=booking_email,booking_phoneno=booking_phoneno,guest_name=guest_name,guest_email=guest_email,guest_phoneno=guest_phoneno,guest_gender=guest_gender, pickup_date_time=pickup_date_time,service_type=service_type,category=category,requested_vehicle_model=requested_vehicle_model,billing_base=billing_base,comment=comment,pick_up_location=pickup_address,drop_location=drop_address,created_by=user,status_id=1,servicing_city_id=city)
        add_booking.save()
        # # sending mail
        # subject, from_email, to = 'hello Client', 'rapido@gmail.com', add_booking.guest_email
        # text_content = 'Thank you for Booking A trip .'
        # html_content = '<p>Your Booking ID is <strong>'+add_booking.booking_id+'</strong><br>booked category:' +add_booking.category.name+"<br>Guest name:"+add_booking.guest_name+ "<br> Phone no" +add_booking.guest_phoneno+ "<br> pick up date and time:"+add_booking.pick_up_date+"&"+ add_booking.pick_up_time+'<br> you will reveive updates Once vehicle is allocated you thank you</p>'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()
        context_dict['message']="booking has been done and mail sent to client/user"

    return render_to_response('rapido/master/create_booking.html',context_dict,context)


@csrf_exempt
def admin_create_booking_others(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place
 
    return render_to_response('rapido/master/create_booking_others.html',context_dict,context)


@login_required
@csrf_exempt
def admin_booking_list(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)

    booking_list= (Bookings.objects.filter(status=2)|Bookings.objects.filter(status=1)).order_by("pickup_date_time")

    context_dict['booking_list'] = booking_list

    return render_to_response('rapido/master/booking.html',context_dict,context)

@login_required
@csrf_exempt
def admin_todaysbooking_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    today = date.today()
    print today
    booking_list= Bookings.objects.filter( pickup_date_time__contains=today,status=1).order_by("pickup_date_time")
    context_dict['booking_list'] = booking_list

    return render_to_response('rapido/master/todaysbooking.html',context_dict,context)


@login_required
def admin_viewbooking_detail(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    cat_list = Category.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['service_place']=service_place
    context_dict['booking']= booking
    return render_to_response('rapido/master/viewbooking_detail.html',context_dict,context)


@csrf_exempt
def admin_view_all_booking(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    booking_list= Bookings.objects.all().order_by('-created_date')
    # booking_list= Bookings.objects.filter(pickup_date_time__range=[fromdate, todate])

    context_dict['booking_list'] = booking_list
    return render_to_response('rapido/master/view_allbooking.html',context_dict,context)

@csrf_exempt
def admin_viewbookingdatewise(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    user = request.user
    # booking_list= Bookings.objects.all().order_by('-created_date')
    # booking_list= Bookings.objects.filter(pickup_date_time__range=[fromdate, todate])
    booking_list= Bookings.objects.filter(pickup_date_time__contains=fromdate)

    context_dict['booking_list'] = booking_list
    context_dict['fromdate'] = fromdate
    context_dict['todate'] = todate
    return render_to_response('rapido/master/view_allbooking.html',context_dict,context)


@login_required
def admin_assigncab(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    chauffeur= Chauffeur.objects.all()
    vehicle = Vehicle.objects.all()
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor_list'] = vendor_list
    return render_to_response('rapido/master/admin_assigncab.html',context_dict,context)


@login_required
def admin_viewdutyslip_detail(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor'] = vendor_list
    return render_to_response('rapido/master/viewdutyslip_detail.html',context_dict,context)


@login_required
@csrf_exempt
def admin_dutyslip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    # booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status=1)
    # context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/master/dutyslip_list.html',context_dict,context)

@login_required
@csrf_exempt
def admin_dutyslip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    # booking_list= Bookings.objects.filter(pickup_date_time__contains=fromdate,status=2)
    dutyslip_list= Dutyslip.objects.filter(booking__in=Bookings.objects.filter(pickup_date_time__contains=fromdate),status=1)
    # context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate

    return render_to_response('rapido/master/dutyslip_list.html',context_dict,context)

@login_required
@csrf_exempt
def admin_ontrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    dutyslip_list= Dutyslip.objects.filter(status=2)

    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/master/ontrip_list.html',context_dict,context)

@login_required
@csrf_exempt
def admin_ontrip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    dutyslip_list= Dutyslip.objects.filter(booking__in=Bookings.objects.filter(pickup_date_time__contains=fromdate),status=2)

    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate

    return render_to_response('rapido/master/ontrip_list.html',context_dict,context)


@login_required
@csrf_exempt
def admin_alltrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    # dutyslip_list= Dutyslip.objects.filter(created_date__range=[fromdate, todate])
    dutyslip_list= Dutyslip.objects.all()
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate

    return render_to_response('rapido/master/alltrip_list.html',context_dict,context)

@login_required
@csrf_exempt
def admin_alltriplist(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    dutyslip_list= Dutyslip.objects.filter(created_date__range=[fromdate, todate])
    # dutyslip_list= Dutyslip.objects.all()
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate
    context_dict['todate'] = todate

    return render_to_response('rapido/master/alltrip_list.html',context_dict,context)

@login_required
def admin_createdutyslip(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    user= request.user
    booking= Bookings.objects.get(booking_id=bookingno)
    booking.status_id=2
    booking.save()
    print "booking status change aytu"

    booking=Bookings.objects.get(booking_id=bookingno)
    chauffeur= Chauffeur.objects.all()
    vehicle = Vehicle.objects.all()
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor'] = vendor_list
    return render_to_response('rapido/master/admin_assigncab.html',context_dict,context)

@login_required
def admin_dutyslip(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    dutyslip=Dutyslip.objects.get(booking=booking)
    chauffeur= Chauffeur.objects.all()
    vehicle = Vehicle.objects.all()
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor'] = vendor_list
    context_dict['dutyslip']= dutyslip
    return render_to_response('rapido/master/dutyslip.html',context_dict,context)

@login_required
def admin_dispatch_vehicle(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    booking.status_id=3
    booking.save()
    dutyslip=Dutyslip.objects.get(booking=booking)
    dutyslip.status_id=2
    dutyslip.save()
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip
    print booking.status
    print dutyslip.status
    return render_to_response('rapido/master/dutyslip.html',context_dict,context)


@login_required
@csrf_exempt
def admin_closetrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status=3)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/master/closetrip_list.html',context_dict,context)

@login_required
@csrf_exempt
def admin_closetrip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(created_date__contains=fromdate,status=3)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate']= fromdate

    return render_to_response('rapido/master/closetrip_list.html',context_dict,context)


@login_required
def admin_closetrip(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    dutyslip=Dutyslip.objects.get(booking=booking)
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip

    return render_to_response('rapido/master/close_trip.html',context_dict,context)


@login_required
def admin_receivetrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status=2)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/master/receivetrip_list.html',context_dict,context)

@login_required
def admin_receivetrip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(created_date__contains=fromdate,status=2)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate

    return render_to_response('rapido/master/receivetrip_list.html',context_dict,context)

@login_required
def receive_tripsheet(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    booking.status_id=4
    booking.save()
    dutyslip=Dutyslip.objects.get(booking=booking)
    dutyslip.status_id=3
    dutyslip.save()
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip

    data= {'message':"status changed"}
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type="application/json")


@login_required
def admin_close_tripsheet(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    booking=Bookings.objects.get(booking_id=bookingno)
    booking.status_id=5
    booking.save()
    print "booking_id"
    print booking.status
    dutyslip=Dutyslip.objects.get(booking=booking)
    dutyslip.status_id=4
    dutyslip.save()
    print dutyslip.status
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip

    return admin_closetrip_list(request)


@login_required
@csrf_exempt
def admin_invoice_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status_id=4)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/master/admin_invoice_list.html',context_dict,context)


@login_required
def admin_invoice(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    dutyslip=Dutyslip.objects.get(booking=booking)
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip
    return render_to_response('rapido/master/invoice.html',context_dict,context)

@login_required
def company_invoice(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    booking=Bookings.objects.get(booking_id=bookingno)
    dutyslip=Dutyslip.objects.get(booking=booking)
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip
    return render_to_response('rapido/company/invoice.html',context_dict,context)


@login_required
@csrf_exempt
def standard_ratecard(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    cat_list = Category.objects.all()
    city_list = City.objects.all()
    travelservice_type_list = Travelservicetype.objects.all()
    slab_list = Slab.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['city_list']= city_list
    vehicle_model = Vehicle_varient.objects.all()
    context_dict['slab_list']= slab_list
    context_dict['vehicle_model']= vehicle_model
    context_dict['travelservice_type_list']= travelservice_type_list   

    return render_to_response( 'rapido/master/standard_ratecard.html',context_dict,context)


@login_required
@csrf_exempt
def admin_completedtrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status_id=4)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/master/admin_completedtrip_list.html',context_dict,context)


@login_required
def admin_calculate_invoice(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    print "calculate_invoice"
    print bookingno
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    dutyslip=Dutyslip.objects.get(booking=booking)
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip

    return render_to_response('rapido/master/calculate_invoice.html',context_dict,context)
#=============== Admin activites close ================

@csrf_exempt
def all_booking_list(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    # booking_list= Bookings.objects.all().order_by('-date')
    booking_list= Bookings.objects.filter(pickup_date_time__range=[fromdate, todate])
    context_dict['booking_list'] = booking_list
    context_dict['fromdate'] = fromdate
    context_dict['todate'] = todate

    return render_to_response('rapido/staff/all_booking_list.html',context_dict,context)



@login_required
def assign_cab(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    chauffeur= Chauffeur.objects.all()
    vehicle = Vehicle.objects.all()
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor'] = vendor_list
    return render_to_response('rapido/staff/assign_cab.html',context_dict,context)


@login_required
def create_dutyslip(request,bookingno):
	user= request.user
	if request.method == "POST":
		vendor = request.POST['vendor']
		allocated_vehicle= request.POST['allocated_vehicle']
		vehicle_colour = request.POST['vehicle_colour']
		vehicle_no = request . POST ['vehicle_no']
		chauffeur_name = request.POST['chauffeur_name']
		chauffeur_phoneno = request.POST['chauffeur_phoneno']
		chauffeur_drivinglicense = request.POST['chauffeur_drivinglicense']
		vendor = Vendor.objects.get(id=vendor)
		category = request.POST['category']
		category = Category.objects.get(id=category)
		bookingno= Bookings.objects.get(booking_id=bookingno)
		create_dutyslip= Dutyslip(dutyslip_createdby=user,category=category,vendor=vendor, allocated_vehicle=allocated_vehicle,vehicle_colour=vehicle_colour,vehicle_no=vehicle_no,chauffeur_name=chauffeur_name,chauffeur_phoneno=chauffeur_phoneno,chauffeur_drivinglicense=chauffeur_drivinglicense)
		create_dutyslip.booking=bookingno
		create_dutyslip.status="pending"
		create_dutyslip.save()
		bookingno.status="vehicle_allocated"
		bookingno.save()
		pick_up_date = bookingno.pick_up_date.strftime('%Y-%m-%d')
		pick_up_time = bookingno.pick_up_time.strftime('%I-%m-%p')
        subject, from_email, to = 'hello Client', 'rapido@gmail.com', bookingno.guest_email
        text_content = 'Thank you for Booking A trip .'
        html_content = '<p>Your Booking ID is <strong>'+bookingno.booking_id+'</strong><br>booked category:' +bookingno.category.name+"<br>Guest name:"+bookingno.guest_name+ "<br> Phone no" +bookingno.guest_phoneno+"<br> pick up date and time:"+pick_up_date+"&"+pick_up_time+'<br> <br>your booking Confirmed and assigned:<br>' +create_dutyslip.vehicle_colour+ " colour " +create_dutyslip.allocated_vehicle+ " and Vehicle No: "+ create_dutyslip.vehicle_no+ '<br> Driver Name:'+create_dutyslip.chauffeur_name+'<br>Phone Number:'+create_dutyslip.chauffeur_phoneno+' <br> vehicle will be on time as your Time <br> Happy Journey</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        # msg.send()
        return HttpResponse("booking Confimed")

	return HttpResponse("Dutyslip Failed to create")



@login_required
@csrf_exempt
def dutyslip_pending(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    dutyslip_list = Dutyslip.objects.filter(status="pending")
    context_dict['dutyslip_list']=dutyslip_list
    return render_to_response('rapido/staff/dutyslip_pending.html',context_dict,context)

@login_required
@csrf_exempt
def dispatch_vehicle(request,dutyslip_no):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    if request.method == "POST":
        dutyslip = Dutyslip.objects.get(dutyslip_id=dutyslip_no)
        dutyslip.status="vehicle_dispatch"
        dutyslip.save()
        bookingno=dutyslip.booking.booking_id
        print bookingno
        bookingno= Bookings.objects.get(booking_id=bookingno)
        bookingno.status="vehicle dispatched"
        bookingno.save()
        return HttpResponse("Trip sheet generated and Vehicle dispatched")
    dutyslip = Dutyslip.objects.get(dutyslip_id=dutyslip_no)
    context_dict['dutyslip']=dutyslip
    return render_to_response('rapido/staff/dispatch_vehicle.html',context_dict,context)


@login_required
@csrf_exempt
def dispatched_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    dutyslip_list = Dutyslip.objects.filter(status="vehicle_dispatch")
    context_dict['dutyslip_list']=dutyslip_list
    return render_to_response('rapido/staff/dispatched_list.html',context_dict,context)


@login_required
@csrf_exempt
def generate_invoice(request,dutyslip_no):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    user = request.user
    dutyslip = Dutyslip.objects.get(dutyslip_id=dutyslip_no)
    context_dict['dutyslip']=dutyslip
    if request.method == "POST":
        date_out= request.POST['date_out']
        date_in = request.POST['date_in']
        print date_out
        d2= datetime.datetime.strptime(u'date_in', '%Y-%m-%d')
        d1 = datetime.datetime.strptime(u'date_out', '%Y-%m-%d')
        opening_time = request.POST['opening_time']
        closing_time = request.POST['closing_time']
        # total_hrs = request.POST['total_hrs']

        # opening_km = request.POST['opening_km']
        # closing_km = request.POST['closing_km']
        # total_kms = closing_km - opening_km

        point_opening_km = request.POST['point_opening_km']
        point_closing_km = request.POST['point_closing_km']
 
        total_point_kms = int(point_closing_km) - int(point_opening_km)

        print total_point_kms
        # point_opening_hrs = request.POST['point_opening_hrs']
        # point_closing_hrs = request.POST['point_closing_hrs']
        # total_point_hrs = request.POST['total_point_hrs']

        parking = request.POST['parking']
        Itinerary = request.POST['Itinerary']
        miscellaneous = request.POST['miscellaneous']

        print "parking"
        print parking

        extra_hr = 0
        extra_km = 0

        package_rate =0
        extra_km_rate =0
        extra_hr_rate =0

        gst_tax=0
        discount=0
        total_amount=0




        dutyslip = Dutyslip.objects.get(dutyslip_id=dutyslip_no)
        dutyslip.status="trip_completed"
        dutyslip.save()
        bookingno=dutyslip.booking.booking_id
        bookingno= Bookings.objects.get(booking_id=bookingno)
        bookingno.status="trip_completed"
        bookingno.save()
        return render_to_response('rapido/staff/generate_invoice.html',context_dict,context)
    dutyslip = Dutyslip.objects.get(dutyslip_id=dutyslip_no)
    context_dict['dutyslip']=dutyslip
    return render_to_response('rapido/staff/generate_invoice.html',context_dict,context)


def completed_trip(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    user = request.user
    dutyslip_list = Dutyslip.objects.filter(status="trip_completed")
    context_dict['dutyslip_list']=dutyslip_list
    return render_to_response('rapido/staff/completed_trip.html',context_dict,context)

def set_airportprice(request):
    context = RequestContext(request)
    context_dict = {}
    objs = json.dumps({ "created_by": 1,"city": 1,"ratecard": [
        {
            "base_rate": 800,
            "category": 1,
            "service_type": 1,
            "vehicle_varient": [
                1,
                2,
                3
            ]
        },
        {
            "base_rate": 900,
            "category": 2,
            "service_type": 1,
            "vehicle_varient": [
                1,
                2,
                5
            ]
        },
        {
            "base_rate": 950,
            "category": 3,
            "service_type": 1,
            "vehicle_varient": [
                3,
                4,
                5
            ]
        },
        {
            "base_rate": 150,
            "category": 4,
            "service_type": 1,
            "vehicle_varient": [
                1,
                2,
                3
            ]
        },
        {
            "base_rate": 1500,
            "category": 5,
            "service_type": 1,
            "vehicle_varient": [
                2,
                3
            ]
        }
        ]  })
    objs = json.loads(objs)

    created_by_id = int(objs['created_by'])
    city_id = int(objs['city'])

    created_by = User.objects.get(id=created_by_id)
    city = City.objects.get(id=city_id)

    # Iterate through the stuff in the list

    for obj in objs['ratecard']:
        try:
            airportprice = Airport_ratecard.objects.get(city=city,category_id=obj['category'])
        except Exception, e:
            print objs['ratecard'][0]['vehicle_varient'][0]
            # Do something Django  with o's name and message, like
            airportprice = Airport_ratecard(created_by=created_by,city=city,category_id=int(obj['category']),service_type_id=int(obj['service_type']),base_rate=int(obj['base_rate']))
            airportprice.save()
            # for k in obj['vehicle_varient']:
            #     vehicle_type=Airport_ratecard_vehicle_varient(airport_ratecard=airportprice,vehicle_varient_id=int(k))
            #     vendor_type.save()
        # Now that the page is saved, display the category instead.

    return HttpResponse(json.dumps(success), content_type='application/json')

    
    if request.method == 'POST':

        data= {'sup':trans.sup.username,'cus':trans.cus.username,'orderno':trans.orderno,'total':trans.total}
        json_data = json.dumps(data)

    return HttpResponse(json_data, content_type="application/json")


# @api_view(['GET', 'POST'])
# def Airport_ratecard_list(request):
#     if request.method == 'GET':
#         queryset = Airport_ratecard.objects.all()
#         print queryset
#         serializer = Airport_ratecardSerializer(queryset, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = Airport_ratecardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def Airport_ratecard(request):
    objs = json.dumps([{
        "base_rate": 1200.0,
        "created_by": 1,
        "city": 3,
        "category": 1,
        "service_type": 2,
        "vehicle_varient": [
            2,
            5
        ]},
    {
        "base_rate": 1400.0,
        "created_by": 1,
        "city": 3,
        "category": 2,
        "service_type": 2,
        "vehicle_varient": [
            1,
            2
        ]},
    {
        "base_rate": 1750.0,
        "created_by": 1,
        "city": 3,
        "category": 4,
        "service_type": 2,
        "vehicle_varient": [
            3,
            4
        ]}  ])
    objs = json.loads(objs)
    for o in objs:
        print int(o['city'])
        try:
            airportprice = Airport_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']))
            print airportprice
        except Exception, e:
            serializer = Airport_ratecardSerializer(data=o)
            if serializer.is_valid():
                print int(o['base_rate'])
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse("json.dumps(success), content_type='application/json'")



@api_view(['GET','POST'])
def Outstation_ratecard(request):
    objs = json.dumps([{
        "base_rate": 1200.0,
        "created_by": 1,
        "city": 3,
        "category": 1,
        "service_type": 2,
        "vehicle_varient": [
            2,
            5
        ]},
    {
        "base_rate": 1200.0,
        "created_by": 1,
        "city": 3,
        "category": 2,
        "service_type": 2,
        "vehicle_varient": [
            1,
            2
        ]} ])
    objs = json.loads(objs)
    for o in objs:
        print int(o['city'])
        try:
            airportprice = Airport_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']))
        except Exception, e:
            serializer = Outstation_ratecardSerializer(data=o)
            if serializer.is_valid():
                print int(o['base_rate'])
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse("json.dumps(success), content_type='application/json'")

@api_view(['GET','POST'])
def City_ratecard(request):
    objs = json.dumps([{
        "base_rate": 1200.0,
        "created_by": 1,
        "city": 3,
        "category": 1,
        "service_type": 2,
        "vehicle_varient": [
            2,
            5
        ]},
    {
        "base_rate": 1200.0,
        "created_by": 1,
        "city": 3,
        "category": 2,
        "service_type": 2,
        "vehicle_varient": [
            1,
            2
        ]} ])
    objs = json.loads(objs)
    for o in objs:
        print int(o['city'])
        try:
            airportprice = City_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']))
        except Exception, e:
            serializer = City_ratecardSerializer(data=o)
            if serializer.is_valid():
                print int(o['base_rate'])
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse("json.dumps(success), content_type='application/json'")

@login_required
@csrf_exempt
def invoice_print(request,invoice_no):
    context = RequestContext(request)
    booking= Bookings.objects.get(booking_id=invoice_no)
    context_dict = {}
    context_dict =totalcount(request)
    dutyslip = Dutyslip.objects.get(booking=booking)

    context_dict['dutyslip']=dutyslip
    context_dict['booking']=booking
    return render_to_response('rapido/invoice_print.html',context_dict,context)


#============= staff activity ==========================

@login_required
@csrf_exempt
def staff_booking_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    booking_list= (Bookings.objects.filter(status=1)|Bookings.objects.filter(status=2)).order_by("pickup_date_time")

    context_dict['booking_list'] = booking_list

    return render_to_response('rapido/staff/booking.html',context_dict,context)

@login_required
@csrf_exempt
def staff_todaysbooking_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    today = date.today()
    # booking_list= (Bookings.objects.filter( pickup_date_time__contains=today,status=1)|Bookings.objects.filter( pickup_date_time__contains=today,status=2)).order_by("pickup_date_time")
    booking_list= (Bookings.objects.filter( pickup_date_time__contains=today,status=1)|Bookings.objects.filter( pickup_date_time__contains=today,status=2)).order_by("pickup_date_time")
    context_dict['booking_list'] = booking_list

    return render_to_response('rapido/staff/booking.html',context_dict,context)



@login_required
def staff_viewbooking_detail(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    cat_list = Category.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['service_place']=service_place
    context_dict['booking']= booking
    return render_to_response('rapido/staff/viewbooking_detail.html',context_dict,context)

@csrf_exempt
def staff_view_all_booking(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    booking_list= Bookings.objects.all().order_by('-created_date')


    context_dict['booking_list'] = booking_list
    return render_to_response('rapido/staff/view_allbooking.html',context_dict,context)


@csrf_exempt
def staff_viewallbooking(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    user = request.user
    # booking_list= Bookings.objects.all().order_by('-created_date')
    booking_list= Bookings.objects.filter(pickup_date_time__range=[fromdate, todate])
    context_dict['booking_list'] = booking_list
    context_dict['fromdate'] = fromdate
    context_dict['todate'] = todate
    return render_to_response('rapido/staff/view_allbooking.html',context_dict,context)

@login_required
@csrf_exempt
def staff_dutyslip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    # booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status=1)
    # context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/staff/dutyslip_list.html',context_dict,context)

@login_required
@csrf_exempt
def staff_dutyslip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    booking_list= Bookings.objects.filter(pickup_date_time__contains=fromdate)
    print booking_list

    dutyslip_list= Dutyslip.objects.filter(booking__in=Bookings.objects.filter(pickup_date_time__contains=fromdate),status=1)
    
    print dutyslip_list
    context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate
    return render_to_response('rapido/staff/dutyslip_list.html',context_dict,context)


@login_required
@csrf_exempt
def staff_ontrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    dutyslip_list= Dutyslip.objects.filter(status=2)

    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/staff/ontrip_list.html',context_dict,context)

@login_required
@csrf_exempt
def staff_ontrip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    dutyslip_list= Dutyslip.objects.filter(booking__in=Bookings.objects.filter(pickup_date_time__contains=fromdate),status=2)

    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate

    return render_to_response('rapido/staff/ontrip_list.html',context_dict,context)

@login_required
@csrf_exempt
def staff_alltrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    # dutyslip_list= Dutyslip.objects.filter(created_date__range=[fromdate,todate])
    dutyslip_list= Dutyslip.objects.all()
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/staff/alltrip_list.html',context_dict,context)

@login_required
@csrf_exempt
def staff_alltriplist(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    dutyslip_list= Dutyslip.objects.filter(created_date__range=[fromdate, todate])
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate
    context_dict['todate'] = todate

    return render_to_response('rapido/staff/alltrip_list.html',context_dict,context)


@login_required
@csrf_exempt
def staff_closetrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status=3)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/staff/closetrip_list.html',context_dict,context)

@login_required
@csrf_exempt
def staff_closetrip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(created_date__contains =fromdate,status=3)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate

    return render_to_response('rapido/staff/closetrip_list.html',context_dict,context)

@csrf_exempt
def staff_create_booking_others(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place
 
    return render_to_response('rapido/staff/create_booking_others.html',context_dict,context)

@csrf_exempt
def staff_create_booking_company(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place

    return render_to_response('rapido/staff/create_booking.html',context_dict,context)


@csrf_exempt
def staff_create_continuous_booking(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place

    return render_to_response('rapido/staff/create_continuous_booking.html',context_dict,context)


@csrf_exempt
def admin_create_continuous_booking(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place

    return render_to_response('rapido/master/create_continuous_booking.html',context_dict,context)



@csrf_exempt
def staff_create_oldbooking_company(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place

    return render_to_response('rapido/staff/oldbooking.html',context_dict,context)

@csrf_exempt
def admin_create_oldbooking_company(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    company_list = Company.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['billing_base']= billing_base
    context_dict['cat_list'] = cat_list
    context_dict['service_type']= service_type
    context_dict['company_list']= company_list
    context_dict['service_place']=service_place

    return render_to_response('rapido/master/oldbooking.html',context_dict,context)

@login_required
def staff_assigncab(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    print bookingno
    booking=Bookings.objects.get(booking_id=bookingno)
    print booking.id
    print booking.booking_id
    chauffeur= Chauffeur.objects.all()
    vehicle = Vehicle.objects.all()
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor_list'] = vendor_list
    return render_to_response('rapido/staff/admin_assigncab.html',context_dict,context)

@login_required
def staff_createdutyslip(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    user= request.user
    booking= Bookings.objects.get(booking_id=bookingno)
    booking.status_id=2
    booking.save()
    print "booking status change aytu"

    booking = Dutyslip.objects.get(booking=booking)  

    context = {'booking': booking}

    html_content = render_to_string('rapido/tripemail.html', context=context).strip()

    booking=Bookings.objects.get(booking_id=bookingno)
    chauffeur= Chauffeur.objects.all()
    vehicle = Vehicle.objects.all()
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor'] = vendor_list
    return render_to_response('rapido/staff/assigncab.html',context_dict,context)

@login_required
def staff_viewdutyslip_detail(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    service_type = Servicetype.objects.all()
    billing_base = Billingbase.objects.all()
    service_place = City.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor'] = vendor_list
    return render_to_response('rapido/staff/viewdutyslip_detail.html',context_dict,context)



@login_required
def staff_dutyslip(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    dutyslip=Dutyslip.objects.get(booking=booking)
    chauffeur= Chauffeur.objects.all()
    context_dict =totalcount(request)
    cat_list = Category.objects.all()
    vendor_list = Vendor.objects.all()
    context_dict['cat_list'] = cat_list
    context_dict['booking']= booking
    context_dict['vendor'] = vendor_list
    context_dict['dutyslip']= dutyslip
    return render_to_response('rapido/staff/dutyslip.html',context_dict,context)

@login_required
def staff_receivetrip_list(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(status=2)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list

    return render_to_response('rapido/staff/receivetrip_list.html',context_dict,context)

@login_required
def staff_receivetrip_list1(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    user = request.user
    #booking_list= Bookings.objects.filter(status=2)
    dutyslip_list= Dutyslip.objects.filter(created_date__contains=fromdate,status=2)

    #context_dict['booking_list'] = booking_list
    context_dict['dutyslip_list']= dutyslip_list
    context_dict['fromdate'] = fromdate

    return render_to_response('rapido/staff/receivetrip_list.html',context_dict,context)


@login_required
def staff_closetrip(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    dutyslip=Dutyslip.objects.get(booking=booking)
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip

    return render_to_response('rapido/staff/close_trip.html',context_dict,context)


@login_required
def staff_close_tripsheet(request,bookingno):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    booking.status_id=5
    booking.save()
    dutyslip=Dutyslip.objects.get(booking=booking)
    dutyslip.status_id=4
    dutyslip.save()
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip

    return admin_closetrip_list(request)

@login_required
def staff_dispatch_vehicle(request,bookingno):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Bookings.objects.get(booking_id=bookingno)
    booking.status_id=3
    booking.save()
    dutyslip=Dutyslip.objects.get(booking=booking)
    dutyslip.status_id=2
    dutyslip.save()
    context_dict['booking']= booking
    context_dict['dutyslip']= dutyslip
    return render_to_response('rapido/staff/dutyslip.html',context_dict,context)


@login_required
def copyairportprice(request,company_id,fromcity_id,tocity_id):
    context = RequestContext(request)
    context_dict = {}
    company_id=company_id
    fromcity_id = fromcity_id
    tocity_id = tocity_id
    company_airportratecard1 = Company_airport_ratecard.objects.filter(company_id=company_id,city_id=fromcity_id)

    for c in company_airportratecard1:
        # print c.base_rate
        print " airport loop"
        vehicle_varient = c.vehicle_varient
        base_rate = c.base_rate
        category_id = c.category_id
        city_id = tocity_id
        company_id = company_id
        created_by = request.user
        service_type_id = c.service_type_id
        try:
            company_airportratecard2 = Company_airport_ratecard(created_by=created_by,vehicle_varient=vehicle_varient,base_rate=base_rate,company_id=company_id,city_id=city_id,category_id=category_id,service_type_id=service_type_id)
            company_airportratecard2.save()
            print company_airportratecard2.base_rate
        except IntegrityError as e:
            print e.message
    return HttpResponse("success")

@login_required
def copycityprice(request,company_id,fromcity_id,tocity_id):
    context = RequestContext(request)
    context_dict = {}
    company_id=company_id
    fromcity_id = fromcity_id
    tocity_id = tocity_id
    company_cityratecard1 = Company_city_ratecard.objects.filter(company_id=company_id,city_id=fromcity_id)

    for c in company_cityratecard1:
        vehicle_varient = c.vehicle_varient
        fgr = c.fgr
        base_rate = c.base_rate
        extra_kmrate = c.extra_kmrate
        extra_hrrate = c.extra_hrrate
        night_batta = c.night_batta
        category_id = c.category_id
        city_id = tocity_id
        company_id = company_id
        created_by = request.user
        service_type_id = c.service_type_id
        slab_id = c.slab_id
        try:
            company_cityratecard2 = Company_city_ratecard(created_by=created_by,vehicle_varient=vehicle_varient,base_rate=base_rate,company_id=company_id,city_id=city_id,category_id=category_id,service_type_id=service_type_id,fgr=fgr,slab_id=slab_id,night_batta=night_batta, extra_hrrate=extra_hrrate ,extra_kmrate=extra_kmrate)
            company_cityratecard2.save()
            print company_cityratecard2.base_rate
        except IntegrityError as e:
            print e.message
    return HttpResponse("json.dumps(success), content_type='application/json'")

@login_required
def copyoutstationprice(request,company_id,fromcity_id,tocity_id):
    context = RequestContext(request)
    context_dict = {}
    company_id=company_id
    fromcity_id = fromcity_id
    tocity_id = tocity_id
    company_outstationratecard1 = Company_outstation_ratecard.objects.filter(company_id=company_id,city_id=fromcity_id)

    for c in company_outstationratecard1:
        vehicle_varient = c.vehicle_varient
        min_km = c.min_km
        perkm_rate = c.perkm_rate
        extrakm_rate = c.extrakm_rate
        day_batta = c.day_batta
        night_batta = c.night_batta
        category_id = c.category_id
        city_id = tocity_id
        company_id = company_id
        created_by = request.user
        service_type_id = c.service_type_id
        try:
            company_outstationratecard2 = Company_outstation_ratecard(created_by=created_by,vehicle_varient=vehicle_varient,min_km=min_km,company_id=company_id,city_id=city_id,category_id=category_id,service_type_id=service_type_id,perkm_rate=perkm_rate,extrakm_rate=extrakm_rate,day_batta=day_batta,night_batta=night_batta)
            company_outstationratecard2.save()
            print company_outstationratecard2.min_km
        except IntegrityError as e:
            print e.message
    return HttpResponse("json.dumps(success), content_type='application/json'")


# handling server exception 

def handler404(request):
    return render(request, 'rapido/404.html', status=404)

def handler500(request):
    return render(request, 'rapido/500.html', status=500)



@login_required
@csrf_exempt
def staff_datewisebookings(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    # booking_list =(Bookings.objects.filter(pickup_date_time__range=[fromdate, todate],status=1)|Bookings.objects.filter(pickup_date_time__range=[fromdate, todate],status=2)).order_by("pickup_date_time")
    booking_list= (Bookings.objects.filter(pickup_date_time__contains=fromdate,status=1)|Bookings.objects.filter(pickup_date_time__contains=fromdate,status=2)).order_by("pickup_date_time")

    context_dict['booking_list'] = booking_list
    context_dict['fromdate'] = fromdate
    context_dict['todate'] = todate

    return render_to_response('rapido/staff/booking.html',context_dict,context)

@login_required
@csrf_exempt
def admin_datewisebookings(request,fromdate,todate):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    # booking_list= Bookings.objects.filter(pickup_date_time__contains=fromdate,status=1).order_by("pickup_date_time")
    # context_dict['booking_list'] = booking_list

    booking_list= (Bookings.objects.filter(pickup_date_time__contains=fromdate,status=1)|Bookings.objects.filter(pickup_date_time__contains=fromdate,status=2)).order_by("pickup_date_time")

    context_dict['fromdate'] = fromdate
    context_dict['booking_list'] = booking_list

    return render_to_response('rapido/master/booking.html',context_dict,context)



@login_required
@csrf_exempt
def cancelbooking(request,bookingid):
    context = RequestContext(request)
    context_dict = {}
    id = bookingid
    reason = request.POST['reason']
    note = request.POST['note']

    try:
        cancelbooking = Bookings.objects.get(booking_id=id)
        try:
            canceldutyslip = Dutyslip.objects.get(booking=cancelbooking,status_id=1)
            canceldutyslip.comment = "This Booking is Cancelled"
            user = request.user 
            canceldutyslip.updated_by = user
            canceldutyslip.remarks = str(reason)
            canceldutyslip.comment = str(note)+" and cancel done by "+ user.username
            canceldutyslip.updated_date = datetime.datetime.now()
            canceldutyslip.status_id = 5
            canceldutyslip.save()
        except Exception as e:
            print e.message

        cancelbooking.comment = "This Booking is Cancelled"
        user = request.user 
        cancelbooking.updated_by = user
        cancelbooking.remarks = str(reason)
        cancelbooking.comment = str(note)+" and cancel done by "+ user.username
        cancelbooking.updated_date = datetime.datetime.now()
        cancelbooking.status_id=6
        cancelbooking.save()
        print "Booking cancelled successfully"
        message = "1"
    except Exception as e:
        print e.message
        message = e.message

 
    data= {'message':message}
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type="application/json")


@login_required
def admin_cancelledbookinglist(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    cancelled_list = Bookings.objects.filter(status_id=6)

    context_dict['cancelled_list'] = cancelled_list
    return render_to_response('rapido/master/cancelledbooking.html',context_dict,context)


@login_required
def view_cancelledbooking_detail(request,bookingid):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking = Bookings.objects.get(booking_id=bookingid)
    context_dict['booking'] = booking
    print bookingid
    return render_to_response('rapido/master/cancelled_booking.html',context_dict,context)

#--------------------------------------

def totalcount(request):
    context = RequestContext(request)
    context_dict = {}
    today = date.today()
    total_pending_booking = Bookings.objects.filter(pickup_date_time__contains=today,status_id=1).count()
    total_pending_dispatch = Dutyslip.objects.filter(booking__in=Bookings.objects.filter(pickup_date_time__contains=today),status=1).count()
    total_ontrip = Dutyslip.objects.filter(booking__in=Bookings.objects.filter(pickup_date_time__contains=today),status_id=2).count()
    total_cancelled = Bookings.objects.filter(pickup_date_time__month=today.month,status_id=6).count()
    total_pendingtoclose = Dutyslip.objects.filter(created_date__month=today.month,status_id=3).count()
    total_closed_trips = Dutyslip.objects.filter(created_date__month=today.month,status_id=4).count()
    context_dict = { 
                     'total_ontrip':total_ontrip,
                     'total_pendingtoclose':total_pendingtoclose,
                     'total_closed_trips':total_closed_trips,
                     'total_cancelled':total_cancelled,
                     'total_pending_booking':total_pending_booking,
                     'total_pending_dispatch':total_pending_dispatch,
                 }
    return (context_dict)



@login_required
def matser1(request,fromdate,todate):
    context = RequestContext(request)
    context_dict = {}
    # total_bookings_tillnow = Bookings.objects.filter(created_date__range=[fromdate, todate]).count()
    # total_pending_booking = Bookings.objects.filter(created_date__range=[fromdate, todate],status_id=1).count()
    # total_pending_dispatch = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=1).count()
    # total_ontrip = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=2).count()
    # total_cancelled = Bookings.objects.filter(created_date__range=[fromdate,todate],status_id=6).count()
    # total_pendingtoclose = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=3).count()
    # total_closed_trips = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=4).count()
    context_dict =totalcount(request)
    context_dict['fromdate'] = fromdate
    return render_to_response('rapido/master/master.html', context_dict, context)

@login_required
def staff1(request,fromdate,todate):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    # total_bookings_tillnow = Bookings.objects.filter(created_date__range=[fromdate, todate]).count()
    # total_pending_booking = Bookings.objects.filter(created_date__range=[fromdate, todate],status_id=1).count()
    # total_pending_dispatch = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=1).count()
    # total_ontrip = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=2).count()
    # total_canceled = Bookings.objects.filter(created_date__range=[fromdate,todate],status_id=6).count()
    # total_pendingtoclose = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=3).count()
    # total_closed_trips = Dutyslip.objects.filter(created_date__range=[fromdate,todate],status_id=4).count()
    # context_dict = { 'total_bookings_tillnow':total_bookings_tillnow,
    #                  'total_ontrip':total_ontrip,
    #                  'total_pendingtoclose':total_pendingtoclose,
    #                  'total_closed_trips':total_closed_trips,
    #                  'total_canceled':total_canceled,
    #                  'total_pending_booking':total_pending_booking,
    #                  'total_pending_dispatch':total_pending_dispatch,
    #                  'date':date,}
    context_dict['fromdate'] = fromdate
    return render_to_response('rapido/staff/staff.html', context_dict, context)


#========== for date conversion ===================
import datetime
#need to convert the date while imporing the data from excel sheet to db or to access 
def minimalist_xldate_as_datetime(xldate):
    datemode= 0
    # datemode: 0 for 1900-based, 1 for 1904-based
    return (
        datetime.datetime(1899, 12, 30)
        + datetime.timedelta(days=xldate + 1462 * datemode)
        )
@csrf_exempt
def add_chauffeur_vehicel(request,vendorid):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    filename = request.FILES['filename']
    newfilename = filename.read()
    # newfilename = "/home/bookmane/Desktop/README.md"+str(filename)
    book = xlrd.open_workbook(file_contents=newfilename)
    sheet = book.sheet_by_name("Sheet1")
    vendor =Vendor.objects.get(id=vendorid)
    rcount =0
    ncount =0
    if sheet:        
        for r in range(1, sheet.nrows):
            print "===========row=========" ,r
            vendor = vendor
            vehicle_no = sheet.cell(r,0).value
            vehicle_modelname = sheet.cell(r,1).value
            vehicle_colour = sheet.cell(r,2).value
            seat_capacity = sheet.cell(r,3).value
            fc_date = sheet.cell(r,4).value
            fcexpairy_date =  minimalist_xldate_as_datetime(fc_date)

            tax_date = sheet.cell(r,5).value
            tax_expire_date =  minimalist_xldate_as_datetime(tax_date)
            
            insurance_date = sheet.cell(r,6).value
            insurance_exp_date =  minimalist_xldate_as_datetime(insurance_date)
            vehicle_engine_no = sheet.cell(r,7).value
            pucexp = sheet.cell(r,8).value
            puc_exp =  minimalist_xldate_as_datetime(pucexp)

            permit = sheet.cell(r,9).value
            chauffeur_name = sheet.cell(r,10).value
            chauffeur_phoneno = sheet.cell(r,11).value
            chauffeur_drivinglicense = sheet.cell(r,12).value
      
            drivinglicense_expire_date = sheet.cell(r,13).value

            chauffeur_drivinglicense_expire_date = minimalist_xldate_as_datetime(drivinglicense_expire_date)

            chauffeur_badgeno = sheet.cell(r,14).value
            badge_expired_date = sheet.cell(r,15).value


            chauffeur_badge_expired_date = minimalist_xldate_as_datetime(badge_expired_date)

            chauffeur_address = sheet.cell(r,16).value
            police_verification= sheet.cell(r,17).value
            created_by = request.user

            try:
                add_vehicel = Chauffeur_vehicel(vendor =vendor,vehicle_no =vehicle_no,vehicle_modelname =vehicle_modelname,
                    vehicle_colour =vehicle_colour,seat_capacity =seat_capacity,fcexpairy_date =fcexpairy_date,tax_expire_date =tax_expire_date,
                    insurance_exp_date =insurance_exp_date,vehicle_engine_no =vehicle_engine_no,puc_exp =puc_exp,permit =permit,
                    chauffeur_name =chauffeur_name,chauffeur_phoneno =chauffeur_phoneno,chauffeur_drivinglicense =chauffeur_drivinglicense,
                    chauffeur_drivinglicense_expire_date =chauffeur_drivinglicense_expire_date,chauffeur_badgeno =chauffeur_badgeno,
                    chauffeur_badge_expired_date =chauffeur_badge_expired_date, chauffeur_address =chauffeur_address,
                    police_verification =police_verification,created_by=created_by)
                add_vehicel.save()
                rcount=rcount+1
            except:
                print "already data is their"
                ncount=ncount+1

        rows = str(sheet.nrows)
        m1= "I just imported "+str(rcount)+" rows from file And "+ str(ncount) +" rows got error out of "+ rows +" while saving to BD!"

        message = " Data inserted sucessfully,"+m1

        chauffeur_vehicel_list = Chauffeur_vehicel.objects.filter(vendor= vendor)
        context_dict['vendor']=vendor
        context_dict['chauffeur_vehicel_list']=chauffeur_vehicel_list
        context_dict['message']=message
        return render_to_response( 'rapido/master/vendor_details.html',context_dict,context)

    message = "check details once"
    context_dict = {'message':message}

    vendor = Vendor.objects.get(id=vendorid)
    chauffeur_vehicel_list = Chauffeur_vehicel.objects.filter(vendor= vendor)
    context_dict['vendor']=vendor
    context_dict['chauffeur_vehicel_list']=chauffeur_vehicel_list
    context_dict['message']=message
    return render_to_response( 'rapido/master/vendor_details.html',context_dict,context)


# def add_chauffeur_vehicel(request,vendorid):
#     context = RequestContext(request)
#     context_dict = {}
#     if(request.method == "POST"):
#         if 'filename' in request.FILES:
#             filename = request.FILES['filename']
#             print filename,type(filename)
#             newfilename = "/home/manju/rapido/hosted/6/product008/rapido/"+str(filename)
#             book = xlrd.open_workbook(newfilename)
#             sheet = book.sheet_by_name("Sheet1")
#             vendor =Vendor.objects.get(id=vendorid)
#             rcount =0
#             ncount =0
#             for r in range(1, sheet.nrows):
#                 print "===========row=========" ,r
#                 vendor = vendor
#                 vehicle_no = sheet.cell(r,0).value
#                 vehicle_modelname = sheet.cell(r,1).value
#                 vehicle_colour = sheet.cell(r,2).value
#                 seat_capacity = sheet.cell(r,3).value
#                 fc_date = sheet.cell(r,4).value
#                 fcexpairy_date =  minimalist_xldate_as_datetime(fc_date)

#                 tax_date = sheet.cell(r,5).value
#                 tax_expire_date =  minimalist_xldate_as_datetime(tax_date)
                
#                 insurance_date = sheet.cell(r,6).value
#                 insurance_exp_date =  minimalist_xldate_as_datetime(insurance_date)
#                 vehicle_engine_no = sheet.cell(r,7).value
#                 pucexp = sheet.cell(r,8).value
#                 puc_exp =  minimalist_xldate_as_datetime(pucexp)

#                 permit = sheet.cell(r,9).value
#                 chauffeur_name = sheet.cell(r,10).value
#                 chauffeur_phoneno = sheet.cell(r,11).value
#                 chauffeur_drivinglicense = sheet.cell(r,12).value
          
#                 drivinglicense_expire_date = sheet.cell(r,13).value

#                 chauffeur_drivinglicense_expire_date = minimalist_xldate_as_datetime(drivinglicense_expire_date)

#                 chauffeur_badgeno = sheet.cell(r,14).value
#                 badge_expired_date = sheet.cell(r,15).value


#                 chauffeur_badge_expired_date = minimalist_xldate_as_datetime(badge_expired_date)

#                 chauffeur_address = sheet.cell(r,16).value
#                 police_verification= sheet.cell(r,17).value
#                 created_by = request.user

#                 try:
#                     add_vehicel = Chauffeur_vehicel(vendor =vendor,vehicle_no =vehicle_no,vehicle_modelname =vehicle_modelname,
#                         vehicle_colour =vehicle_colour,seat_capacity =seat_capacity,fcexpairy_date =fcexpairy_date,tax_expire_date =tax_expire_date,
#                         insurance_exp_date =insurance_exp_date,vehicle_engine_no =vehicle_engine_no,puc_exp =puc_exp,permit =permit,
#                         chauffeur_name =chauffeur_name,chauffeur_phoneno =chauffeur_phoneno,chauffeur_drivinglicense =chauffeur_drivinglicense,
#                         chauffeur_drivinglicense_expire_date =chauffeur_drivinglicense_expire_date,chauffeur_badgeno =chauffeur_badgeno,
#                         chauffeur_badge_expired_date =chauffeur_badge_expired_date, chauffeur_address =chauffeur_address,
#                         police_verification =police_verification,created_by=created_by)
#                     add_vehicel.save()
#                     rcount=rcount+1
#                 except:
#                     print "already data is their"
#                     ncount=ncount+1

#             rows = str(sheet.nrows)
#             m1= "I just imported "+str(rcount)+" rows from file And "+ str(ncount) +" rows got error out of "+ rows +" while saving to BD!"

#             message = " Data inserted sucessfully,"+m1
#             status = 1
#             data= {'message':message,'status':status}
#             json_data = json.dumps(data)
#             return HttpResponse(json_data, content_type="application/json")

#     status = 0
#     message = "check details once"
#     data= {'message':message,'status':status}
#     json_data = json.dumps(data)
#     return HttpResponse(json_data, content_type="application/json")

#--------------------------------------------------------------------------------------

# Sales activities
@login_required
@csrf_exempt
def sales(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict['cat_list'] = cat_list
    company_type_list = Companytype.objects.all()
    context_dict['company_type_list']= company_type_list
    company_client_list = Company.objects.all()
    context_dict['company_client_list']=company_client_list    
    return render_to_response( 'rapido/sales/sales.html',context_dict,context)

@login_required
@csrf_exempt
def sales_companydetail(request,companyid):
    print " bantu"
    context = RequestContext(request)
    context_dict = {}
    cat_list = Category.objects.all()
    city_list = City.objects.all()
    slab_list=Slab.objects.all()
    travelservice_type_list = Travelservicetype.objects.all()
    vehicle_model = Vehicle_varient.objects.all()
    context_dict['vehicle_model']=vehicle_model
    context_dict['cat_list'] = cat_list
    context_dict['city_list']= city_list
    context_dict['slab_list']=slab_list
    context_dict['travelservice_type_list']=travelservice_type_list
    company = Company.objects.get(id=companyid)
    context_dict['company']=company
    return render_to_response('rapido/sales/sales_company_detail.html',context_dict,context)


@login_required
@csrf_exempt
def sales_addCompany(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict['cat_list'] = cat_list
    company_type_list = Companytype.objects.all()
    context_dict['company_type_list']= company_type_list

    if request.method == 'POST':
        company_name = request.POST['company_name']
        company_type = request.POST['company_type']
        # company_website = request.POST['company_website']
        company_phoneno = request.POST['company_phoneno']
        company_email = request.POST['company_email']

        company_manager_name = request.POST['company_manager_name']
        company_manager_mobileno=request.POST['company_manager_mobileno']
        company_manager_email = request.POST['company_manager_email']
        company_payment_type = request.POST['company_payment_type']
        
        company_agreement_start_date = request.POST['company_agreement_start_date']
        company_agreement_end_date = request.POST['company_agreement_end_date']
        
        travelling_time_treshhold = request.POST['travelling_time_treshhold']
        gst= request.POST['gst']
        pan = request.POST['pan']

        if 'company_documents' in request.FILES:
            company_documents  = request.FILES['company_documents']
        else:
            company_documents =""

        if 'company_logo' in request.FILES:
            company_logo = request.FILES['company_logo']

        # cuser=User(username=company_name,email=company_email)
        # cuser.set_password("abc123")
        # cuser.save()

        user= request.user
        company_type= Companytype.objects.get(id=company_type)

        street_address= request.POST['street_address']
        landmark = request.POST['landmark']
        area = request.POST['area']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        address=Location(created_by=user, street_address=street_address,landmark=landmark,area=area,city=city,state=state,pincode=pincode,country=country)
        address.save()

        company = Company(created_by=user, company_name=company_name,company_type=company_type,company_phoneno=company_phoneno,company_email=company_email,company_manager_name=company_manager_name,company_manager_mobileno=company_manager_mobileno,company_manager_email=company_manager_email,company_payment_type=company_payment_type,company_agreement_start_date=company_agreement_start_date,company_agreement_end_date=company_agreement_end_date,travelling_time_treshhold=travelling_time_treshhold,company_logo=company_logo,company_documents=company_documents,gst=gst,pan=pan)
        cuser=User(username=company_name,email=company_email)
        cuser.set_password("abc123")
        cuser.save()

        company.user=cuser
        company.company_address=address
        company.save()
        print company.id
        return HttpResponseRedirect('/rapido/sales_set_ratecard/%s/' % company.id )

    company_client_list = Company.objects.all()
    context_dict['company_client_list']=company_client_list    
    return render_to_response( 'rapido/sales/sales.html',context_dict,context)

@login_required
@csrf_exempt
def sales_set_ratecard(request,companyid):
    print " bantu"
    context = RequestContext(request)
    context_dict = {}
    company = Company.objects.get(id=companyid)
    context_dict['company']=company
    cat_list = Category.objects.all()
    city_list = City.objects.all()
    slab_list=Slab.objects.all()
    travelservice_type_list = Travelservicetype.objects.all()
    vehicle_model = Vehicle_varient.objects.all()
    context_dict['vehicle_model']=vehicle_model
    context_dict['cat_list'] = cat_list
    context_dict['city_list']= city_list
    context_dict['slab_list']=slab_list
    context_dict['travelservice_type_list']=travelservice_type_list
    return render_to_response( 'rapido/sales/sales_ratecard.html',context_dict,context)


def get_completedetail(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    if request.method == 'POST':
        bookingid = request.POST['bookingid']
        try:
            booking=Bookings.objects.get(booking_id=bookingid)
            smsdetails= Smsforothers.objects.filter(booking_id=bookingid)
            context_dict['booking'] = booking
            context_dict['smsdetails']= smsdetails
            message = "Resulut Is:"
            context_dict['success']= message

            return render_to_response('rapido/master/completedetail.html',context_dict,context)
        except:
            message = " This Booking Details Not Present"
            context_dict['error']= message
            return render_to_response('rapido/master/completedetail.html',context_dict,context)
    return render_to_response('rapido/master/completedetail.html',context_dict,context)

#--------------------------------- Changes made from here ---------------------------------------


def billingreport(request):    
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)

    filename = request.FILES['filename']
    newfilename = filename.read()
    book = xlrd.open_workbook(file_contents=newfilename)
    # #print number of sheets
    no_of_sheet= book.nsheets
    #print no_of_sheet,"no_of_sheet=",type(no_of_sheet)
    if book:
        for i in range(0,book.nsheets):
            #print i,"index"
            # get the first worksheet
            first_sheet = book.sheet_by_index(i)
            # #print first_sheet,"first_sheet"
     
            # sheet = book.sheet_by_name("first_sheet")

            sheet = first_sheet
            # #print " sheet working",sheet
            rcount =0
            ncount =0
            if sheet:
                #print "iiiiiii",i        
                # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
                for r in range(1, sheet.nrows):
                    idd = sheet.cell(r,0).value

                    date_of = sheet.cell(r,1).value
                    date_used =  minimalist_xldate_as_datetime(date_of)
                    date_of_usage = date_used

                    booking_id = sheet.cell(r,2).value
                    #print "booking_id", booking_id
                    client_name = sheet.cell(r,3).value
                    billing_address = sheet.cell(r,4).value
                    company_pan = sheet.cell(r,5).value
                    company_gst = sheet.cell(r,6).value

                    city_requested = sheet.cell(r,7).value
                    city_used = sheet.cell(r,8).value
                    vehicle_request = sheet.cell(r,9).value
                    
                    user_name = sheet.cell(r,10).value
                    guest_phoneno = sheet.cell(r,11).value

                    booked_by = sheet.cell(r,12).value
                    code = sheet.cell(r,13).value
                    pickup = sheet.cell(r,14).value
                    pickuptime = sheet.cell(r,15).value
                    #print "pickuptime", pickuptime
                    drop = sheet.cell(r,16).value
                    duty_type = sheet.cell(r,17).value

                    drivername = sheet.cell(r,18).value

                    driverphoneno = sheet.cell(r,19).value
                    vehicle_no = sheet.cell(r,20).value
                    
                    vdate_out =  sheet.cell(r,21).value
                    date1 =  minimalist_xldate_as_datetime(vdate_out)
                    date_out =  date1
                    # #print "date out", date_out

                    vdate_in =  sheet.cell(r,22).value
                    date2 =  minimalist_xldate_as_datetime(vdate_in)
                    date_in = date2
                    # #print "date in", date_in

                    no_of_days = sheet.cell(r,23).value

                    km_out = sheet.cell(r,24).value
                    time_out = sheet.cell(r,25).value

                    km_in = sheet.cell(r,26).value
                    time_in =  sheet.cell(r,27).value

                    total_km = sheet.cell(r,28).value
                    total_hour = sheet.cell(r,29).value

                    parking_toll =sheet.cell(r,30).value

                    slab_used = sheet.cell(r,31).value
                    extra_km_run = sheet.cell(r,32).value
                    extra_hr_run = sheet.cell(r,33).value
             
                    extra_km_rate = sheet.cell(r,34).value
                    extra_hour_rate = sheet.cell(r,35).value
                    base_slab_rate = sheet.cell(r,36).value

                    extra_hr_amt = sheet.cell(r,37).value
                    extra_km_amt = sheet.cell(r,38).value
                    total_amount = sheet.cell(r,39).value

                    night_batta = sheet.cell(r,40).value
                    day_batta = sheet.cell(r,41).value
                    interstate_tax = sheet.cell(r,42).value
                    others = sheet.cell(r,43).value
                    total = sheet.cell(r,44).value
                    gst = sheet.cell(r,45).value
                    total_bill_amount =sheet.cell(r,46).value

                    cgst = sheet.cell(r,47).value 
                    sgst = sheet.cell(r,47).value
                    fgr = sheet.cell(r,48).value
                    # fgr = 0
                    try:
                        billingsummary = Billingsummary( booking_id=booking_id,
                                            client_name = client_name,billing_address = billing_address,company_pan = company_pan,company_gst = company_gst,
                                            city = city_requested,city_used = city_used,vehicle_request = vehicle_request,  
                                            user_name = user_name,guest_phoneno = guest_phoneno,booked_by = booked_by,code = code,
                                            pickup = pickup,pickuptime = pickuptime,drop = drop,duty_type = duty_type,
                                            drivername = drivername,driver_phoneno = driverphoneno,vehicle_no = vehicle_no, 
                                            date_of_usage = date_of_usage,date_out =  date_out,date_in = date_in,no_of_days = no_of_days,
                                            km_out = km_out,time_out = time_out,km_in = km_in,time_in = time_in,total_km = total_km,total_hour = total_hour,
                                            parking_toll = parking_toll,slab_used = slab_used,extra_km_run = extra_km_run,extra_hr_run = extra_hr_run, 
                                            extra_km_rate = extra_km_rate,extra_hour_rate = extra_hour_rate, base_slab_rate = base_slab_rate,extra_hr_amt = extra_hr_amt,
                                            extra_km_amt = extra_km_amt,total_amount = total_amount,night_batta = night_batta, day_batta = day_batta,
                                            interstate_tax =interstate_tax , other_amt = others,total = total,gst = gst,total_bill_amount =total_bill_amount,
                                            cgst=cgst,sgst=sgst,fgr=fgr)
                        print booking_id
                        billingsummary.save()

                    except IntegrityError as e:
                        print "data present"

                    except e:
                        print "error in fileds",e

        message = " Data inserted sucessfully,"
        context_dict['message']=message
        ##print "All Done! Bye, for now."
        columns = str(sheet.ncols)
        today=date.today()
        booking_list= Billingsummary.objects.filter(created_date__contains=today)
        # booking_list= Billingsummary.objects.all()
        context_dict['booking_list'] = booking_list
        return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)

    today=date.today()
    # booking_list= Billingsummary.objects.filter(created_date__contains=today)
    booking_list= Billingsummary.objects.all()
    message = "Sheet name not proper"
    context_dict['message']=message
    context_dict['booking_list'] = booking_list
    return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)

#============ old Billing history =========

# def billingreport(request):    
#     context = RequestContext(request)
#     context_dict = {}
#     context_dict =totalcount(request)

#     filename = request.FILES['filename']
#     newfilename = filename.read()
#     book = xlrd.open_workbook(file_contents=newfilename)
#     # #print number of sheets
#     no_of_sheet= book.nsheets
#     #print no_of_sheet,"no_of_sheet=",type(no_of_sheet)
#     if book:
#         for i in range(0,book.nsheets):
#             #print i,"index"
#             # get the first worksheet
#             first_sheet = book.sheet_by_index(i)
#             # #print first_sheet,"first_sheet"
     
#             # sheet = book.sheet_by_name("first_sheet")

#             sheet = first_sheet
#             # #print " sheet working",sheet
#             rcount =0
#             ncount =0
#             if sheet:
#                 #print "iiiiiii",i        
#                 # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
#                 for r in range(1, sheet.nrows):
#                     idd = sheet.cell(r,0).value

#                     date_of = sheet.cell(r,1).value
#                     date_used =  minimalist_xldate_as_datetime(date_of)
#                     date_of_usage = date_used

#                     booking_id = sheet.cell(r,2).value
#                     #print "booking_id", booking_id
#                     client_name = sheet.cell(r,3).value
#                     billing_address = sheet.cell(r,4).value
#                     company_pan = sheet.cell(r,5).value
#                     company_gst = sheet.cell(r,6).value

#                     city_requested = sheet.cell(r,7).value
#                     city_used = sheet.cell(r,8).value
#                     vehicle_request = sheet.cell(r,9).value
                    
#                     user_name = sheet.cell(r,10).value
#                     guest_phoneno = sheet.cell(r,11).value

#                     booked_by = sheet.cell(r,12).value
#                     code = sheet.cell(r,13).value
#                     pickup = sheet.cell(r,14).value
#                     pickuptime = sheet.cell(r,15).value
#                     #print "pickuptime", pickuptime
#                     drop = sheet.cell(r,16).value
#                     duty_type = sheet.cell(r,17).value

#                     drivername = sheet.cell(r,18).value

#                     driverphoneno = sheet.cell(r,19).value
#                     vehicle_no = sheet.cell(r,20).value
                    
#                     vdate_out =  sheet.cell(r,21).value
#                     date1 =  minimalist_xldate_as_datetime(vdate_out)
#                     date_out =  date1
#                     # #print "date out", date_out

#                     vdate_in =  sheet.cell(r,22).value
#                     date2 =  minimalist_xldate_as_datetime(vdate_in)
#                     date_in = date2
#                     # #print "date in", date_in

#                     no_of_days = sheet.cell(r,23).value

#                     km_out = sheet.cell(r,24).value
#                     time_out = sheet.cell(r,26).value

#                     km_in = sheet.cell(r,28).value
#                     time_in =  sheet.cell(r,29).value

#                     total_km = sheet.cell(r,32).value
#                     total_hour = sheet.cell(r,33).value

#                     parking_toll =sheet.cell(r,34).value

#                     slab_used = sheet.cell(r,35).value
#                     extra_km_run = sheet.cell(r,36).value
#                     extra_hr_run = sheet.cell(r,37).value
             
#                     extra_km_rate = sheet.cell(r,38).value
#                     extra_hour_rate = sheet.cell(r,39).value
#                     base_slab_rate = sheet.cell(r,40).value

#                     extra_hr_amt = sheet.cell(r,41).value
#                     extra_km_amt = sheet.cell(r,42).value
#                     total_amount = sheet.cell(r,43).value

#                     night_batta = sheet.cell(r,44).value
#                     day_batta = sheet.cell(r,45).value
#                     interstate_tax = sheet.cell(r,46).value
#                     others = sheet.cell(r,47).value
#                     total = sheet.cell(r,48).value
#                     gst = sheet.cell(r,49).value
#                     total_bill_amount =sheet.cell(r,50).value

#                     cgst = sheet.cell(r,51).value 
#                     sgst = sheet.cell(r,51).value
#                     fgr = sheet.cell(r,31).value
#                     # fgr = 0
#                     try:
#                         billingsummary = Billingsummary( booking_id=booking_id,
#                                             client_name = client_name,billing_address = billing_address,company_pan = company_pan,company_gst = company_gst,
#                                             city = city_requested,city_used = city_used,vehicle_request = vehicle_request,  
#                                             user_name = user_name,guest_phoneno = guest_phoneno,booked_by = booked_by,code = code,
#                                             pickup = pickup,pickuptime = pickuptime,drop = drop,duty_type = duty_type,
#                                             drivername = drivername,driver_phoneno = driverphoneno,vehicle_no = vehicle_no, 
#                                             date_of_usage = date_of_usage,date_out =  date_out,date_in = date_in,no_of_days = no_of_days,
#                                             km_out = km_out,time_out = time_out,km_in = km_in,time_in = time_in,total_km = total_km,total_hour = total_hour,
#                                             parking_toll = parking_toll,slab_used = slab_used,extra_km_run = extra_km_run,extra_hr_run = extra_hr_run, 
#                                             extra_km_rate = extra_km_rate,extra_hour_rate = extra_hour_rate, base_slab_rate = base_slab_rate,extra_hr_amt = extra_hr_amt,
#                                             extra_km_amt = extra_km_amt,total_amount = total_amount,night_batta = night_batta, day_batta = day_batta,
#                                             interstate_tax =interstate_tax , other_amt = others,total = total,gst = gst,total_bill_amount =total_bill_amount,
#                                             cgst=cgst,sgst=sgst,fgr=fgr)
#                         print booking_id
#                         billingsummary.save()

#                     except IntegrityError as e:
#                         print "data present"

#                     except e:
#                         print "error in fileds",e

#         message = " Data inserted sucessfully,"
#         context_dict['message']=message
#         ##print "All Done! Bye, for now."
#         columns = str(sheet.ncols)
#         today=date.today()
#         booking_list= Billingsummary.objects.filter(created_date__contains=today)
#         # booking_list= Billingsummary.objects.all()
#         context_dict['booking_list'] = booking_list
#         return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)

#     today=date.today()
#     # booking_list= Billingsummary.objects.filter(created_date__contains=today)
#     booking_list= Billingsummary.objects.all()
#     message = "Sheet name not proper"
#     context_dict['message']=message
#     context_dict['booking_list'] = booking_list
#     return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)

# def billingreport(request):    
#     context = RequestContext(request)
#     context_dict = {}
#     context_dict =totalcount(request)

#     filename = request.FILES['filename']
#     newfilename = filename.read()
#     book = xlrd.open_workbook(file_contents=newfilename)
#     # #print number of sheets
#     no_of_sheet= book.nsheets
#     #print no_of_sheet,"no_of_sheet=",type(no_of_sheet)
#     if book:
#         for i in range(0,book.nsheets):
#             #print i,"index"
#             # get the first worksheet
#             first_sheet = book.sheet_by_index(i)
#             # #print first_sheet,"first_sheet"
     
#             # sheet = book.sheet_by_name("first_sheet")

#             sheet = first_sheet
#             # #print " sheet working",sheet
#             rcount =0
#             ncount =0
#             if sheet:
#                 #print "iiiiiii",i        
#                 # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
#                 for r in range(1, sheet.nrows):
#                     idd = sheet.cell(r,0).value

#                     date_of = sheet.cell(r,1).value
#                     date_used =  minimalist_xldate_as_datetime(date_of)
#                     date_of_usage = date_used

#                     booking_id = sheet.cell(r,2).value
#                     #print "booking_id", booking_id
#                     client_name = sheet.cell(r,3).value
#                     billing_address = sheet.cell(r,4).value
#                     company_pan = sheet.cell(r,5).value
#                     company_gst = sheet.cell(r,6).value

#                     city_requested = sheet.cell(r,7).value
#                     city_used = sheet.cell(r,8).value
#                     vehicle_request = sheet.cell(r,9).value
                    
#                     user_name = sheet.cell(r,10).value
#                     guest_phoneno = sheet.cell(r,11).value

#                     booked_by = sheet.cell(r,12).value
#                     code = sheet.cell(r,13).value
#                     pickup = sheet.cell(r,14).value
#                     pickuptime = sheet.cell(r,15).value
#                     #print "pickuptime", pickuptime
#                     drop = sheet.cell(r,16).value
#                     duty_type = sheet.cell(r,17).value

#                     drivername = sheet.cell(r,18).value

#                     driverphoneno = sheet.cell(r,19).value
#                     vehicle_no = sheet.cell(r,20).value
                    
#                     vdate_out =  sheet.cell(r,21).value
#                     date1 =  minimalist_xldate_as_datetime(vdate_out)
#                     date_out =  date1
#                     # #print "date out", date_out

#                     vdate_in =  sheet.cell(r,22).value
#                     date2 =  minimalist_xldate_as_datetime(vdate_in)
#                     date_in = date2
#                     # #print "date in", date_in

#                     no_of_days = sheet.cell(r,23).value

#                     km_out = sheet.cell(r,24).value
#                     time_out = sheet.cell(r,25).value

#                     km_in = sheet.cell(r,26).value
#                     time_in =  sheet.cell(r,27).value

#                     total_km = sheet.cell(r,28).value
#                     total_hour = sheet.cell(r,29).value

#                     parking_toll =sheet.cell(r,30).value

#                     slab_used = sheet.cell(r,31).value
#                     extra_km_run = sheet.cell(r,32).value
#                     extra_hr_run = sheet.cell(r,33).value
             
#                     extra_km_rate = sheet.cell(r,34).value
#                     extra_hour_rate = sheet.cell(r,35).value
#                     base_slab_rate = sheet.cell(r,36).value

#                     extra_hr_amt = sheet.cell(r,37).value
#                     extra_km_amt = sheet.cell(r,38).value
#                     total_amount = sheet.cell(r,39).value

#                     night_batta = sheet.cell(r,40).value
#                     day_batta = sheet.cell(r,41).value
#                     interstate_tax = sheet.cell(r,42).value
#                     others = sheet.cell(r,43).value
#                     total = sheet.cell(r,44).value
#                     gst = sheet.cell(r,45).value
#                     total_bill_amount =sheet.cell(r,46).value

#                     cgst = sheet.cell(r,47).value 
#                     sgst = sheet.cell(r,47).value
#                     fgr = sheet.cell(r,48).value
#                     comment = sheet.cell(r,49).value
#                     # fgr = 0
#                     try:
#                         billingsummary = Billingsummary( booking_id=booking_id,
#                                             client_name = client_name,billing_address = billing_address,company_pan = company_pan,company_gst = company_gst,
#                                             city = city_requested,city_used = city_used,vehicle_request = vehicle_request,  
#                                             user_name = user_name,guest_phoneno = guest_phoneno,booked_by = booked_by,code = code,
#                                             pickup = pickup,pickuptime = pickuptime,drop = drop,duty_type = duty_type,
#                                             drivername = drivername,driver_phoneno = driverphoneno,vehicle_no = vehicle_no, 
#                                             date_of_usage = date_of_usage,date_out =  date_out,date_in = date_in,no_of_days = no_of_days,
#                                             km_out = km_out,time_out = time_out,km_in = km_in,time_in = time_in,total_km = total_km,total_hour = total_hour,
#                                             parking_toll = parking_toll,slab_used = slab_used,extra_km_run = extra_km_run,extra_hr_run = extra_hr_run, 
#                                             extra_km_rate = extra_km_rate,extra_hour_rate = extra_hour_rate, base_slab_rate = base_slab_rate,extra_hr_amt = extra_hr_amt,
#                                             extra_km_amt = extra_km_amt,total_amount = total_amount,night_batta = night_batta, day_batta = day_batta,
#                                             interstate_tax =interstate_tax , other_amt = others,total = total,gst = gst,total_bill_amount =total_bill_amount,
#                                             cgst=cgst,sgst=sgst,fgr=fgr,comment=comment)
#                         print booking_id
#                         billingsummary.save()

#                     except IntegrityError as e:
#                         print "data present"

#                     except e:
#                         print "error in fileds",e

#         message = " Data inserted sucessfully,"
#         context_dict['message']=message
#         ##print "All Done! Bye, for now."
#         columns = str(sheet.ncols)
#         today=date.today()
#         booking_list= Billingsummary.objects.filter(created_date__contains=today)
#         # booking_list= Billingsummary.objects.all()
#         context_dict['booking_list'] = booking_list
#         return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)

#     today=date.today()
#     # booking_list= Billingsummary.objects.filter(created_date__contains=today)
#     booking_list= Billingsummary.objects.all()
#     message = "Sheet name not proper"
#     context_dict['message']=message
#     context_dict['booking_list'] = booking_list
#     return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)



# def billingreport(request):    
#     context = RequestContext(request)
#     context_dict = {}
#     context_dict =totalcount(request)

#     filename = request.FILES['filename']
#     newfilename = filename.read()
#     book = xlrd.open_workbook(file_contents=newfilename)
#     # #print number of sheets
#     no_of_sheet= book.nsheets
#     #print no_of_sheet,"no_of_sheet=",type(no_of_sheet)
#     if book:
#         for i in range(0,book.nsheets):
#             #print i,"index"
#             # get the first worksheet
#             first_sheet = book.sheet_by_index(i)
#             # #print first_sheet,"first_sheet"
     
#             # sheet = book.sheet_by_name("first_sheet")

#             sheet = first_sheet
#             # #print " sheet working",sheet
#             rcount =0
#             ncount =0
#             if sheet:
#                 #print "iiiiiii",i        
#                 # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
#                 for r in range(1, sheet.nrows):
#                     idd = sheet.cell(r,0).value

#                     date_of = sheet.cell(r,1).value
#                     date_used =  minimalist_xldate_as_datetime(date_of)
#                     date_of_usage = date_used

#                     booking_id = sheet.cell(r,2).value
#                     #print "booking_id", booking_id
#                     client_name = sheet.cell(r,3).value
#                     billing_address = sheet.cell(r,4).value
#                     company_pan = sheet.cell(r,5).value
#                     company_gst = sheet.cell(r,6).value

#                     city_requested = sheet.cell(r,7).value
#                     city_used = sheet.cell(r,8).value
#                     vehicle_request = sheet.cell(r,9).value
                    
#                     user_name = sheet.cell(r,10).value
#                     guest_phoneno = sheet.cell(r,11).value

#                     booked_by = sheet.cell(r,12).value
#                     code = sheet.cell(r,13).value
#                     pickup = sheet.cell(r,14).value
#                     pickuptime = sheet.cell(r,15).value
#                     #print "pickuptime", pickuptime
#                     drop = sheet.cell(r,16).value
#                     duty_type = sheet.cell(r,17).value

#                     drivername = sheet.cell(r,18).value

#                     driverphoneno = sheet.cell(r,19).value
#                     vehicle_no = sheet.cell(r,20).value
                    
#                     vdate_out =  sheet.cell(r,21).value
#                     date1 =  minimalist_xldate_as_datetime(vdate_out)
#                     date_out =  date1
#                     # #print "date out", date_out

#                     vdate_in =  sheet.cell(r,22).value
#                     date2 =  minimalist_xldate_as_datetime(vdate_in)
#                     date_in = date2
#                     # #print "date in", date_in

#                     no_of_days = sheet.cell(r,23).value

#                     km_out = sheet.cell(r,24).value
#                     time_out = sheet.cell(r,26).value

#                     km_in = sheet.cell(r,28).value
#                     time_in =  sheet.cell(r,29).value

#                     total_km = sheet.cell(r,30).value
#                     total_hour = sheet.cell(r,31).value

#                     parking_toll =sheet.cell(r,32).value

#                     slab_used = sheet.cell(r,33).value
#                     extra_km_run = sheet.cell(r,34).value
#                     extra_hr_run = sheet.cell(r,35).value
             
#                     extra_km_rate = sheet.cell(r,36).value
#                     extra_hour_rate = sheet.cell(r,37).value
#                     base_slab_rate = sheet.cell(r,38).value

#                     extra_hr_amt = sheet.cell(r,39).value
#                     extra_km_amt = sheet.cell(r,40).value
#                     total_amount = sheet.cell(r,41).value

#                     night_batta = sheet.cell(r,42).value
#                     day_batta = sheet.cell(r,43).value
#                     interstate_tax = sheet.cell(r,44).value
#                     others = sheet.cell(r,45).value
#                     total = sheet.cell(r,46).value
#                     gst = sheet.cell(r,47).value
#                     total_bill_amount =sheet.cell(r,48).value

#                     cgst = sheet.cell(r,49).value 
#                     sgst = sheet.cell(r,49).value
#                     fgr = sheet.cell(r,50).value
#                     try:
#                         billingsummary = Billingsummary( booking_id=booking_id,
#                                             client_name = client_name,billing_address = billing_address,company_pan = company_pan,company_gst = company_gst,
#                                             city = city_requested,city_used = city_used,vehicle_request = vehicle_request,  
#                                             user_name = user_name,guest_phoneno = guest_phoneno,booked_by = booked_by,code = code,
#                                             pickup = pickup,pickuptime = pickuptime,drop = drop,duty_type = duty_type,
#                                             drivername = drivername,driver_phoneno = driverphoneno,vehicle_no = vehicle_no, 
#                                             date_of_usage = date_of_usage,date_out =  date_out,date_in = date_in,no_of_days = no_of_days,
#                                             km_out = km_out,time_out = time_out,km_in = km_in,time_in = time_in,total_km = total_km,total_hour = total_hour,
#                                             parking_toll = parking_toll,slab_used = slab_used,extra_km_run = extra_km_run,extra_hr_run = extra_hr_run, 
#                                             extra_km_rate = extra_km_rate,extra_hour_rate = extra_hour_rate, base_slab_rate = base_slab_rate,extra_hr_amt = extra_hr_amt,
#                                             extra_km_amt = extra_km_amt,total_amount = total_amount,night_batta = night_batta, day_batta = day_batta,
#                                             interstate_tax =interstate_tax , other_amt = others,total = total,gst = gst,total_bill_amount =total_bill_amount,
#                                             cgst=cgst,sgst=sgst,fgr=fgr)
#                         print booking_id
#                         billingsummary.save()

#                     except IntegrityError as e:
#                         print "data present"

#                     except e:
#                         print "error in fileds",e

#         message = " Data inserted sucessfully,"
#         context_dict['message']=message
#         ##print "All Done! Bye, for now."
#         columns = str(sheet.ncols)
#         today=date.today()
#         booking_list= Billingsummary.objects.filter(created_date__contains=today)
#         # booking_list= Billingsummary.objects.all()
#         context_dict['booking_list'] = booking_list
#         return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)

#     today=date.today()
#     # booking_list= Billingsummary.objects.filter(created_date__contains=today)
#     booking_list= Billingsummary.objects.all()
#     message = "Sheet name not proper"
#     context_dict['message']=message
#     context_dict['booking_list'] = booking_list
#     return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)







@login_required
@csrf_exempt
def oldbookinghistroy(request):
    context = RequestContext(request)
    cat_list = Category.objects.all()
    context_dict = {}
    context_dict =totalcount(request)
    context_dict['cat_list'] = cat_list
    today=date.today()
    booking_list= Billingsummary.objects.filter(created_date__contains=today)
    # booking_list= Billingsummary.objects.all()
    context_dict['booking_list'] = booking_list
    return render_to_response('rapido/master/oldbookinghistroy.html',context_dict,context)


@login_required
def oldinvoice(request,id):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    booking=Billingsummary.objects.get(id=id)
    today = date.today()
    context_dict['today']= today
    context_dict['booking']= booking
    return render_to_response('rapido/oldinvoice.html',context_dict,context)

#------ vendor changes -----------------------------

@login_required
def alloldinvoice(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict =totalcount(request)
    today=date.today()
    billinglist= Billingsummary.objects.filter(created_date__contains=today).order_by('id')[00:100]
    context_dict['today']= today
    context_dict['billinglist']= billinglist
    return render_to_response('rapido/alloldinvoice.html',context_dict,context)



#------------------------ download -------------------------------

def download(request, file_type):

    sheet = excel.pe.Sheet(data)

    return excel.make_response(sheet, file_type)


def download_bookings(request):

    file_name1 = "manju24j"
    file_type1 = "xls"
    data = [['SL no','Booking received date','Booking ID','Booking needed On','City of booking','Type of Car','Company Name','Guest Name','Contact No','Booked By','Booking phoneno','Pickup Location','Time of Pick up','Drop Location','Type Of Duty','Status','Note']]
    bookings=Bookings.objects.all()
    slno=1

    print " done all=============="
    for i in bookings:
        print i.created_date
        createddate =i.created_date.strftime("%d-%b-%Y")
        bookingneededon =i.pickup_date_time.strftime("%d-%b-%Y") 
        cityofbooking = i.servicing_city.name
        typeofcar = i.requested_vehicle_model
        companyname = str(i.company)
        guestname =i.guest_name
        guestphoneno = i.guest_phoneno
        bookedby = i.booking_from
        bookerphoneno = i.booking_phoneno
        pickuplocation =i.pick_up_location

        pickuptiming = i.pickup_date_time.strftime("%H-%M") 
        
        droplocation =i.drop_location
        typeofduty = str(i.service_type)
        status = str(i.status)
        notes = i.remarks
        data.append([slno,createddate,i.booking_id,bookingneededon,cityofbooking,typeofcar,companyname,guestname,guestphoneno,bookedby,bookerphoneno,pickuplocation,pickuptiming,droplocation,typeofduty,status,notes])
        slno=slno+1

    return excel.make_response_from_array(
        data, file_type1, file_name=file_name1)

def download_dutyslip(request):

    file_name1 = "manju24j"
    file_type1 = "xls"
    data = [['SL no','Booking received date','Booking ID','Booking needed On','City of booking','Type of Car','Company Name','Guest Name','Contact No','Booked By','Pickup Location','Time of Pick up','Drop Location','Type Of Duty','Status']]
    bookings=Bookings.objects.all()
    slno=1

    for i in bookings:
        # print type(i.created_date)
        print i.created_date
        createddate =i.created_date.strftime("%d-%b-%Y")
        # dateout = datetime.datetime.strptime(i.created_date, "%m/%d/%Y")
        data.append([slno,createddate,'',i.booking_id])
        slno=slno+1
        # print i.created_date , type(i.pickup_date_time)

    # print data

    print type(data)

    return excel.make_response_from_array(
        data, file_type1, file_name=file_name1)


def download_companybookings(request,companyid):
    company=Company.objects.get(id=companyid)
    file_name1 = str(company.company_name)
    file_type1 = "xls"
    # data = [['SL no','Booking received date','Booking ID','Booking needed On','City of booking','Type of Car','Company Name','Guest Name','Contact No','Booked By','Booking phoneno','Pickup Location','Time of Pick up','Drop Location','Type Of Duty','Status','Note']]
    bookings=Bookings.objects.filter(company_id = companyid)
    slno=1

    print " done all=============="
    for i in bookings:
        print i.created_date
        createddate =i.created_date.strftime("%d-%b-%Y")
        bookingneededon =i.pickup_date_time.strftime("%d-%b-%Y") 
        cityofbooking = i.servicing_city.name
        typeofcar = i.requested_vehicle_model
        companyname = str(i.company)
        guestname =i.guest_name
        guestphoneno = i.guest_phoneno
        bookedby = i.booking_from
        bookerphoneno = i.booking_phoneno
        pickuplocation =i.pick_up_location

        pickuptiming = i.pickup_date_time.strftime("%H-%M") 
        
        droplocation =i.drop_location
        typeofduty = str(i.service_type)
        status = str(i.status)
        notes = i.remarks
        data.append([slno,createddate,i.booking_id,bookingneededon,cityofbooking,typeofcar,companyname,guestname,guestphoneno,bookedby,bookerphoneno,pickuplocation,pickuptiming,droplocation,typeofduty,status,notes])
        slno=slno+1

    return excel.make_response_from_array(
        data, file_type1, file_name=file_name1)

def download_companyinvoice(request,companyid):

    file_name1 = "manju24j"
    file_type1 = "xls"
    data = [['SL no','Booking received date','Booking ID','Booking needed On','City of booking','Type of Car','Company Name','Guest Name','Contact No','Booked By','Pickup Location','Time of Pick up','Drop Location','Type Of Duty','Status']]
    bookings=Bookings.objects.all()
    slno=1

    for i in bookings:
        # print type(i.created_date)
        print i.created_date
        createddate =i.created_date.strftime("%d-%b-%Y")
        # dateout = datetime.datetime.strptime(i.created_date, "%m/%d/%Y")
        data.append([slno,createddate,'',i.booking_id])
        slno=slno+1
        # print i.created_date , type(i.pickup_date_time)

    # print data

    print type(data)

    return excel.make_response_from_array(
        data, file_type1, file_name=file_name1)
