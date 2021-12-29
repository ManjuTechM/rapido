from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers, viewsets, routers

from rapido.models import City,Slab,Vendortype,Bookingstatus,Dutyslipstatus,Invoicestatus,Servicetype,Billingbase,Companytype,Travelservicetype,Vehicle_varient,Category,Vendortype ,Company_booker,Chauffeur_vehicel ,Smsforothers,Billingsummary

from rapido.models import Location,Vendor,Vehicle,Chauffeur,Company,Bookings,Dutyslip,ClientInvoice,VendorInvoice,Bookingstatus,Dutyslipstatus,Invoicestatus,Billingbase,City_ratecard,Outstation_ratecard,Airport_ratecard,Company_city_ratecard,Company_outstation_ratecard,Company_airport_ratecard

from .serializers import CitySerializer,CityfullSerializer,SlabSerializer,SlabfullSerializer,ServicetypeSerializer,ServicetypefullSerializer,VendortypeSerializer,VendortypefullSerializer,Vehicle_varientSerializer,Airport_ratecardfullSerializer,Airport_ratecardSerializer,Outstation_ratecardfullSerializer,City_ratecardfullSerializer,Company_airport_ratecardSerializer,Company_outstation_ratecardSerializer,Company_city_ratecardSerializer,BookingsSerializer,Outstation_ratecardSerializer, Company_outstation_ratecardfullSerializer,Company_airport_ratecardfullSerializer,Company_city_ratecardfullSerializer


from .serializers import UserSerializer, CategorySerializer,City_ratecardSerializer,CategoryfullSerializer,LocationSerializer,VendorSerializer,VehicleSerializer,ChauffeurSerializer,CompanySerializer,VehiclefullSerializer,VendorfullSerializer,ClientInvoiceSerializer,VendorInvoiceSerializer,Chauffeur_vehicelsubSerializer,SmsforothersSerializer,BillingSerializer

from .serializers import BookingstatusSerializer,BookingstatusfullSerializer,CompanytypeSerializer,CompanytypefullSerializer,DutyslipSerializer,DutyslipstatusSerializer,DutyslipstatusfullSerializer,InvoicestatusSerializer,InvoicestatusfullSerializer,TravelservicetypeSerializer,TravelservicetypefullSerializer ,BillingbaseSerializer,BillingbasefullSerializer,ChauffeurfullSerializer,CompanyfullSerializer

from .serializers import VendoraddSerializer,ChauffeuraddSerializer,CompanyaddSerializer,Company_bookerSerializer,Chauffeur_vehicelSerializer



