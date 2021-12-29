from rest_framework import serializers

from rapido.models import User,City,Slab,Vendortype,Bookingstatus,Dutyslipstatus,Invoicestatus,Servicetype,Billingbase,Companytype,Travelservicetype,Vehicle_varient,Category,Company_booker,Chauffeur_vehicel,Smsforothers,Billingsummary

from rapido.models import Location,Vendor,Vehicle,Chauffeur,Company,Bookings,Dutyslip,ClientInvoice,VendorInvoice,Bookingstatus,Dutyslipstatus,Invoicestatus,Billingbase,City_ratecard,Outstation_ratecard,Airport_ratecard,Company_city_ratecard,Company_outstation_ratecard,Company_airport_ratecard

# from .models import Standered_rate_card , Company_client_rate_card ,




#---------------------------------
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UsersubSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email')

#-----------------------------------------------------


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class CityfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = City
        fields = "__all__"

class CitysubSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id','name')

#-----------------------------------------------
class SlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slab
        fields = "__all__"
class SlabfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Slab
        fields = "__all__"
class SlabsubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slab
        fields = ('id','name')
#-----------------------------------------

class VendortypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendortype
        fields = "__all__"
class VendortypefullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Vendortype
        fields = "__all__"
class VendortypesubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendortype
        fields = ('id','name')
#--------------------------------------

class CompanytypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companytype
        fields = "__all__"
class CompanytypefullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Companytype
        fields = "__all__"
class CompanytypesubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companytype
        fields = ('id','name')
#----------------------------------

class  TravelservicetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travelservicetype
        fields = "__all__"
class  TravelservicetypefullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Travelservicetype
        fields = "__all__"
class TravelservicetypesubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travelservicetype
        fields = ('id','name')
#------------------------------------------

class Vehicle_varientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_varient
        fields = "__all__"

class Vehicle_varientsubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_varient
        fields = ('id','name')

#---------------------------------
class BookingstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookingstatus
        fields = "__all__"
class BookingstatusfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Bookingstatus
        fields = "__all__"
class BookingstatussubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookingstatus
        fields = ('id','name')
#---------------------------------
class DutyslipstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dutyslipstatus
        fields = "__all__"
class DutyslipstatusfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Dutyslipstatus
        fields = "__all__"
class DutyslipstatussubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dutyslipstatus
        fields = ('id','name')
#---------------------------------
class InvoicestatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoicestatus
        fields = "__all__"
class InvoicestatusfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Invoicestatus
        fields = "__all__"
class InvoicestatussubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoicestatus
        fields = ('id','name')

#----------CATEGORY Serializer ---------------------------

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class CategoryfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
class CategorysubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')
#-------------------------------------------

class ServicetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicetype
        fields = "__all__"
class ServicetypefullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Servicetype
        fields = "__all__"
class ServicetypesubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicetype
        fields = ('id','name')

#--------------------------------------------------------
class BillingbaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billingbase
        fields = "__all__"
class BillingbasefullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Billingbase
        fields = "__all__"
class BillingbasesubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billingbase
        fields = ('id','name')

#----- LOCATION SERIALIZER -------------------------------
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
class LocationfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Location
        fields = "__all__"
class LocationsubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id','city','state')

#------- VENDOR Serializer-------------------------------
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"
class VendorfullSerializer(serializers.ModelSerializer):
    vendor_address = LocationsubSerializer(read_only=False)
    vendor_type = VendortypesubSerializer(read_only=False)
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Vendor
        fields = "__all__"
class VendoraddSerializer(serializers.ModelSerializer):
    vendor_address = LocationSerializer(read_only=False)
    class Meta:
        model = Vendor
        fields = "__all__"

    def create(self, validated_data):
        address = validated_data.pop('vendor_address')
        vendor_address= Location.objects.create(**address)
        vendor = Vendor.objects.create(vendor_address=vendor_address,**validated_data)
        return vendor

    # def update(self,instance, validated_data):
    #     address = validated_data.pop('vendor_address')
    #     vendor_address= Location.objects.update(**address)
    #     vendor = validated_data.pop('validated_data')
    #     vendor = Vendor.objects.update(**validated_data)
    #     return vendor
class VendorsubSerializer(serializers.ModelSerializer):
    vendor_address = LocationsubSerializer(read_only=False)
    vendor_type = VendortypesubSerializer(read_only=False)
    
    class Meta:
        model = Vendor
        fields = ('id','vendor_name','vendor_phoneno','vendor_type','vendor_address')

# ---------VEHICLE SERIALIZER---------------------------
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
class VehiclefullSerializer(serializers.ModelSerializer):
    category = CategorysubSerializer(read_only=False)
    vehicle_belongsto = VendorsubSerializer(read_only=False)
    created_by = UsersubSerializer(read_only=True)
    updated_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Vehicle
        fields = "__all__"

# ---------Chauffeurs SERIALIZER---------------------------
class ChauffeuraddSerializer(serializers.ModelSerializer):
    chauffeur_address = LocationSerializer(read_only=False)
    class Meta:
        model = Chauffeur
        fields = "__all__"

    def create(self, validated_data):
        address = validated_data.pop('chauffeur_address')
        chauffeur_address= Location.objects.create(**address)
        chauffeur = Chauffeur.objects.create(chauffeur_address=chauffeur_address,**validated_data)
        return chauffeur
class ChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = "__all__"
class ChauffeurfullSerializer(serializers.ModelSerializer):
    chauffeur_address = LocationsubSerializer(read_only=True)
    chauffeur_belongsto = VendorsubSerializer(read_only=True)
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    class Meta:
        model = Chauffeur
        fields = "__all__"

