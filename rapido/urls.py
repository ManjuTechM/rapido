from django.conf.urls import url

from . import views,sendemail
from . import api_views , api
# from rapido.views import UserViewSet

# Bookingstatus,Dutyslipstatus,Invoicestatus,Travelservicetype,Vendortype,Billingbase


urlpatterns = [

   # API views

    # url(r'^user/', views.UserViewSet, name='UserViewSet'),

    # url(r'^user_details/(?P<pk>[0-9]+)/$',views.UserViewSet, name='UserViewSet'),

   # #1. To access the List of All Category list. and to create a new category 
    url(r'^api/category/', api.CategoryList.as_view()),

   # #2. To access the List of Single Category Details. Accept Single Argument primary key { id:12 }
    url(r'^api/category_details/(?P<pk>[0-9]+)/$', api.CategoryDetail.as_view()),



#------------- CITY -----------------
  
    url(r'^api/add_city/$', api_views.Citycreate.as_view()),
    url(r'^api/list_city/$', api_views.CityList.as_view()),
    url(r'^api/city_details/(?P<pk>[0-9]+)/$', api_views.CityDetail.as_view()),
    url(r'^api/update_city/(?P<pk>[0-9]+)/$', api_views.Cityupdate.as_view()),
    url(r'^api/delete_city/(?P<pk>[0-9]+)/$', api_views.CityDelete.as_view()),


#------------- Service Type ---------------

    url(r'^api/add_servicetype/$', api_views.Servicetypecreate.as_view()),
    url(r'^api/list_servicetype/$', api_views.ServicetypeList.as_view()),
    url(r'^api/servicetype_details/(?P<pk>[0-9]+)/$',api_views.ServicetypeDetail.as_view()),
    url(r'^api/update_servicetype/(?P<pk>[0-9]+)/$', api_views.Servicetypeupdate.as_view()),
    url(r'^api/delete_servicetype/(?P<pk>[0-9]+)/$', api_views.ServicetypeDelete.as_view()),

#-----------------Vendor Type--------

    url(r'^api/add_vendortype/$', api_views.Vendortypecreate.as_view()),
    url(r'^api/list_vendortype/$', api_views.VendortypeList.as_view()),
    url(r'^api/vendortype_details/(?P<pk>[0-9]+)/$', api_views.VendortypeDetail.as_view()),
    url(r'^api/update_vendortype/(?P<pk>[0-9]+)/$', api_views.Vendortypeupdate.as_view()),
    url(r'^api/delete_vendortype/(?P<pk>[0-9]+)/$', api_views.VendortypeDelete.as_view()),

#------------------SLAB----------------
    url(r'^api/add_slab/$', api_views.Slabcreate.as_view()),
    url(r'^api/list_slab/$', api_views.SlabList.as_view()),
    url(r'^api/slab_details/(?P<pk>[0-9]+)/$', api_views.SlabDetail.as_view()),
    url(r'^api/update_slab/(?P<pk>[0-9]+)/$', api_views.Slabupdate.as_view()),
    url(r'^api/delete_slab/(?P<pk>[0-9]+)/$', api_views.SlabDelete.as_view()),

#----------- BookingStatus------------
    url(r'^api/add_bookingstatus/$', api_views.Bookingstatuscreate.as_view()),
    url(r'^api/list_bookingstatus/$', api_views.BookingstatusList.as_view()),
    url(r'^api/bookingstatus_details/(?P<pk>[0-9]+)/$', api_views.BookingstatusDetail.as_view()),
    url(r'^api/update_bookingstatus/(?P<pk>[0-9]+)/$', api_views.Bookingstatusupdate.as_view()),
    url(r'^api/delete_bookingstatus/(?P<pk>[0-9]+)/$', api_views.BookingstatusDelete.as_view()),

#------------------Dutyslip Status---------------
    url(r'^api/add_dutyslipstatus/$', api_views.Dutyslipstatuscreate.as_view()),
    url(r'^api/list_dutyslipstatus/$', api_views.DutyslipstatusList.as_view()),
    url(r'^api/dutyslipstatus_details/(?P<pk>[0-9]+)/$', api_views.DutyslipstatusDetail.as_view()),
    url(r'^api/update_dutyslipstatus/(?P<pk>[0-9]+)/$', api_views.Dutyslipstatusupdate.as_view()),
    url(r'^api/delete_dutyslipstatus/(?P<pk>[0-9]+)/$', api_views.DutyslipstatusDelete.as_view()),

#------------- Invoice status----------------------

    url(r'^api/add_invoicestatus/$', api_views.Invoicestatuscreate.as_view()),
    url(r'^api/list_invoicestatus/$', api_views.InvoicestatusList.as_view()),
    url(r'^api/invoicestatus_details/(?P<pk>[0-9]+)/$', api_views.InvoicestatusDetail.as_view()),
    url(r'^api/update_invoicestatus/(?P<pk>[0-9]+)/$', api_views.Invoicestatusupdate.as_view()),
    url(r'^api/delete_invoicestatus/(?P<pk>[0-9]+)/$', api_views.InvoicestatusDelete.as_view()),

#--------------Billingbase-----------------
    url(r'^api/add_billingbase/$', api_views.Billingbasecreate.as_view()),
    url(r'^api/list_billingbase/$', api_views.BillingbaseList.as_view()),
    url(r'^api/billingbase_details/(?P<pk>[0-9]+)/$', api_views.BillingbaseDetail.as_view()),
    url(r'^api/update_billingbase/(?P<pk>[0-9]+)/$', api_views.Billingbaseupdate.as_view()),
    url(r'^api/delete_billingbase/(?P<pk>[0-9]+)/$', api_views.BillingbaseDelete.as_view()),

#----------------Company_type------
    url(r'^api/add_companytype/$', api_views.Companytypecreate.as_view()),
    url(r'^api/list_companytype/$', api_views.CompanytypeList.as_view()),
    url(r'^api/companytype_details/(?P<pk>[0-9]+)/$', api_views.CompanytypeDetail.as_view()),
    url(r'^api/update_companytype/(?P<pk>[0-9]+)/$', api_views.Companytypeupdate.as_view()),
    url(r'^api/delete_companytype/(?P<pk>[0-9]+)/$', api_views.CompanytypeDelete.as_view()),

#----------------Travelservicetype------

    url(r'^api/add_travelservicetype/$', api_views.Travelservicetypecreate.as_view()),
    url(r'^api/list_travelservicetype/$', api_views.TravelservicetypeList.as_view()),
    url(r'^api/travelservicetype_details/(?P<pk>[0-9]+)/$', api_views.TravelservicetypeDetail.as_view()),
    url(r'^api/update_travelservicetype/(?P<pk>[0-9]+)/$', api_views.Travelservicetypeupdate.as_view()),
    url(r'^api/delete_travelservicetype/(?P<pk>[0-9]+)/$', api_views.TravelservicetypeDelete.as_view()),

#--------------- Category ---------------------------------------------------

    url(r'^api/add_category/$', api_views.Categorycreate.as_view()),
    url(r'^api/list_category/$', api_views.CategoryList.as_view()),
    url(r'^api/category_details/(?P<pk>[0-9]+)/$', api_views.CategoryDetail.as_view()),
    url(r'^api/update_category/(?P<pk>[0-9]+)/$', api_views.Categoryupdate.as_view()),
    url(r'^api/delete_category/(?P<pk>[0-9]+)/$', api_views.CategoryDelete.as_view()),

#--------------- Vehicle varient --------------------------------------------------

    url(r'^api/add_vehiclemodels/$', api_views.Vehicle_varientList.as_view()),
    url(r'^api/vehiclemodel/(?P<pk>[0-9]+)/$', api_views.Vehicle_varientDetail.as_view()),
    url(r'^api/delete_vehiclemodel/(?P<pk>[0-9]+)/$', api_views.Vehicle_varientDelete.as_view()),

#----------------------------------location-------------------------------

   #1. To access the List of All Vehicle  list. and to create a new category 
    url(r'^api/add_location/$', api_views.LocationList.as_view()),
   #2. To access the List of Single Vehicle  Details. Accept Single Argument primary key { id:12 }
    url(r'^api/get_location_details/(?P<pk>[0-9]+)/$', api_views.LocationDetail.as_view()),
    #3. to delete Vehicle  Details Accept Single Argument primary key { id:12 }
    url(r'^api/delete_location/(?P<pk>[0-9]+)/$', api_views.LocationDelete.as_view()),

#------------------- Vendor ------------------------------------------------

   #1. CREATE
    url(r'^api/addvendor/$', api_views.Vendoradd.as_view()),
    url(r'^api/add_vendor/$', api_views.Vendorcreate.as_view()),
    url(r'^api/list_vendor/$', api_views.VendorList.as_view()),
    url(r'^api/vendor_details/(?P<pk>[0-9]+)/$', api_views.VendorDetail.as_view()),
    url(r'^api/update_vendor/(?P<pk>[0-9]+)/$', api_views.Vendorupdate.as_view()),
    url(r'^api/delete_vendor/(?P<pk>[0-9]+)/$', api_views.VendorDelete.as_view()),

#---------- Vehicle -------------------------

    url(r'^api/add_vehicle/$', api_views.Vehiclecreate.as_view()),
    url(r'^api/list_vehicle/$', api_views.VehicleList.as_view()),
    url(r'^api/vehicle_details/(?P<pk>[0-9]+)/$', api_views.VehicleDetail.as_view()),
    url(r'^api/update_vehicle/(?P<pk>[0-9]+)/$', api_views.Vehicleupdate.as_view()),
    url(r'^api/delete_vehicle/(?P<pk>[0-9]+)/$', api_views.VehicleDelete.as_view()),

#------------------- chauffeur/Driver ---------------------------------------

    url(r'^api/addchauffeur/$', api_views.Chauffeuradd.as_view()),
    url(r'^api/add_chauffeur/$', api_views.Chauffeurcreate.as_view()),
    url(r'^api/list_chauffeur/$', api_views.ChauffeurList.as_view()),
    url(r'^api/chauffeur_details/(?P<pk>[0-9]+)/$', api_views.ChauffeurDetail.as_view()),
    url(r'^api/update_chauffeur/(?P<pk>[0-9]+)/$', api_views.Chauffeurupdate.as_view()),
    url(r'^api/delete_chauffeur/(?P<pk>[0-9]+)/$', api_views.ChauffeurDelete.as_view()),


#------------------- Company ------------------------------------------------
 
    url(r'^api/addcompany/$', api_views.Companyadd.as_view()),
    url(r'^api/add_company/$', api_views.Companycreate.as_view()),
    url(r'^api/list_company/$', api_views.CompanyList.as_view()),
    url(r'^api/company_details/(?P<pk>[0-9]+)/$', api_views.CompanyDetail.as_view()),
    url(r'^api/update_company/(?P<pk>[0-9]+)/$', api_views.Companyupdate.as_view()),
    url(r'^api/delete_company/(?P<pk>[0-9]+)/$', api_views.CompanyDelete.as_view()),


#------------------- Stanared Rate Card ------------------------------------------------
 
    url(r'^standard_ratecard/$', views.standard_ratecard, name='standard_ratecard'),


    #---------- AIRPORT ----------------
    url(r'^api/add_airportratecard/$', api_views.Airport_ratecardadd.as_view()),
    url(r'^api/list_airportratecard/$', api_views.Airport_ratecardList.as_view()),
    url(r'^api/update_airportratecard/(?P<pk>[0-9]+)/$', api_views.Airport_ratecardDetail.as_view()),
    url(r'^api/delete_airportratecard/(?P<pk>[0-9]+)/$', api_views.Airport_ratecardDelete.as_view()),
  
    url(r'^api/airportratecard/$', api.Airport_ratecardList.as_view()),
    url(r'^api/airportratecardbycity/(?P<city_id>[0-9]+)/$', api_views.AirportratecardcityList.as_view()),

    url(r'^api/airportprice/(?P<city_id>[0-9]+)/(?P<category_id>[0-9]+)/$', api_views.AirportpriceDetail.as_view()),
    # url(r'^api/airportratecard/$',  views.Airport_ratecard, name="Airport_ratecard"),

    #---------- OUT-STATION ----------------

    url(r'^api/add_outstationratecard/$', api_views.Outstation_ratecardadd.as_view()),
    url(r'^api/list_outstationratecard/$', api_views.Outstation_ratecardList.as_view()),
    url(r'^api/update_outstationratecard/(?P<pk>[0-9]+)/$', api_views.Outstation_ratecardDetail.as_view()),
    url(r'^api/delete_outstationratecard/(?P<pk>[0-9]+)/$', api_views.Outstation_ratecardDelete.as_view()),
 
    url(r'^api/set_outstationratecard/$', api.Outstation_ratecardList.as_view()),
    url(r'^api/outstationratecardbycity/(?P<city_id>[0-9]+)/$', api_views.OutstationratecardcityList.as_view()),

    url(r'^api/outstationprice/(?P<city_id>[0-9]+)/(?P<category_id>[0-9]+)/$', api_views.OutstationpriceDetail.as_view()),

    #---------- CITY-STATION ----------------

    url(r'^api/add_cityratecard/$', api_views.City_ratecardadd.as_view()),
    url(r'^api/list_cityratecard/$', api_views.City_ratecardList.as_view()),
    url(r'^api/update_cityratecard/(?P<pk>[0-9]+)/$', api_views.City_ratecardDetail.as_view()),
    url(r'^api/delete_cityratecard/(?P<pk>[0-9]+)/$', api_views.City_ratecardDelete.as_view()),
 
    url(r'^api/set_cityratecard/$', api.City_ratecardList.as_view()),
    url(r'^api/cityratecardbycity/(?P<city_id>[0-9]+)/$', api_views.CityratecardcityList.as_view()),

    url(r'^api/cityprice/(?P<city_id>[0-9]+)/(?P<category_id>[0-9]+)/$', api_views.CitypriceDetail.as_view()),

#------------------- Company Rate Card  pass argument company id------------------------------------------------

  #---------- COMPANY AIRPORT ----------------
    url(r'^api/add_companyairportratecard/$', api_views.Company_airport_ratecardadd.as_view()),
    url(r'^api/list_companyairportratecard/$', api_views.Company_airport_ratecardList.as_view()),
    url(r'^api/update_companyairportratecard/(?P<pk>[0-9]+)/$', api_views.Company_airport_ratecardDetail.as_view()),
    url(r'^api/delete_companyairportratecard/(?P<pk>[0-9]+)/$', api_views.Company_airport_ratecardDelete.as_view()),

    url(r'^api/set_companyairportratecard/$', api.Company_airport_ratecardList.as_view()),
    url(r'^api/companyairportratecardbycity/(?P<company_id>[0-9]+)/(?P<city_id>[0-9]+)/$', api_views.Company_airportratecardcityList.as_view()),

    url(r'^api/companyairportprice/(?P<company_id>[0-9]+)/(?P<city_id>[0-9]+)/(?P<category_id>[0-9]+)/$', api_views.Company_airportpriceDetail.as_view()),

  #----------COMPANY  OUT-STATION ----------------

    url(r'^api/add_companyoutstationratecard/$', api_views.Company_outstation_ratecardadd.as_view()),
    url(r'^api/list_companyoutstationratecard/$', api_views.Company_outstation_ratecardList.as_view()),
    url(r'^api/update_companyoutstationratecard/(?P<pk>[0-9]+)/$', api_views.Company_outstation_ratecardDetail.as_view()),
    url(r'^api/delete_companyoutstationratecard/(?P<pk>[0-9]+)/$', api_views.Company_outstation_ratecardDelete.as_view()),
 
    url(r'^api/set_companyoutstationratecard/$', api.Company_outstation_ratecardList.as_view()),
    url(r'^api/companyoutstationratecardbycity/(?P<company_id>[0-9]+)/(?P<city_id>[0-9]+)/$', api_views.Company_outstationratecardcityList.as_view()),
    url(r'^api/companyoutstationprice/(?P<company_id>[0-9]+)/(?P<city_id>[0-9]+)/(?P<category_id>[0-9]+)/$', api_views.Company_outstationpriceDetail.as_view()),


    #---------- CITY-STATION ----------------

    url(r'^api/add_companycityratecard/$', api_views.Company_city_ratecardadd.as_view()),
    url(r'^api/list_companycityratecard/$', api_views.Company_city_ratecardList.as_view()),
    url(r'^api/update_companycityratecard/(?P<pk>[0-9]+)/$', api_views.Company_city_ratecardDetail.as_view()),
    url(r'^api/delete_companycityratecard/(?P<pk>[0-9]+)/$', api_views.Company_city_ratecardDelete.as_view()),
 
    url(r'^api/set_companycityratecard/$', api.Company_city_ratecardList.as_view()),
    url(r'^api/companycityratecardbycity/(?P<company_id>[0-9]+)/(?P<city_id>[0-9]+)/$', api_views.Company_cityratecardcityList.as_view()),
    url(r'^api/companycityprice/(?P<company_id>[0-9]+)/(?P<city_id>[0-9]+)/(?P<category_id>[0-9]+)/$', api_views.Company_citypriceDetail.as_view()),


#----------------------------------------------------------------------------

    url(r'^api/get_bookings_list/$', api_views.BookingsList.as_view()),
    url(r'^api/get_bookings_details/(?P<pk>[0-9]+)/$', api_views.BookingsDetail.as_view()),
    url(r'^api/delete_bookings_details/(?P<pk>[0-9]+)/$', api_views.BookingsDelete.as_view()),

    url(r'^api/get_bookerlist/(?P<company_id>[0-9]+)/$', api_views.CompanybookerList.as_view()),


    url(r'^api/get_dutyslip_list/$', api_views.DutyslipList.as_view()),

    url(r'^api/get_dutyslip_details/(?P<pk>[0-9]+)/$', api_views.DutyslipDetail.as_view()),
    
    url(r'^api/delete_dutyslip_details/(?P<pk>[0-9]+)/$', api_views.DutyslipDelete.as_view()),


    url(r'^api/get_booker_list/$', api_views.CompanybookerList.as_view()),
    url(r'^api/get_booker_details/(?P<pk>[0-9]+)/$', api_views.CompanybookerDetail.as_view()),
    url(r'^api/delete_booker_details/(?P<pk>[0-9]+)/$', api_views.CompanybookerDelete.as_view()),



    url(r'^api/get_chauffeur_vehicel_list/$', api_views.Chauffeur_vehicelList.as_view()),
    url(r'^api/get_chauffeur_vehicel__details/(?P<pk>[0-9]+)/$', api_views.Chauffeur_vehicelDetail.as_view()),
    url(r'^api/delete_chauffeur_vehicel_details/(?P<pk>[0-9]+)/$', api_views.Chauffeur_vehicelDelete.as_view()),
    url(r'^api/get_chaufer_vehicle/(?P<vendor_id>[0-9]+)/$', api_views.Chauffeur_vehicelby_vendorList.as_view()),
    url(r'^api/chauffeur_vehicel_list/$', api_views.ChauffeurvehicelList.as_view()),


	# Home Index page link
    url(r'^$', views.index, name='index'),


    url(r'^bookingsms/(?P<bookingid>[0-9]+)/$', views.bookingsms, name='bookingsms'),
    url(r'^dutyslipsms/(?P<tripid>[0-9]+)/$', views.dutyslipsms, name='dutyslipsms'),


    url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', 
    views.sendSimpleEmail, name = 'sendSimpleEmail'),

    # url(r'^bookingemail/$', views.bookingemail, name='bookingemail'),
    url(r'^sendbookingemail/(?P<bookingid>[0-9]+)/$', views.sendbookingemail, name='sendbookingemail'),
    url(r'^sendbookingsms/(?P<bookingid>[0-9]+)/$', views.sendbookingsms, name='sendbookingsms'),

    url(r'^sendbookingsmsforothers/(?P<bookingid>[0-9]+)/$', views.sendbookingsmsforothers, name='sendbookingsmsforothers'),
    url(r'^sendtripdetailsmsforothers/(?P<tripid>[0-9]+)/$', views.sendtripdetailsmsforothers, name='sendtripdetailsmsforothers'),

    url(r'^sendcancelemail/(?P<bookingid>[0-9]+)/$', views.sendcancelemail, name='sendcancelemail'),
    url(r'^sendcancelsms/(?P<bookingid>[0-9]+)/$', views.sendcancelsms, name='sendcancelsms'),

    url(r'^sendtripdetailemail/(?P<tripid>[0-9]+)/$', views.sendtripdetailemail, name='sendtripdetailemail'),
    url(r'^sendtripdetailsmsforuser/(?P<tripid>[0-9]+)/$', views.sendtripdetailsmsforuser, name='sendtripdetailsmsforuser'),
    url(r'^sendtripdetailsmsfordriver/(?P<tripid>[0-9]+)/$', views.sendtripdetailsmsfordriver, name='sendtripdetailsmsfordriver'),

    url(r'^activatecompanyemail/(?P<cid>[0-9]+)/$', views.activatecompanyemail, name='activatecompanyemail'),
	# Register page link where he can login select account
	# url(r'^register/$', views.register, name='register'),


	# Login link for the all users
    url(r'^login/$', views.user_login, name='login'),

    # After Login link to the Mater/Admin page
    url(r'^master/$', views.matser, name='master'),
    url(r'^master/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.matser1, name='master1'),
 
 	# logout for all and redirects to home page
     url(r'^logout/$', views.user_logout, name='logout'),

   # After Login link to the Mater/Admin page
    url(r'^company/$', views.company, name='company'),

   # After Login link to the Mater/Admin page
    url(r'^staff/$', views.staff, name='staff'),

    url(r'^staff/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.staff1, name='staff1'),
#------------------- Matser Related Operations--------
  
    #  category list
     url(r'^category/$', views.mastercategory, name='mastercategory'),

    # 1.Creating new category
    url(r'^add_category/$', views.add_category, name='add_category'),
   
    #2. View  category
    url(r'^category_details/(?P<category_name_url>\w+)/$', views.category_details, name='category_details'),

    # 3.Update category
    url(r'^update_category/(?P<category_id>[0-9]+)/$', views.update_category, name='update_category'),

#--------------------------------------------------------------------


   # 1.vender list and creating vender
    url(r'^vendor/$', views.vendor_master, name='vendor_master'),

    url(r'^add_vendor/$', views.add_vendor_master, name='add_vendor_master'),

   # 2. View vender details
    url(r'^vendor_details/(?P<vendor_id>[0-9]+)/$', views.vendor_details, name='vendor_details'),

    url(r'^add_chauffeur_vehicel/(?P<vendorid>[0-9]+)/$', views.add_chauffeur_vehicel, name='add_chauffeur_vehicel'),

   # 3. Update vender details
   url(r'^update_vendor/(?P<vendor_id>[0-9]+)/$', views.update_vendor, name='update_vendor'),

#------------------------------------------------------------------------------------------
   # 1. Creating vehicle and vehicles list
  	url(r'^vehicle/$', views.vehicle_master, name='vehicle_master'),

    url(r'^add_vehicle/$', views.add_vehicle_master, name='add_vehicle_master'),

   # 2. View vehicle details
   #   url(r'^vehicle_details/(?P<vehicle_id>[0-9]+)/$', views.vehicle_details, name='vehicle_details'),

   # 3. Update vehicle details
   #  url(r'^update_vehicle/(?P<vehicle_id>[0-9]+)/$', views.update_vehicle, name='update_vehicle'),
#----------------------------------------------------------------------------------------

   # 1.Creating chauffeur
   url(r'^chauffeur/$', views.chauffeur_master, name='chauffeur_master'),

   # 2.View chauffeur Details
   # url(r'^chauffeur_details/$', views.chauffeur_details, name='chauffeur_details'),

   # 3.Update chauffeur
   # url(r'^update_chauffeur/$', views.chauffeur_master, name='chauffeur_master'),

#-----------------------------------------------------------------------------------------


   # 1 .Creating and Client company list
    url(r'^company_client/$', views.company_client_master, name='company_client_master'),

    url(r'^add_company_client/$', views.add_company_client_master, name='add_company_client_master'),

   # 2 .View Client company Details
   #   url(r'^company_client_details/$', views.company_client_master_details, name='company_client_master_details'),

   # 3 .Update Client company details
   #  url(r'^update_company_client/$', views.update_company_client_master, name='update_company_client_master'),
#-----------------------------------------------------------------------------------------

    url(r'^admin_booking_list/$', views.admin_booking_list, name='admin_booking_list'), 

    url(r'^admin_todaysbooking_list/$', views.admin_todaysbooking_list, name='admin_todaysbooking_list'), 

    url(r'^admin_viewbooking_detail/(?P<bookingno>\w+)/$',views.admin_viewbooking_detail,name='admin_viewbooking_detail'),

    url(r'^admin_view_all_booking/$', views.admin_view_all_booking, name='admin_view_all_booking'), 

    url(r'^admin_viewbookingdatewise/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.admin_viewbookingdatewise, name='admin_viewbookingdatewise'), 


    url(r'^admin_dutyslip_list/$', views.admin_dutyslip_list, name='admin_dutyslip_list'), 
    url(r'^admin_dutyslip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.admin_dutyslip_list1, name='admin_dutyslip_list1'), 

    url(r'^admin_ontrip_list/$', views.admin_ontrip_list, name='admin_ontrip_list'), 
    url(r'^admin_ontrip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.admin_ontrip_list1, name='admin_ontrip_list1'), 
    url(r'^admin_alltrip_list/$', views.admin_alltrip_list, name='admin_alltrip_list'), 

    url(r'^admin_closetrip_list/$', views.admin_closetrip_list, name='admin_closetrip_list'), 
    url(r'^admin_closetrip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.admin_closetrip_list1, name='admin_closetrip_list1'), 
   
    url(r'^admin_invoice_list/$', views.admin_invoice_list, name='admin_invoice_list'), 
  
#----------------------------------------------------------------------------------------


    # assign a cab for bookings / create duty slip
    url(r'^admin_companydetail/(?P<company_id>[0-9]+)/$', views.admin_companydetail, name='admin_companydetail'), 
    url(r'^admin_create_booking_others/$', views.admin_create_booking_others, name='admin_create_booking_others'),     
    url(r'^admin_createbooking/$', views.admin_createbooking, name='admin_createbooking'), 

    url(r'^admin_assigncab/(?P<bookingno>\w+)/$',views.admin_assigncab,name='admin_assigncab'),
    url(r'^admin_createdutyslip/(?P<bookingno>\w+)/$',views.admin_createdutyslip,name='admin_createdutyslip'),
    url(r'^admin_viewdutyslip_detail/(?P<bookingno>\w+)/$',views.admin_viewdutyslip_detail,name='admin_viewdutyslip_detail'),
    url(r'^admin_dutyslip/(?P<bookingno>\w+)/$',views.admin_dutyslip,name='admin_dutyslip'),

    url(r'^admin_receivetrip_list/$',views.admin_receivetrip_list,name='admin_receivetrip_list'),

    url(r'^admin_receivetrip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.admin_receivetrip_list1, name='admin_receivetrip_list1'), 

    url(r'^receive_tripsheet/(?P<bookingno>\w+)/$',views.receive_tripsheet,name='receive_tripsheet'),

    url(r'^admin_closetrip/(?P<bookingno>\w+)/$',views.admin_closetrip,name='admin_closetrip'),

    url(r'^admin_close_tripsheet/(?P<bookingno>\w+)/$',views.admin_close_tripsheet,name='admin_close_tripsheet'),

    url(r'^admin_invoice/(?P<bookingno>\w+)/$',views.admin_invoice,name='admin_invoice'),

    url(r'^admin_dispatch_vehicle/(?P<bookingno>\w+)/$',views.admin_dispatch_vehicle,name='admin_dispatch_vehicle'),

 

    url(r'^assign_cab/(?P<bookingno>\w+)/$',views.assign_cab,name='assign_cab'),

    # assign a cab for bookings / create duty slip
    url(r'^create_booking/$',views.create_booking,name='create_booking'),

    # assign a cab for bookings / create duty slip
    url(r'^all_booking_list/$',views.all_booking_list,name='all_booking_list'),

    url(r'^admin_completedtrip_list/$',views.admin_completedtrip_list,name='admin_completedtrip_list'),

    url(r'^company_invoice/(?P<bookingno>\w+)/$',views.company_invoice,name='company_invoice'),
    
    url(r'^admin_calculate_invoice/(?P<bookingno>\w+)/$',views.admin_calculate_invoice,name='admin_calculate_invoice'),

# below 3 urls for coping the rate card from one city to another city for perticular company 

    url(r'^copyairportprice/(?P<company_id>[0-9]+)/(?P<fromcity_id>[0-9]+)/(?P<tocity_id>[0-9]+)/$',views.copyairportprice,name='copyairportprice'),

    url(r'^copycityprice/(?P<company_id>[0-9]+)/(?P<fromcity_id>[0-9]+)/(?P<tocity_id>[0-9]+)/$',views.copycityprice,name='copycityprice'),

    url(r'^copyoutstationprice/(?P<company_id>[0-9]+)/(?P<fromcity_id>[0-9]+)/(?P<tocity_id>[0-9]+)/$',views.copyoutstationprice,name='copyoutstationprice'),

#----------------------------------------------------------------------------------------

   # assign a cab for bookings / create duty slip
    url(r'^create_dutyslip/(?P<bookingno>\w+)/$',views.create_dutyslip,name='create_dutyslip'),

    # Take a print out thats indicating the dispatch of the car from rapido office
    url(r'^dispatch_vehicle/(?P<dutyslip_no>\w+)/$',views.dispatch_vehicle,name='dispatch_vehicle'),

    # list of booking that are went for Trip/service
    url(r'^dispatched_list/$',views.dispatched_list,name='dispatched_list'),

    # list of booking that are went for Trip/service
    url(r'^completed_trip/$',views.completed_trip,name='completed_trip'),

#-----------------------------------------------------------------------------------------
    # # assign a cab for bookings / create duty slip
    url(r'^generate_invoice/(?P<dutyslip_no>\w+)/$',views.generate_invoice,name='generate_invoice'),

#----------------------------------------------------------------------------------------

   # Client company_view rate_card
    url(r'^company_view_ratecard/$', views.company_view_ratecard, name='company_view_ratecard'),


   # # After Login link Company Booking cabs
    url(r'^company_bookcab/$', views.company_bookcab, name='company_bookcab'),

    url(r'^company_viewbooking_detail/(?P<bookingno>\w+)/$',views.company_viewbooking_detail,name='company_viewbooking_detail'),

   #  # After Login link Company Booking cabs
    url(r'^booking_history/$', views.booking_history, name='booking_history'),
 
   url(r'^invoice_list/$', views.invoice_list, name='invoice_list'), 
 
    url(r'^invoice_print/(?P<invoice_no>\w+)/$',views.invoice_print,name='invoice_print'),
 
   #  # booking list 
   #  url(r'^booking_list/$', views.booking_list, name='booking_list'),

   #  # Duty slip pending
   #  url(r'^dutyslip_pending/$', views.dutyslip_pending, name='dutyslip_pending'),
    
   #  # View Invoice 
   #  url(r'^view_invoice/$', views.view_invoice, name='view_invoice'),

#============================================================================================
        # staff activities 

    url(r'^staff_todaysbooking_list/$', views.staff_todaysbooking_list, name='staff_todaysbooking_list'), 

    url(r'^staff_booking_list/$', views.staff_booking_list, name='staff_booking_list'), 

    url(r'^staff_viewbooking_detail/(?P<bookingno>\w+)/$',views.staff_viewbooking_detail,name='staff_viewbooking_detail'),

    url(r'^staff_view_all_booking/$', views.staff_view_all_booking, name='staff_view_all_booking'), 

    url(r'^staff_viewallbooking/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.staff_viewallbooking, name='staff_viewallbooking'), 

    url(r'^staff_dutyslip_list/$', views.staff_dutyslip_list, name='staff_dutyslip_list'), 

    url(r'^staff_dutyslip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.staff_dutyslip_list1, name='staff_dutyslip_list1'), 

    url(r'^staff_ontrip_list/$', views.staff_ontrip_list, name='staff_ontrip_list'), 
    url(r'^staff_ontrip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.staff_ontrip_list1, name='staff_ontrip_list1'), 
    url(r'^staff_alltrip_list/$', views.staff_alltrip_list, name='staff_alltrip_list'), 
    url(r'^staff_alltriplist/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.staff_alltriplist, name='staff_alltriplist'), 

    url(r'^staff_closetrip_list/$', views.staff_closetrip_list, name='staff_closetrip_list'), 
    url(r'^staff_closetrip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$', views.staff_closetrip_list1, name='staff_closetrip_list1'), 
  
#----------------------------------------------------------------------------------------
    url(r'^admin_create_oldbooking_company/$', views.admin_create_oldbooking_company, name='admin_create_oldbooking_company'),     

    url(r'^staff_create_oldbooking_company/$', views.staff_create_oldbooking_company, name='staff_create_oldbooking_company'),     

    # assign a cab for bookings / create duty slip
    url(r'^staff_create_booking_others/$', views.staff_create_booking_others, name='staff_create_booking_others'),     
    url(r'^staff_create_booking_company/$', views.staff_create_booking_company, name='staff_create_booking_company'), 

    url(r'^staff_assigncab/(?P<bookingno>\w+)/$',views.staff_assigncab,name='staff_assigncab'),
    url(r'^staff_createdutyslip/(?P<bookingno>\w+)/$',views.staff_createdutyslip,name='staff_createdutyslip'),
    url(r'^staff_viewdutyslip_detail/(?P<bookingno>\w+)/$',views.staff_viewdutyslip_detail,name='staff_viewdutyslip_detail'),
    url(r'^staff_dutyslip/(?P<bookingno>\w+)/$',views.staff_dutyslip,name='staff_dutyslip'),

    url(r'^staff_receivetrip_list/$',views.staff_receivetrip_list,name='staff_receivetrip_list'),
    url(r'^staff_receivetrip_list/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$',views.staff_receivetrip_list1,name='staff_receivetrip_list1'),
    # url(r'^staff_receive_tripsheet/(?P<bookingno>\w+)/$',staff_receive_tripsheet,name='staff_receive_tripsheet'),

    url(r'^staff_closetrip/(?P<bookingno>\w+)/$',views.staff_closetrip,name='staff_closetrip'),

    url(r'^staff_close_tripsheet/(?P<bookingno>\w+)/$',views.staff_close_tripsheet,name='staff_close_tripsheet'),

    url(r'^staff_dispatch_vehicle/(?P<bookingno>\w+)/$',views.staff_dispatch_vehicle,name='staff_dispatch_vehicle'),

    url(r'^staff_datewisebookings/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$',views.staff_datewisebookings,name='staff_datewisebookings'),

    url(r'^admin_datewisebookings/(?P<fromdate>\d{4}-\d{2}-\d{2})/(?P<todate>\d{4}-\d{2}-\d{2})/$',views.admin_datewisebookings,name='admin_datewisebookings'),

    url(r'^cancelbooking/(?P<bookingid>\w+)/$',views.cancelbooking,name='cancelbooking'),

    url(r'^admin_cancelledbookinglist/$',views.admin_cancelledbookinglist,name='admin_cancelledbookinglist'),

    url(r'^view_cancelledbooking_detail/(?P<bookingid>\w+)/$',views.view_cancelledbooking_detail,name='view_cancelledbooking_detail'),

    url(r'^get_completedetail/$',views.get_completedetail,name='get_completedetail'),

#--------------------------SALES URLS-------------------------------------------------------

    url(r'^sales/$',views.sales,name='sales'),

    url(r'^sales_companydetail/(?P<companyid>\w+)/$',views.sales_companydetail,name='sales_companydetail'),
    
    url(r'^sales_addCompany/$',views.sales_addCompany,name='sales_addCompany'),

    url(r'^sales_set_ratecard/(?P<companyid>\w+)/$',views.sales_set_ratecard,name='sales_set_ratecard'),

#----------------------------CHANGES DONE FROM-----------------------------------------------

    url(r'^billingreport/$', views.billingreport, name='billingreport'),

    url(r'^admin_oldinvoice_list/$', views.oldbookinghistroy, name='oldbookinghistroy'),
    
    url(r'^oldinvoice/(?P<id>[0-9]+)/$', views.oldinvoice, name='oldinvoice'),
    url(r'^alloldinvoice/$', views.alloldinvoice, name='alloldinvoice'),
    
    url(r'^api/getoldinvoice/(?P<pk>[0-9]+)/$', api_views.BillingDetail.as_view()),

    url(r'^download/(.*)', views.download, name="download"),
    
    url(r'^download_bookings/', views.download_bookings,name="download_bookings"),
    url(r'^download_dutyslip/', views.download_dutyslip,name="download_dutyslip"),
    url(r'^download_companybookings/(?P<companyid>\w+)/$', views.download_companybookings,name="download_companybookings"),
    url(r'^download_companyinvoice/(?P<companyid>\w+)/$', views.download_companyinvoice,name="download_companyinvoice"),
    # url(r'^download_c/', views.download_as_attachment,name="download_attachment"),
 
   url(r'^staff_create_continuous_booking/$', views.staff_create_continuous_booking, name='staff_create_continuous_booking'),
    url(r'^staff_create_continuous_booking/$', views.admin_create_continuous_booking, name='admin_create_continuous_booking'),
 

]