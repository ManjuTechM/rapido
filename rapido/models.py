from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime

#-----------------------------------

class City(models.Model):
    name = models.CharField(max_length=128,unique=True)
    is_active= models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="city_created")
    updated_date= models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="city_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)
    city_code = models.CharField(max_length=128,blank=True,null=True)

    class Meta:
        db_table="City"

	def __unicode__(self):
		return self.name

class Slab(models.Model):
	name=models.CharField(max_length=128)
	is_active= models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,related_name="slab_created")
	updated_date= models.DateTimeField(blank=True, null=True)
	updated_by = models.ForeignKey(User,related_name="slab_updated", blank=True, null=True)
	created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
	updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		db_table="Slab"
	def __unicode__(self):
		return self.name

class Vendortype(models.Model):
	name=models.CharField(max_length=128)
	is_active= models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,related_name="vendortype_created")
	updated_date= models.DateTimeField(blank=True, null=True)
	updated_by = models.ForeignKey(User,related_name="vendortype_updated", blank=True, null=True)
	created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
	updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		db_table="Vendortype"
	def __unicode__(self):
		return self.name

class Companytype(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_date =models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="companytype_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="companytype_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Companytype"

    def __unicode__(self):
        return self.name

class Vehicle_varient(models.Model):
	name=models.CharField(max_length=128)
	created_date = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,related_name="cabname_created")
	updated_date= models.DateTimeField( blank=True, null=True)
	updated_by = models.ForeignKey(User,related_name="cabname_updated", blank=True, null=True)
	created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
	updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		db_table="Vehicle_varient"
	def __unicode__(self):
		return self.name

#------------------------------------------

class Bookingstatus(models.Model):
	name=models.CharField(max_length=128)
	is_active= models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,related_name="bookingstatus_created")
	updated_date= models.DateTimeField(blank=True, null=True)
	updated_by = models.ForeignKey(User,related_name="bookingstatus_updated", blank=True, null=True)
	created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
	updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		db_table="Bookingstatus"

	def __unicode__(self):
		return self.name

class Dutyslipstatus(models.Model):
	name=models.CharField(max_length=128)
	is_active= models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,related_name="sutyslipstatus_created")
	updated_date= models.DateTimeField( blank=True, null=True)
	updated_by = models.ForeignKey(User,related_name="sutyslipstatus_updated", blank=True, null=True)
	created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
	updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		db_table="Dutyslipstatus"
	def __unicode__(self):
		return self.name

class Invoicestatus(models.Model):
	name=models.CharField(max_length=128)
	is_active=models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,related_name="invoicestatus_created")
	updated_date= models.DateTimeField( blank=True, null=True)
	updated_by = models.ForeignKey(User,related_name="invoicestatus_updated", blank=True, null=True)
	created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
	updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		db_table="Invoicestatus"
	def __unicode__(self):
		return self.name


#-------- Type of services------------------