class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.ListCreateAPIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------CITY----------------------
class Citycreate(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = City.objects.all()
    serializer_class = CitySerializer
class CityList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = City.objects.all()
    serializer_class = CityfullSerializer
class CityDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = City.objects.all()
    serializer_class = CityfullSerializer
class Cityupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = City.objects.all()
    serializer_class = CitySerializer
class CityDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = City.objects.all()
    serializer_class = CitySerializer

#-----------slab------------------
class Slabcreate(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Slab.objects.all()
    serializer_class = SlabSerializer
class SlabList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Slab.objects.all()
    serializer_class = SlabfullSerializer
class SlabDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Slab.objects.all()
    serializer_class = SlabfullSerializer
class Slabupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Slab.objects.all()
    serializer_class = SlabSerializer
class SlabDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Slab.objects.all()
    serializer_class = SlabSerializer

#------------Vendor Type -----
class Vendortypecreate(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Vendortype.objects.all()
    serializer_class = VendortypeSerializer
class VendortypeList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Vendortype.objects.all()
    serializer_class = VendortypefullSerializer
class VendortypeDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Vendortype.objects.all()
    serializer_class = VendortypefullSerializer
class Vendortypeupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Vendortype.objects.all()
    serializer_class = VendortypeSerializer
class VendortypeDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Vendortype.objects.all()
    serializer_class = VendortypefullSerializer

#------------Service type -----
class Servicetypecreate(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Servicetype.objects.all()
    serializer_class = ServicetypeSerializer
class ServicetypeList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Servicetype.objects.all()
    serializer_class = ServicetypefullSerializer
class ServicetypeDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Servicetype.objects.all()
    serializer_class = ServicetypefullSerializer
class Servicetypeupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Servicetype.objects.all()
    serializer_class = ServicetypeSerializer
class ServicetypeDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Servicetype.objects.all()
    serializer_class = ServicetypeSerializer

#-----------BOOKING STATUS------------
class Bookingstatuscreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Bookingstatus.objects.all()
    serializer_class = BookingstatusSerializer
class BookingstatusList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Bookingstatus.objects.all()
    serializer_class = BookingstatusfullSerializer
class BookingstatusDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Bookingstatus.objects.all()
    serializer_class = BookingstatusfullSerializer
class Bookingstatusupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Bookingstatus.objects.all()
    serializer_class = BookingstatusSerializer
class BookingstatusDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Bookingstatus.objects.all()
    serializer_class = BookingstatusSerializer

#----- DUTYSLIP STATUS-----------------------------
class Dutyslipstatuscreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Dutyslipstatus.objects.all()
    serializer_class = DutyslipstatusSerializer
class DutyslipstatusList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Dutyslipstatus.objects.all()
    serializer_class = DutyslipstatusfullSerializer
class DutyslipstatusDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Dutyslipstatus.objects.all()
    serializer_class = DutyslipstatusfullSerializer
class Dutyslipstatusupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Dutyslipstatus.objects.all()
    serializer_class = DutyslipstatusSerializer
class DutyslipstatusDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Dutyslipstatus.objects.all()
    serializer_class = DutyslipstatusSerializer

#---------- Invoice status ----------------
class Invoicestatuscreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Invoicestatus.objects.all()
    serializer_class = InvoicestatusSerializer
class InvoicestatusList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Invoicestatus.objects.all()
    serializer_class = InvoicestatusfullSerializer
class InvoicestatusDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Invoicestatus.objects.all()
    serializer_class = InvoicestatusfullSerializer
class Invoicestatusupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Invoicestatus.objects.all()
    serializer_class = InvoicestatusSerializer
class InvoicestatusDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Invoicestatus.objects.all()
    serializer_class = InvoicestatusSerializer

#---------- Billing Base ----------------
class Billingbasecreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Billingbase.objects.all()
    serializer_class = BillingbaseSerializer
class BillingbaseList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Billingbase.objects.all()
    serializer_class = BillingbasefullSerializer
class BillingbaseDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Billingbase.objects.all()
    serializer_class = BillingbasefullSerializer
class Billingbaseupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Billingbase.objects.all()
    serializer_class = BillingbaseSerializer
class BillingbaseDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Billingbase.objects.all()
    serializer_class = BillingbaseSerializer

#---------- Company Type----------------
class Companytypecreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Companytype.objects.all()
    serializer_class = CompanytypeSerializer
class CompanytypeList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Companytype.objects.all()
    serializer_class = CompanytypefullSerializer
class CompanytypeDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Travelservicetype.objects.all()
    serializer_class = TravelservicetypefullSerializer
class Companytypeupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Travelservicetype.objects.all()
    serializer_class = TravelservicetypeSerializer
class CompanytypeDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Companytype.objects.all()
    serializer_class = TravelservicetypeSerializer

#---------- Company service Type----------------
class Travelservicetypecreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Travelservicetype.objects.all()
    serializer_class = TravelservicetypeSerializer
class TravelservicetypeList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Travelservicetype.objects.all()
    serializer_class = TravelservicetypefullSerializer
class TravelservicetypeDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Travelservicetype.objects.all()
    serializer_class = TravelservicetypefullSerializer
class Travelservicetypeupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Travelservicetype.objects.all()
    serializer_class = TravelservicetypeSerializer
class TravelservicetypeDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Travelservicetype.objects.all()
    serializer_class = TravelservicetypeSerializer

#---------- Category MODEL --------------------
class Categorycreate(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Category.objects.all()
    serializer_class = CategoryfullSerializer
class CategoryDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Category.objects.all()
    serializer_class = CategoryfullSerializer
class Categoryupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#-----------Vehicle MOdels---------

class Vehicle_varientList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Vehicle_varient.objects.all()
    serializer_class = Vehicle_varientSerializer
class Vehicle_varientDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Vehicle_varient.objects.all()
    serializer_class = Vehicle_varientSerializer
class Vehicle_varientDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Vehicle_varient.objects.all()
    serializer_class = Vehicle_varientSerializer

#---------- Location MODEL --------------------
class LocationList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
class LocationDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
class LocationDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

#---------- VENDOR MODEL ------
class Vendoradd(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Vendor.objects.all()
    serializer_class = VendoraddSerializer
class Vendorcreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
class VendorList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Vendor.objects.all()
    serializer_class = VendorfullSerializer
class VendorDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Vendor.objects.all()
    serializer_class = VendorfullSerializer
class Vendorupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
class VendorDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

#------------Full serialize VEHICLES MODEL ------------------
class VehicleList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Vehicle.objects.all()
    serializer_class = VehiclefullSerializer
class VehicleDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Vehicle.objects.all()
    serializer_class = VehiclefullSerializer
class Vehiclecreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
class Vehicleupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
class VehicleDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

#---------- CHAUFFEUR MODEL-----------------------
class Chauffeuradd(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeuraddSerializer
class Chauffeurcreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurSerializer
class ChauffeurList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurfullSerializer
class ChauffeurDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurfullSerializer
class Chauffeurupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurSerializer
class ChauffeurDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurSerializer

#------------COMPANY MODELS --------------------
class Companyadd(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Company.objects.all()
    serializer_class = CompanyaddSerializer
class Companycreate(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class CompanyList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Company.objects.all()
    serializer_class = CompanyfullSerializer
class CompanyDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Company.objects.all()
    serializer_class = CompanyfullSerializer
class Companyupdate(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class CompanyDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

#------------Standered Rate Card MODELS --------------------

class Airport_ratecardadd(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Airport_ratecard.objects.all()
    serializer_class = Airport_ratecardSerializer
class Airport_ratecardList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Airport_ratecard.objects.all()
    serializer_class = Airport_ratecardfullSerializer
class Airport_ratecardDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Airport_ratecard.objects.all()
    serializer_class = Airport_ratecardfullSerializer
class Airport_ratecardDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Airport_ratecard.objects.all()
    serializer_class = Airport_ratecardfullSerializer

class AirportratecardcityList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Airport_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        queryset=Airport_ratecard.objects.filter(city_id=city)
        return queryset
class AirportpriceDetail(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Airport_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        category= self.kwargs['category_id']
        queryset=Airport_ratecard.objects.filter(city_id=city,category_id=category)
        return queryset


#----------------------------------------------------

class Outstation_ratecardadd(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Outstation_ratecard.objects.all()
    serializer_class = Outstation_ratecardSerializer
class Outstation_ratecardList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Outstation_ratecard.objects.all()
    serializer_class = Outstation_ratecardfullSerializer
class Outstation_ratecardDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Outstation_ratecard.objects.all()
    serializer_class = Outstation_ratecardfullSerializer
class Outstation_ratecardDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Outstation_ratecard.objects.all()
    serializer_class = Outstation_ratecardfullSerializer

class OutstationratecardcityList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Outstation_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        queryset=Outstation_ratecard.objects.filter(city_id=city)
        return queryset
class OutstationpriceDetail(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Outstation_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        category= self.kwargs['category_id']
        queryset=Outstation_ratecard.objects.filter(city_id=city,category_id=category)
        return queryset

#--------------------------------------------------------

class City_ratecardadd(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = City_ratecard.objects.all()
    serializer_class = City_ratecardSerializer
class City_ratecardList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = City_ratecard.objects.all()
    serializer_class = City_ratecardfullSerializer
class City_ratecardDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = City_ratecard.objects.all()
    serializer_class = City_ratecardfullSerializer
class City_ratecardDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = City_ratecard.objects.all()
    serializer_class = City_ratecardfullSerializer

class CityratecardcityList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = City_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        queryset=City_ratecard.objects.filter(city_id=city)
        return queryset

class CitypriceDetail(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = City_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        category= self.kwargs['category_id']
        queryset=City_ratecard.objects.filter(city_id=city,category_id=category)
        return queryset


#-----------------------Company Rate Card ----------

class Company_airport_ratecardadd(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Company_airport_ratecard.objects.all()
    serializer_class = Company_airport_ratecardSerializer
class Company_airport_ratecardList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Company_airport_ratecard.objects.all()
    serializer_class = Company_airport_ratecardfullSerializer
class Company_airport_ratecardDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Company_airport_ratecard.objects.all()
    serializer_class = Company_airport_ratecardfullSerializer
class Company_airport_ratecardDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Company_airport_ratecard.objects.all()
    serializer_class = Company_airport_ratecardSerializer

class Company_airportratecardcityList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class =Company_airport_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        company = self.kwargs['company_id']
        queryset= Company_airport_ratecard.objects.filter(city_id=city,company_id=company)
        return queryset
class Company_airportpriceDetail(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Company_airport_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        category= self.kwargs['category_id']
        company = self.kwargs['company_id']
        queryset=Company_airport_ratecard.objects.filter(city_id=city,category_id=category,company_id=company)
        return queryset


class Company_outstation_ratecardadd(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Company_outstation_ratecard.objects.all()
    serializer_class = Company_outstation_ratecardSerializer

class Company_outstation_ratecardList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Company_outstation_ratecard.objects.all()
    serializer_class = Company_outstation_ratecardfullSerializer
class Company_outstation_ratecardDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Company_outstation_ratecard.objects.all()
    serializer_class = Company_outstation_ratecardfullSerializer
class Company_outstation_ratecardDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Company_outstation_ratecard.objects.all()
    serializer_class = Company_outstation_ratecardSerializer

class Company_outstationratecardcityList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class =  Company_outstation_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        company = self.kwargs['company_id']
        queryset=Company_outstation_ratecard.objects.filter(city_id=city,company_id=company)
        return queryset
class Company_outstationpriceDetail(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Company_outstation_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        category= self.kwargs['category_id']
        company = self.kwargs['company_id']
        queryset=Company_outstation_ratecard.objects.filter(city_id=city,category_id=category,company_id=company)
        return queryset


class Company_city_ratecardadd(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Company_city_ratecard.objects.all()
    serializer_class = Company_city_ratecardSerializer

class Company_city_ratecardList(generics.ListCreateAPIView):
    # Get / Update a Choice
    queryset = Company_city_ratecard.objects.all()
    serializer_class = Company_city_ratecardfullSerializer
class Company_city_ratecardDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Company_city_ratecard.objects.all()
    serializer_class = Company_city_ratecardfullSerializer
class Company_city_ratecardDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Company_city_ratecard.objects.all()
    serializer_class = Company_city_ratecardfullSerializer

class Company_cityratecardcityList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Company_city_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        company = self.kwargs['company_id']
        queryset=Company_city_ratecard.objects.filter(city_id=city,company_id=company)
        return queryset

class Company_citypriceDetail(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Company_city_ratecardfullSerializer
    def get_queryset(self):
        city=self.kwargs['city_id']
        category= self.kwargs['category_id']
        company = self.kwargs['company_id']
        queryset=Company_city_ratecard.objects.filter(city_id=city,category_id=category,company_id=company)
        return queryset


#------------Bookings MODELS --------------------

class BookingsList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer

class BookingsDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer

class BookingsDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer

#------------Duty_slip MODELS --------------------

class DutyslipList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Dutyslip.objects.all()
    serializer_class = DutyslipSerializer

class DutyslipDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Dutyslip.objects.all()
    serializer_class = DutyslipSerializer

class DutyslipDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Dutyslip.objects.all()
    serializer_class = DutyslipSerializer


#------------Invoice MODELS --------------------
class ClientInvoiceList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = ClientInvoice.objects.all()
    serializer_class = ClientInvoiceSerializer

class ClientInvoiceDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = ClientInvoice.objects.all()
    serializer_class = ClientInvoiceSerializer

class InvoiceDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = ClientInvoice.objects.all()
    serializer_class = ClientInvoiceSerializer



class VendorInvoiceList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = VendorInvoice.objects.all()
    serializer_class = VendorInvoiceSerializer

class VendorInvoiceDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = VendorInvoice.objects.all()
    serializer_class = VendorInvoiceSerializer

class VendorInvoiceDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = VendorInvoice.objects.all()
    serializer_class = VendorInvoiceSerializer



class CompanybookerList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Company_booker.objects.all()
    serializer_class = Company_bookerSerializer

class CompanybookerDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Company_booker.objects.all()
    serializer_class = Company_bookerSerializer

class CompanybookerDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Company_booker.objects.all()
    serializer_class = Company_bookerSerializer

class CompanybookerList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Company_bookerSerializer
    def get_queryset(self):
        company = self.kwargs['company_id']
        queryset=Company_booker.objects.filter(company_id=company)
        return queryset

#=====Chauffeur_vehicelSerializer=========

class Chauffeur_vehicelList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Chauffeur_vehicel.objects.all()
    serializer_class = Chauffeur_vehicelSerializer

class Chauffeur_vehicelDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Chauffeur_vehicel.objects.all()
    serializer_class = Chauffeur_vehicelSerializer

class Chauffeur_vehicelDelete(generics.RetrieveDestroyAPIView):
    # Get / Delete questions
    queryset = Chauffeur_vehicel.objects.all()
    serializer_class = Chauffeur_vehicelSerializer

class Chauffeur_vehicelby_vendorList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = Chauffeur_vehicelsubSerializer
    def get_queryset(self):
        vendor = self.kwargs['vendor_id']
        queryset=Chauffeur_vehicel.objects.filter(vendor_id=vendor)
        return queryset

class ChauffeurvehicelList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Chauffeur_vehicel.objects.all()
    serializer_class = Chauffeur_vehicelsubSerializer


#================== SMS for Others ===============

class SmsforothersList(generics.ListCreateAPIView):
    # Get / Create questions
    serializer_class = SmsforothersSerializer
    def get_queryset(self):
        booking_id = self.kwargs['booking_id']
        queryset=Smsforothers.objects.filter(booking_id=booking_id)
        return queryset


#------------old invoice--------------------

class BillingList(generics.ListCreateAPIView):
    # Get / Create questions
    queryset = Billingsummary.objects.all()
    serializer_class = BillingSerializer

class BillingDetail(generics.RetrieveUpdateAPIView):
    # Get / Update a Choice
    queryset = Billingsummary.objects.all()
    serializer_class = BillingSerializer
