from django.contrib import admin

from rapido.models import City,Slab,Vendortype,Bookingstatus,Dutyslipstatus,Invoicestatus,Servicetype,Billingbase,Companytype,Vehicle_varient,Category,Travelservicetype,Vendortype 
from rapido.models import Location,Vendor,Vehicle,Chauffeur,Company,Bookings,Dutyslip,ClientInvoice,VendorInvoice,Bookingstatus,Dutyslipstatus,Invoicestatus,Billingbase,City_ratecard,Outstation_ratecard,Airport_ratecard,Company_city_ratecard,Company_outstation_ratecard,Company_airport_ratecard

#Register your models here.


#-----------------------------------

admin.site.register(City)
admin.site.register(Slab)
admin.site.register(Vendortype)
admin.site.register(Companytype)
admin.site.register(Vehicle_varient)

#----------------------------------
admin.site.register(Servicetype)
admin.site.register(Billingbase)
admin.site.register(Category)
admin.site.register(Travelservicetype)

#---------------------------------

admin.site.register(Bookingstatus)

admin.site.register(Dutyslipstatus)

admin.site.register(Invoicestatus)

#--------------------------------
admin.site.register(Location)
admin.site.register(Vendor)
admin.site.register(Vehicle)
admin.site.register(Chauffeur)
admin.site.register(Company)
#--------------------------------------

admin.site.register(Airport_ratecard)
admin.site.register(Outstation_ratecard)
admin.site.register(City_ratecard)

admin.site.register(Company_airport_ratecard)
admin.site.register(Company_outstation_ratecard)
admin.site.register(Company_city_ratecard)

#---------------------------------
#admin.site.register(Standered_rate_card)

#admin.site.register(Company_client_rate_card)

admin.site.register(Bookings)

admin.site.register(Dutyslip)

admin.site.register(ClientInvoice)
admin.site.register(VendorInvoice)