class Servicetype(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_date =models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="service_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="service_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Servicetype"

    def __unicode__(self):
        return self.name

# Billing Base
class Billingbase(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_date =models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="billbase_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="billbase_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Billingbase"

    def __unicode__(self):
        return self.name

class Travelservicetype(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_date =models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="company_servicetype_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="company_servicetype_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Travelservicetype"

    def __unicode__(self):
        return self.name

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    picture = models.ImageField(upload_to='category_pics',blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="category_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="category_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Category"

    def __unicode__(self):
        return self.name


#-------------------------------------------

# Address
class Location(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="location_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="location_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)
    street_address=models.CharField(max_length=200,blank=True, null=True)
    landmark= models.CharField(max_length=128)
    area = models.CharField(max_length=128)
    city= models.CharField(max_length=128)
    state=models.CharField(max_length=128)
    country=models.CharField(max_length=128,default="India")
    pincode = models.IntegerField()

	# class Meta:
	# 	db_table="Location"

    def __unicode__(self):
        return self.city
			

# vendor details
class Vendor(models.Model):
    vendor_type = models.ForeignKey(Vendortype)
    vendor_name = models.CharField(max_length=128)
    vendor_phoneno = models.CharField(max_length=10)
    vendor_email = models.EmailField(max_length=70,unique=True)
    vendor_picture = models.ImageField(upload_to='vendor_documents',blank=True, null=True)
    vendor_joined_date = models.DateField(null=True)
    vendor_payment_type=models.CharField(max_length=20,blank=True, null=True)
    vendor_agreement_start_date=models.DateField()
    vendor_agreement_end_date= models.DateField()
    vendor_documents = models.FileField(upload_to='vendor_documents', blank=True, null=True)
    bank_name= models.CharField(max_length=100, blank=True, null=True)
    beneficiary_account_name=models.CharField(max_length=50, blank=True, null=True)
    accountno=models.CharField(max_length=20, blank=True, null=True)
    ifsc = models.CharField(max_length=10, blank=True, null=True)
    vendor_address = models.ForeignKey(Location)
    is_active = models.BooleanField(default=False)
    remarks= models.CharField(max_length=200,default="nothing")

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="vendor_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="vendor_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Vendor"
            unique_together=(("vendor_name","vendor_email"),)

    def __unicode__(self):
        return self.vendor_name

# car details
class Vehicle(models.Model):
    vehicle_belongsto = models.ForeignKey(Vendor)
    vehicle_modelname = models.ForeignKey(Vehicle_varient)
    vehicle_no = models.CharField(max_length=10,unique=True)
    vehicle_picture = models.ImageField(upload_to='vehicle_pics',blank=True, null=True)
    vehicle_colour=models.CharField(max_length=128,blank=True, null=True)
    vehicle_ownername = models.CharField(max_length=128,blank=True, null=True)
    vehicle_owner_phoneno = models.CharField(max_length=10,blank=True, null=True)
    seat_capacity = models.IntegerField()
    insurance_expire_date = models.DateField()
    tax_expire_date = models.DateField()
    vehicle_engine_no = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="vehicle_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="vehicle_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Vehicle"

    def __unicode__(self):
        return self.vehicle_no


class Chauffeur(models.Model):
    chauffeur_name = models.CharField(max_length=128)
    chauffeur_belongsto = models.ForeignKey(Vendor)
    chauffeur_phoneno = models.CharField(max_length=10,unique=True)
    chauffeur_picture = models.ImageField(upload_to='chaffeur_pics',default="chaffeur_pics/img_avatar3.png", blank=True)    
    chauffeur_drivinglicense = models.CharField(max_length=20)
    chauffeur_drivinglicense_expire_date = models.DateField()
    chauffeur_badgeno = models.CharField(max_length=10)
    chauffeur_badge_expired_date= models.DateField()
    chauffeur_address = models.ForeignKey(Location,blank=True, null=True)
    likes = models.IntegerField(default=0)
    ratings = models.IntegerField(blank=True,default=5)
    is_active = models.BooleanField(default=True)

    created_date =models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="chauufer_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="chauffer_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
            db_table="Chauffeur"
            unique_together=(("chauffeur_name","chauffeur_drivinglicense"),)

    def __unicode__(self):
        return self.chauffeur_phoneno

def increment_company_code():
    last_dutyslip = Company.objects.all().order_by('id').last()
    if not last_dutyslip:
        return 'RTIPL-CORP-' + '0000'
    dutyslip_id = last_dutyslip.company_code
    dutyslip_no = int(dutyslip_id[11:15])
    new_dutyslip_no = dutyslip_no + 1
    new_dutyslip_no = 'RITPL-CORP-'+ str(new_dutyslip_no).zfill(4)
    print new_dutyslip_no
    return new_dutyslip_no

class Company(models.Model):
    user = models.OneToOneField(User)
    company_name = models.CharField(max_length=128)
    company_type = models.ForeignKey(Companytype)
    company_logo = models.ImageField(null=True, blank=True, upload_to='company_documents')
    company_phoneno = models.CharField(max_length=15)
    company_email= models.EmailField(max_length=128)
    company_address= models.ForeignKey(Location)

    company_manager_name = models.CharField(max_length=128)
    company_manager_mobileno= models.CharField(max_length=10)
    company_manager_email= models.EmailField()

    company_payment_type = models.CharField(max_length=128)
    company_agreement_start_date = models.DateField()
    company_agreement_end_date = models.DateField()
    travelling_time_treshhold = models.IntegerField()
    status = models.BooleanField(default=False)
    company_documents=models.FileField(upload_to='company_documents', blank=True,null=True)
    remarks = models.CharField(max_length=200,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="company_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="company_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)
    gst = models.CharField(max_length=20,unique=True,blank=True,null=True)
    pan =models.CharField(max_length=20,unique=True, blank=True, null=True)
    company_code = models.CharField(max_length=20,default=increment_company_code,editable=False)
    class Meta:
            db_table="Company"

    def __unicode__(self):
        return self.company_name
		


#--------------------City rate card--------------------------

class Airport_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="airport_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="airport_ratecard_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    service_type = models.ForeignKey(Travelservicetype)
    base_rate = models.FloatField(default="0.0")
    
    class Meta:
    	db_table="Airport_ratecard"
    	unique_together=(("city","category"),)


class Outstation_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="outstation_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="outstation_ratecard_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    service_type = models.ForeignKey(Travelservicetype)

    min_km = models.FloatField(default="0.0")
    perkm_rate = models.FloatField(default="0.00")
    extrakm_rate = models.FloatField(default="0.00")
    day_batta = models.FloatField(default="0.00")
    night_batta = models.FloatField(default="0.00")
    class Meta:
    	db_table="Outstation_ratecard"
    	unique_together=(("city","category"),)


class City_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="city_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="city_ratecard_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    vehicle_varient= models.CharField(max_length=128, blank=True, null=True)
    service_type = models.ForeignKey(Travelservicetype)
    fgr = models.FloatField(default="0")

    slab = models.ForeignKey(Slab)
    base_rate = models.FloatField(default="0.0")
    extra_kmrate = models.FloatField(default="0.00")
    extra_hrrate = models.FloatField(default="0.00")
    night_batta = models.FloatField(default="0.00")

    class Meta:
    	db_table="City_ratecard"
    	unique_together=(("city","category","slab"),)
#-------------------------------------------------------------
class Company_city_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="company_city_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="company_city_ratecard_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    company=models.ForeignKey(Company)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    service_type = models.ForeignKey(Travelservicetype)
    fgr = models.FloatField(default="0")

    slab = models.ForeignKey(Slab)
    base_rate = models.FloatField(default="0.0")
    extra_kmrate = models.FloatField(default="0.00")
    extra_hrrate = models.FloatField(default="0.00")
    night_batta = models.FloatField(default="0.00")
    gst_no =  models.CharField(max_length=128,blank=True,null=True)
    
    class Meta:
    	db_table="Company_city_ratecard"
    	unique_together=(("company","city","category","slab"),)

class Company_outstation_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="company_outstation_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="company_outstation_ratecard_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    company=models.ForeignKey(Company)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    service_type = models.ForeignKey(Travelservicetype)

    min_km = models.FloatField(default="0.0")
    perkm_rate = models.FloatField(default="0.00")
    extrakm_rate = models.FloatField(default="0.00")
    day_batta = models.FloatField(default="0.00")
    night_batta = models.FloatField(default="0.00")
    gst_no =  models.CharField(max_length=128,blank=True,null=True)

    class Meta:
    	db_table="Company_outstation_ratecard"
    	unique_together=(("company" ,"city","category"),)


class Company_airport_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="company_airport_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="company_airport_ratecard_updated", blank=True, null=True)
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)
    company= models.ForeignKey(Company)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    service_type = models.ForeignKey(Travelservicetype)
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    base_rate = models.FloatField(default="0.0")
    gst_no =  models.CharField(max_length=128,blank=True,null=True)
    class Meta:
    	db_table="Company_airport_ratecard"
    	unique_together=(("company" ,"city","category"),)

#-------------------------------------------------------------


def increment_booking_number():
    last_booking = Bookings.objects.all().order_by('id').last()
    if not last_booking:
    	print '0000'
        return '0850'
    booking_id = last_booking.booking_id
    print booking_id
    booking_int = int(booking_id[0:5])
    print " booking_int"
    print booking_int
    new_booking_int = booking_int + 1
    new_booking_id  = str(new_booking_int).zfill(4)
    return new_booking_id


class Bookings(models.Model):
    booking_id = models.CharField(max_length=20,unique=True,default=increment_booking_number,editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="created_user")
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="updated_user", blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    service_type = models.ForeignKey(Servicetype)
    category = models.ForeignKey(Category)
    servicing_city = models.ForeignKey(City)

    booking_from = models.CharField(max_length=128, blank=True, null=True)
    booking_phoneno = models.CharField(max_length=10, blank=True, null=True)
    booking_email = models.EmailField(blank=True, null=True)
    guest_name = models.CharField(max_length=128)
    guest_gender = models.CharField(max_length=128)
    guest_phoneno = models.CharField(max_length=10)
    guest_email = models.EmailField(blank=True, null=True)
    pickup_date_time = models.DateTimeField(max_length=128)
    pick_up_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200, blank=True, null=True)
    requested_vehicle_model = models.CharField(max_length=128, blank=True, null=True)
    billing_base = models.ForeignKey(Billingbase)
    status = models.ForeignKey(Bookingstatus)
    comment = models.CharField(max_length=200,blank=True,null=True)
    remarks = models.CharField(max_length=200,blank=True,null=True)
    company = models.ForeignKey(Company,blank=True, null=True)
    emailcopy = models.ImageField(upload_to='email_copy',blank=True, null=True)

    class Meta:
        db_table="Bookings"


#----------------------------------------------------

def increment_dutyslip_number():
    last_dutyslip = Dutyslip.objects.all().order_by('id').last()
    if not last_dutyslip:
        return 'RDUTY' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2)+ '0000'
    dutyslip_id = last_dutyslip.dutyslip_id
    dutyslip_no = int(dutyslip_id[11:15])
    new_dutyslip_no = dutyslip_no + 1
    new_dutyslip_no = 'RDUTY' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2)+ str(datetime.date.today().day).zfill(2) + str(new_dutyslip_no).zfill(4)
    return new_dutyslip_no