# ---------COMPANY-SERIALIZER---------------------------
class CompanyaddSerializer(serializers.ModelSerializer):
    company_address = LocationSerializer(read_only=False)
    user = UserSerializer(read_only=False)
    class Meta:
        model = Company
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop('user')
        user=User.objects.create(**user)
        user.set_password("abc123")
        user.save()
        address = validated_data.pop('company_address')
        company_address = Location.objects.create(**address)
        company = Company.objects.create(user=user,company_address=company_address,**validated_data)
        return company
class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = "__all__"
class CompanyfullSerializer(serializers.ModelSerializer):
    company_address = LocationsubSerializer(read_only=True)
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    company_type = CompanytypesubSerializer(read_only=True)
    Travelservicetype=TravelservicetypesubSerializer(read_only=True)
    user = UsersubSerializer(read_only=True)
    class Meta:
        model = Company
        fields = "__all__"

# ---------Standered_Rate_Card---------------------------

class Airport_ratecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport_ratecard
        fields = "__all__"

class Airport_ratecardfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    category = CategorysubSerializer(read_only=True)
    city= CitysubSerializer(read_only=True)
    service_type = TravelservicetypesubSerializer(read_only=True)
    class Meta:
        model = Airport_ratecard
        fields = "__all__"

# ---------Standered_Rate_Card---------------------------

class Outstation_ratecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outstation_ratecard
        fields = "__all__"

class Outstation_ratecardfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    category = CategorysubSerializer(read_only=True)
    city= CitysubSerializer(read_only=True)
    service_type = TravelservicetypesubSerializer(read_only=True)
    class Meta:
        model = Outstation_ratecard
        fields = "__all__"

# ---------Standered_Rate_Card---------------------------

class City_ratecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = City_ratecard
        fields = "__all__"

class City_ratecardfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    category = CategorysubSerializer(read_only=True)
    city= CitysubSerializer(read_only=True)
    service_type = TravelservicetypesubSerializer(read_only=True)
    slab= SlabsubSerializer(read_only=True)
    class Meta:
        model = City_ratecard
        fields = "__all__"

#---------------------------------------------------------------------

class Company_airport_ratecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_airport_ratecard
        fields = "__all__"
class Company_airport_ratecardfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    category = CategorysubSerializer(read_only=True)
    city= CitysubSerializer(read_only=True)
    service_type = TravelservicetypesubSerializer(read_only=True)
    class Meta:
        model = Company_airport_ratecard
        fields = "__all__"

class Company_outstation_ratecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_outstation_ratecard
        fields = "__all__"
class Company_outstation_ratecardfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    category = CategorysubSerializer(read_only=True)
    city= CitysubSerializer(read_only=True)
    service_type = TravelservicetypesubSerializer(read_only=True)
    class Meta:
        model = Company_outstation_ratecard
        fields = "__all__"

class Company_city_ratecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_city_ratecard
        fields = "__all__"
class Company_city_ratecardfullSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    update_by = UsersubSerializer (read_only=True)
    category = CategorysubSerializer(read_only=True)
    city= CitysubSerializer(read_only=True)
    service_type = TravelservicetypesubSerializer(read_only=True)
    slab= SlabsubSerializer(read_only=True)
    class Meta:
        model = Company_city_ratecard
        fields = "__all__"


# --------- BOOKINGS ---------------------------
class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = "__all__"


class BookingsfullSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)
    servicetype=ServicetypeSerializer(read_only=True)
    status=BookingstatusSerializer(read_only=False)
    class Meta:
        model = Bookings
        fields = "__all__"


# --------- Duty-SLip ---------------------------

class DutyslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dutyslip
        fields = "__all__"

class DutyslipfullSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=False)
    booking= BookingsSerializer(read_only=False)
    vendor= VendorSerializer(read_only=True)
    status= DutyslipstatusSerializer(read_only=False)
    class Meta:
        model = Dutyslip
        fields = "__all__"

# --------- Invoice ---------------------------


class ClientInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInvoice
        fields = "__all__"

class ClientInvoicefullSerializer(serializers.ModelSerializer):
    booking= BookingsSerializer(read_only=False)
    dutyslip= DutyslipSerializer(read_only=True)
    class Meta:
        model = ClientInvoice
        fields = "__all__"


class VendorInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorInvoice
        fields = "__all__"

class VendorInvoicefullSerializer(serializers.ModelSerializer):
    booking= BookingsSerializer(read_only=False)
    dutyslip= DutyslipSerializer(read_only=True)
    class Meta:
        model = VendorInvoice
        fields = "__all__"


#---------------------------------------------------


class Vendorsub1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id','vendor_name')


class Company_bookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_booker
        fields = "__all__"

class Chauffeur_vehicelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur_vehicel
        fields = "__all__"

class Chauffeur_vehicelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur_vehicel
        fields = "__all__"

class Chauffeur_vehicelsubSerializer(serializers.ModelSerializer):
    vendor= Vendorsub1Serializer(read_only=False)
    class Meta:
        model = Chauffeur_vehicel
        fields = ('vendor','id','vehicle_no','vehicle_modelname','vehicle_colour','chauffeur_name','chauffeur_phoneno','chauffeur_drivinglicense')


#-------------------------

class SmsforothersSerializer(serializers.ModelSerializer):
    created_by = UsersubSerializer(read_only=True)
    class Meta:
        model = Smsforothers
        fields = "__all__"

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billingsummary
        fields = "__all__"