class Dutyslip(models.Model):
    dutyslip_id = models.CharField(max_length=20,default=increment_dutyslip_number,editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="dutyslip_created")
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="dutyslip_updated", blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    booking = models.OneToOneField(Bookings)
    category =  models.ForeignKey(Category)
    vendor = models.ForeignKey(Vendor)

    allocated_vehicle = models.CharField(max_length=128)
    vehicle_colour = models.CharField(max_length=128)
    vehicle_no = models.CharField(max_length=128)
    chauffeur_name = models.CharField(max_length=128)
    chauffeur_phoneno = models.CharField(max_length=10)
    chauffeur_drivinglicense = models.CharField(max_length=128,blank=True, null=True)

    date_out = models.DateField(blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    total_days = models.FloatField(blank=True, null=True)
    
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    total_hrs = models.FloatField(blank=True, null=True)

    opening_km = models.FloatField(blank=True, null=True)
    closing_km = models.FloatField(blank=True, null=True)
    total_kms = models.FloatField(blank=True, null=True)

    point_opening_km = models.FloatField(blank=True, null=True)
    point_closing_km = models.FloatField(blank=True, null=True)
    total_point_kms = models.FloatField(blank=True, null=True)

    point_opening_hrs = models.TimeField(blank=True, null=True)
    point_closing_hrs = models.TimeField(blank=True, null=True)
    total_point_hrs = models.FloatField(blank=True, null=True)

    extra_hr = models.FloatField(blank=True, null=True)
    extra_km = models.FloatField(blank=True, null=True)

    package = models.CharField(max_length=128,blank=True, null=True)
    package_rate = models.FloatField(blank=True, null=True)
    extra_km_rate = models.FloatField(blank=True, null=True)
    extra_hr_rate = models.FloatField(blank=True, null=True)

    parking = models.FloatField(blank=True, null=True)
    itinerary = models.FloatField(blank=True, null=True)
    miscellaneous = models.FloatField(blank=True, null=True)

    gst_percentage = models.FloatField(blank=True, null=True)
    gst_Rs = models.FloatField( blank=True, null=True)
    discount = models.FloatField( blank=True, null=True)

    total_amount = models.FloatField( blank=True, null=True)
    status = models.ForeignKey(Dutyslipstatus)
    comment = models.CharField(max_length=128,blank=True, null=True)

    cgst_percentage= models.FloatField(blank=True,null=True)
    cgst_Rs = models.FloatField(blank=True, null= True)
    sgst_percentage = models.FloatField(blank=True,null=True)
    sgst_Rs = models.FloatField(blank=True,null=True)
    fgr = models.FloatField(blank=True,null=True)

    daybhatta = models.FloatField(blank=True,null=True)
    nightbhatta = models.FloatField(blank=True,null=True)
    subtotal = models.FloatField(blank=True,null=True)
    discount = models.FloatField(blank=True,null=True)
    extra_km_runrate = models.FloatField(blank=True, null=True)
    extra_hr_runrate = models.FloatField(blank=True, null=True)
    permit = models.FloatField(blank=True,null=True)

    amount_tobe_paid = models.FloatField(blank=True,null=True)
    km_used = models.FloatField(blank=True,null=True)
    hrs_used = models.FloatField(blank=True,null=True)

    class Meta:
		db_table="Dutyslip"
			
#----------------------------------------------------

class Bookingsms(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="bookingsms")
    created_by_ip_address = models.CharField(max_length=128, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="bookingsmsupdate", blank=True, null=True)
    updated_by_ip_address = models.CharField(max_length=128, blank=True, null=True)

    booking = models.OneToOneField(Bookings)

    emailsent = models.BooleanField(default =False)
    smssent = models.BooleanField(default = False)
    smsdelivery = models.BooleanField(default = False)
    status = models.CharField(max_length=128)

    class Meta:
        db_table="Bookingsms"

class Dutyslipsms(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="dutyslipsms")
    created_by_ip_address=models.CharField(max_length=128, blank=True, null=True)
    updated_date= models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="dutyslipsmsupdate", blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)
    dutyslip = models.OneToOneField(Dutyslip)

    emailsent = models.BooleanField(default =False)
    usersmssent = models.BooleanField(default = False)
    usersmsdelivery = models.BooleanField(default = False)
    userstatus = models.CharField(max_length=128,blank=True, null=True)

    driversmssent = models.BooleanField(default = False)
    driversmsdelivery = models.BooleanField(default = False)
    driverstatus = models.CharField(max_length=128, blank=True, null=True)
    class Meta:
        db_table="Dutyslipsms"

class Cancelsms(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="cancelsms")
    created_by_ip_address = models.CharField(max_length=128, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="cancelsmsupdate", blank=True, null=True)
    updated_by_ip_address = models.CharField(max_length=128, blank=True, null=True)

    booking = models.OneToOneField(Bookings)

    useremailsent = models.BooleanField(default =False)
    usersmssent = models.BooleanField(default = False)
    usersmsdelivery = models.BooleanField(default = False)
    userstatus = models.CharField(max_length=128,blank=True, null=True)

    driversmssent = models.BooleanField(default = False)
    driversmsdelivery = models.BooleanField(default = False)
    driverstatus = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table="Cancelsms"

class Company_booker(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="company_booker_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="company_booker_updated", blank=True, null=True)

    company=models.ForeignKey(Company)

    label = models.CharField(max_length=128, blank=True, null=True)
    booking_phoneno = models.CharField(max_length=10, blank=True, null=True)
    booking_email = models.EmailField(blank=True, null=True)

    class Meta:
        db_table="Company_booker"
        unique_together=(("company" ,"label","booking_phoneno"),)



#---------------------------------------

class Chauffeur_vehicel(models.Model):
    vendor = models.ForeignKey(Vendor)
    vehicle_no = models.CharField(max_length=20,unique=True)
    vehicle_modelname = models.CharField(max_length=128,blank=True, null=True)
    vehicle_colour=models.CharField(max_length=128,blank=True, null=True)
    # vehicle_ownername = models.CharField(max_length=128,blank=True, null=True)
    # vehicle_owner_phoneno = models.CharField(max_length=10,blank=True, null=True)
    seat_capacity = models.IntegerField()
    fcexpairy_date = models.DateField(blank=True,null=True) 
    tax_expire_date = models.DateField(blank=True,null=True)
    insurance_exp_date = models.DateField(blank=True,null=True)
    vehicle_engine_no = models.CharField(max_length=30,blank=True,null=True)
    puc_exp = models.DateField(blank=True,null=True)
    permit = models.CharField(max_length=128,blank=True,null=True)
    chauffeur_name = models.CharField(max_length=128,blank=True,null=True)
    chauffeur_phoneno = models.IntegerField(max_length=10)
    chauffeur_picture = models.ImageField(upload_to='chaffeur_pics',default="chaffeur_pics/img_avatar3.png",blank=True,null=True)
    chauffeur_drivinglicense = models.CharField(max_length=120,blank=True,null=True)
    chauffeur_drivinglicense_expire_date = models.DateField(blank=True,null=True)
    chauffeur_badgeno = models.CharField(max_length=128,blank=True,null=True)
    chauffeur_badge_expired_date= models.DateField(blank=True,null=True)
    chauffeur_address = models.CharField(max_length=250,blank=True,null=True)
    police_verification = models.CharField(max_length=128,blank=True,null=True)
    likes = models.IntegerField(default=0)
    ratings = models.IntegerField(blank=True,default=5)
    is_active = models.BooleanField(default=True)

    created_date =models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="chauufer_vehicle_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="chauffer_vehicle_updated", blank=True, null=True)
    created_by_ip_address= models.CharField(max_length=128, blank=True, null=True)
    updated_by_ip_address= models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table="Chauffeur_vehicel"
        unique_together=(("vendor" ,"vehicle_no","chauffeur_phoneno","chauffeur_name"),)

class Smsforothers(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="smsforothers")
    booking_id = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=10)
    message = models.CharField(max_length=300)
    emailsent = models.BooleanField(default =False)
    smssent = models.BooleanField(default = False)
    smsdelivery = models.BooleanField(default = False)
    status = models.CharField(max_length=128)

    class Meta:
        db_table="Smsforothers"


class Billingsummary(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField(unique=True,max_length=128)
    client_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128,blank=True,null=True)
    date_of_usage = models.DateField(blank=True,null=True) 
    date_out = models.DateField(blank=True,null=True) 
    date_in = models.DateField(blank=True,null=True) 
    city = models.CharField(max_length=128)
    duty_type = models.CharField(max_length=128,blank=True,null=True)
    vehicle_request = models.CharField(max_length=128,blank=True,null=True)
    h4_40_km_rate = models.IntegerField(max_length=128,blank=True,null=True)
    h8_80_KM_rate = models.IntegerField(max_length=128,blank=True,null=True)
    extra_hour_rate = models.IntegerField(max_length=128,blank=True,null=True)
    extra_km_rate = models.IntegerField(max_length=128,blank=True,null=True)
    outstation_min_km = models.IntegerField(max_length=128,blank=True,null=True)
    airport_trf_rate = models.FloatField(max_length=128,blank=True,null=True)
    km_out = models.IntegerField(max_length=128,blank=True,null=True)
    km_in = models.IntegerField(max_length=128,blank=True,null=True)
    total_km = models.FloatField(max_length=128,blank=True,null=True)
    time_out = models.FloatField(max_length=128,blank=True,null=True)
    time_in =  models.FloatField(max_length=128,blank=True,null=True)
    total_hour = models.FloatField(max_length=128,blank=True,null=True)
    slab_used = models.CharField(max_length=128,blank=True,null=True)
    extra_km_run = models.IntegerField(max_length=128,blank=True,null=True)
    extra_hr_run = models.FloatField(max_length=128,blank=True,null=True)
    base_slab_rate = models.FloatField(max_length=128,blank=True,null=True)
    extra_km_amt = models.FloatField(max_length=128,blank=True,null=True)
    extra_hr_amt = models.FloatField(max_length=128,blank=True,null=True)
    total_amount = models.FloatField(max_length=128,blank=True,null=True)
    parking_toll = models.FloatField(max_length=128,blank=True,null=True)
    interstate_tax = models.FloatField(max_length=128,blank=True,null=True)
    day_batta = models.FloatField(max_length=128,blank=True,null=True)
    night_batta = models.FloatField(max_length=128,blank=True,null=True)
    total = models.FloatField(max_length=128,blank=True,null=True)
    gst = models.FloatField(max_length=128,blank=True,null=True)
    total_bill_amount =models.FloatField(max_length=128,blank=True,null=True)
    vendor_type =  models.CharField(max_length=128,blank=True,null=True)
    vendor_name = models.CharField(max_length=128,blank=True,null=True)
    vehicle_no = models.CharField(max_length=128,blank=True,null=True)
    vendor_bill_no = models.CharField(max_length=128,blank=True,null=True)
    vbase_slab = models.FloatField(max_length=128,blank=True,null=True)
    vextra_km_amt = models.FloatField(max_length=128,blank=True,null=True)
    vextra_hr_amt = models.FloatField(max_length=128,blank=True,null=True)
    vtotal_amount =  models.FloatField(max_length=128,blank=True,null=True)
    vparking = models.FloatField(max_length=128,blank=True,null=True)
    vinterstate_tax = models.FloatField(max_length=128,blank=True,null=True)
    vbatta = models.FloatField(max_length=128,blank=True,null=True)
    vendorpayble_amt = models.FloatField(max_length=128,blank=True,null=True)
    our_margin_amt = models.FloatField(max_length=128,blank=True,null=True)
    margin_percentage = models.FloatField(max_length=128,blank=True,null=True)
    status = models.BooleanField(default=False)
    comment = models.CharField(max_length=128,blank=True, null=True)
    other_amt = models.FloatField(max_length=128,blank=True,null=True)
    no_of_days = models.CharField(max_length=128,blank=True,null=True)
    sgst = models.CharField(max_length=128,blank=True,null=True)
    cgst = models.CharField(max_length=128,blank=True,null=True)
    company_gst = models.CharField(max_length=128,blank=True,null=True)
    company_pan = models.CharField(max_length=128,blank=True,null=True)
    reporting_time = models.CharField(max_length=128,blank=True,null=True)
    billing_address = models.CharField(max_length=250,blank=True,null=True)
    city_used = models.CharField(max_length=128,blank=True,null=True)
    booked_by = models.CharField(max_length=128,blank=True,null=True)
    code = models.CharField(max_length=128,blank=True,null=True)
    pickup = models.CharField(max_length=128,blank=True,null=True)
    drop = models.CharField(max_length=128,blank=True,null=True)
    pickuptime = models.CharField(max_length=128,blank=True,null=True)
    drivername = models.CharField(max_length=128,blank=True,null=True)
    driver_phoneno = models.CharField(max_length=128,blank=True,null=True)
    guest_phoneno = models.CharField(max_length=128,blank=True,null=True)
    fgr = models.CharField(max_length=128,blank=True,null=True)

    class Meta:
        db_table="Billingsummary"

#================= vendor price list ================================

#-------------------------------------------------------------
class Vendor_city_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="vendor_city_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="vendor_city_ratecard_updated", blank=True, null=True)

    vendor=models.ForeignKey(Vendor)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    margin = models.FloatField(default="0.0")
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    service_type = models.ForeignKey(Travelservicetype)
    fgr = models.FloatField(default="0")

    slab = models.ForeignKey(Slab)
    base_rate = models.FloatField(default="0.0")
    extra_kmrate = models.FloatField(default="0.00")
    extra_hrrate = models.FloatField(default="0.00")
    night_batta = models.FloatField(default="0.00")
    gst_no =  models.CharField(max_length=128,blank=True,null=True)
    
    class Meta:
        db_table="Vendor_city_ratecard"
        unique_together=(("vendor","city","category","slab"),)

class Vendor_outstation_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="vendor_outstation_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="vendor_outstation_ratecard_updated", blank=True, null=True)

    vendor=models.ForeignKey(Vendor)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    margin = models.FloatField(default="0.0")
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    service_type = models.ForeignKey(Travelservicetype)

    min_km = models.FloatField(default="0.0")
    perkm_rate = models.FloatField(default="0.00")
    extrakm_rate = models.FloatField(default="0.00")
    day_batta = models.FloatField(default="0.00")
    night_batta = models.FloatField(default="0.00")
    gst_no =  models.CharField(max_length=128,blank=True,null=True)

    class Meta:
        db_table="Vendor_outstation_ratecard"
        unique_together=(("vendor" ,"city","category"),)


class Vendor_airport_ratecard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="vendor_airport_ratecard_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="vendor_airport_ratecard_updated", blank=True, null=True)
    vendor=models.ForeignKey(Vendor)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    service_type = models.ForeignKey(Travelservicetype)
    margin = models.FloatField(default="0.0")
    vehicle_varient= models.CharField(max_length=128,blank=True,null=True)
    base_rate = models.FloatField(default="0.0")
    gst_no =  models.CharField(max_length=128,blank=True,null=True)
    class Meta:
        db_table="Vendor_airport_ratecard"
        unique_together=(("vendor" ,"city","category"),)

#-------------------------------------------------------------
#---------------- CLient Invoice--------------------------------

class ClientInvoice(models.Model):
    # dutyslip_id = models.CharField(max_length=20,default=increment_dutyslip_number,editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="clientinvoice_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="clientinvoice_updated", blank=True, null=True)

    booking = models.OneToOneField(Bookings)
    dutyslip = models.OneToOneField(Dutyslip)

    package = models.CharField(max_length=128,blank=True, null=True)
    package_rate = models.FloatField(blank=True, null=True)

    fgr = models.FloatField(blank=True,null=True)

    km_used = models.FloatField(blank=True,null=True)
    hrs_used = models.FloatField(blank=True,null=True)

    extra_hr = models.FloatField(blank=True, null=True)
    extra_km = models.FloatField(blank=True, null=True)

    extra_hr_rate = models.FloatField(blank=True, null=True)
    extra_km_rate = models.FloatField(blank=True, null=True)

    extra_km_runrate = models.FloatField(blank=True, null=True)
    extra_hr_runrate = models.FloatField(blank=True, null=True)

    parking = models.FloatField(blank=True, null=True)
    itinerary = models.FloatField(blank=True, null=True)
    miscellaneous = models.FloatField(blank=True, null=True)

    daybhatta = models.FloatField(blank=True,null=True)
    nightbhatta = models.FloatField(blank=True,null=True)

    permit = models.FloatField(blank=True,null=True)

    subtotal = models.FloatField(blank=True,null=True)

    gst_percentage = models.FloatField(blank=True, null=True)
    gst_Rs = models.FloatField( blank=True, null=True)

    cgst_percentage= models.FloatField(blank=True,null=True)
    cgst_Rs = models.FloatField(blank=True, null= True)

    sgst_percentage = models.FloatField(blank=True,null=True)
    sgst_Rs = models.FloatField(blank=True,null=True)

    total_amount = models.FloatField( blank=True, null=True)

    discount = models.FloatField( blank=True, null=True)

    amount_tobe_paid = models.FloatField(blank=True,null=True)

    adminapproved = models.BooleanField(default=False)
    clientapproved = models.BooleanField(default=False)

    comment = models.CharField(max_length=128,blank=True, null=True)

    class Meta:
        db_table="ClientInvoice"
            

#---------------- Vendor Invoice--------------------------------

class VendorInvoice(models.Model):
    # dutyslip_id = models.CharField(max_length=20,default=increment_dutyslip_number,editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="vendorinvoice_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="vendorinvoice_updated", blank=True, null=True)

    booking = models.OneToOneField(Bookings)
    dutyslip = models.OneToOneField(Dutyslip)

    margin = models.FloatField(blank=True, null=True)

    package = models.CharField(max_length=128,blank=True, null=True)
    package_rate = models.FloatField(blank=True, null=True)

    fgr = models.FloatField(blank=True,null=True)

    km_used = models.FloatField(blank=True,null=True)
    hrs_used = models.FloatField(blank=True,null=True)

    extra_hr = models.FloatField(blank=True, null=True)
    extra_km = models.FloatField(blank=True, null=True)

    extra_hr_rate = models.FloatField(blank=True, null=True)
    extra_km_rate = models.FloatField(blank=True, null=True)

    extra_km_runrate = models.FloatField(blank=True, null=True)
    extra_hr_runrate = models.FloatField(blank=True, null=True)

    parking = models.FloatField(blank=True, null=True)
    itinerary = models.FloatField(blank=True, null=True)
    miscellaneous = models.FloatField(blank=True, null=True)

    daybhatta = models.FloatField(blank=True,null=True)
    nightbhatta = models.FloatField(blank=True,null=True)

    permit = models.FloatField(blank=True,null=True)

    subtotal = models.FloatField(blank=True,null=True)

    gst_percentage = models.FloatField(blank=True, null=True)
    gst_Rs = models.FloatField( blank=True, null=True)

    total_amount = models.FloatField( blank=True, null=True)

    amount_tobe_paid = models.FloatField(blank=True,null=True)

    adminapproved = models.BooleanField(default=False)
    vendorapproved = models.BooleanField(default=False)

    comment = models.CharField(max_length=128,blank=True, null=True)

    class Meta:
        db_table="VendorInvoice"
            
#----------------------------------------------------

class Batch(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="batch_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="batch_updated", blank=True, null=True)
    company=models.ForeignKey(Company)
    batch_name = models.CharField(max_length=128)
    no_of_invoice = models.IntegerField(max_length=128)
    class Meta:
        db_table="Batch"


class Invoice_batch(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="batch_invoice_created")
    updated_date= models.DateTimeField( blank=True, null=True)
    updated_by = models.ForeignKey(User,related_name="batch_invoice_updated", blank=True, null=True)
    batch = models.ForeignKey(Batch)
    invoice = models.ForeignKey(ClientInvoice)
    batch_name = models.CharField(max_length=128)
    no_of_invoice = models.IntegerField(max_length=128)
    class Meta:
        db_table="Invoice_batch"

