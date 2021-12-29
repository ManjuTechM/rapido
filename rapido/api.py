from django.contrib.auth.models import User
from rapido.models import Category , Airport_ratecard ,Outstation_ratecard, City_ratecard,Company_city_ratecard,Company_outstation_ratecard,Company_airport_ratecard,Smsforothers
from django.http import Http404
from django.http import HttpResponse
from rapido.serializers import UserSerializer
from .serializers import CategorySerializer,CompanySerializer,Airport_ratecardSerializer,City_ratecardSerializer,Outstation_ratecardSerializer,Company_airport_ratecardSerializer,Company_outstation_ratecardSerializer,Company_city_ratecardSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser,FormParser, MultiPartParser
from rest_framework.decorators import parser_classes


@parser_classes((MultiPartParser, ))
#----------------------- User --------------------

class UserList(APIView):
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

class UserDetail(APIView):
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

#----------------------- CATEGORY--------------------------
@parser_classes((MultiPartParser, ))
class CategoryList(APIView):
    """
    List all Category, or create a new Category.
    """


    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        thumbnail = request.FILES["picture"]
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        category = CategorySerializer(category)
        return Response(category.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#------------- statdered rate card ----------------------

    #------ Airport-------
class Airport_ratecardList(APIView):

    def get(self, request, format=None):
        airport_ratecard = Airport_ratecard.objects.all()
        serializer = Airport_ratecardSerializer(airport_ratecard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        for o in data:
            x= int(o['city'])
            try:
                airportprice = Airport_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']))
                print airportprice.id
            except Exception, e:
                serializer = Airport_ratecardSerializer(data=o)
                if serializer.is_valid():
                    print int(o['base_rate'])
                    serializer.save()
                #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        airport_ratecard = Airport_ratecard.objects.filter(city_id=x)
        serializer = Airport_ratecardSerializer(airport_ratecard, many=True)
        return Response(serializer.data)


    #------ Outstation-------
class Outstation_ratecardList(APIView):

    def get(self, request, format=None):
        outstation_ratecard = Outstation_ratecard.objects.all()
        serializer = Outstation_ratecardSerializer(outstation_ratecard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        for o in data:
            x= int(o['city'])
            print x
            try:
                outstationprice = Outstation_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']))
                print outstationprice.id
            except Exception, e:
                serializer = Outstation_ratecardSerializer(data=o)
                if serializer.is_valid():
                    serializer.save()
                #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        outstation_ratecard = Outstation_ratecard.objects.filter(city_id=x)
        serializer = Outstation_ratecardSerializer(outstation_ratecard, many=True)
        return Response(serializer.data)

    #------ City usage-------
class City_ratecardList(APIView):

    def get(self, request, format=None):
        city_ratecard = City_ratecard.objects.all()
        serializer = City_ratecardSerializer(city_ratecard, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        data = request.data
        for o in data:
            x= int(o['city'])
            try:
                cityprice = City_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']),slab_id=int(o['slab']))
                print x
            except Exception, e:
                serializer = City_ratecardSerializer(data=o)
                if serializer.is_valid():
                    serializer.save()

                #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        city_ratecard = City_ratecard.objects.filter(city_id=x)
        serializer = City_ratecardSerializer(city_ratecard, many=True)
        return Response(serializer.data)


#====================== Company Rate Card List ===========
    #------ Airport-------
class Company_airport_ratecardList(APIView):

    def get(self, request, format=None):
        airport_ratecard = Company_airport_ratecard.objects.all()
        serializer = Company_airport_ratecardSerializer(airport_ratecard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        for o in data:
            c= int(o['company'])
            x= int(o['city'])
            try:
                airportprice = Company_airport_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']))
                print airportprice.id
            except Exception, e:
                serializer = Company_airport_ratecardSerializer(data=o)
                if serializer.is_valid():
                    print int(o['base_rate'])
                    serializer.save()
                #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        airport_ratecard =Company_airport_ratecard.objects.filter(city_id=x,company_id=c)
        serializer = Company_airport_ratecardSerializer(airport_ratecard, many=True)
        return Response(serializer.data)

    #------ Outstation-------

class Company_outstation_ratecardList(APIView):

    def get(self, request, format=None):
        outstation_ratecard = Company_outstation_ratecard.objects.all()
        serializer = Company_outstation_ratecardSerializer(outstation_ratecard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        for o in data:
            x= int(o['city'])
            c= int(o['company'])
            print x
            try:
                outstationprice = Company_outstation_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']))
                print outstationprice.id
            except Exception, e:
                serializer = Company_outstation_ratecardSerializer(data=o)
                if serializer.is_valid():
                    serializer.save()
                #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        outstation_ratecard = Company_outstation_ratecard.objects.filter(city_id=x,company_id=c)
        serializer = Company_outstation_ratecardSerializer(outstation_ratecard, many=True)
        return Response(serializer.data)

    #------ City usage-------

class Company_city_ratecardList(APIView):

    def get(self, request, format=None):
        city_ratecard = Company_city_ratecard.objects.all()
        serializer = Company_city_ratecardSerializer(city_ratecard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        for o in data:
            c= int(o['company'])
            x= int(o['city'])
            try:
                cityprice = City_ratecard.objects.get(city=int(o['city']),category_id=int(o['category']),slab_id=int(o['slab']))
                print x
            except Exception, e:
                serializer = Company_city_ratecardSerializer(data=o)
                if serializer.is_valid():
                    serializer.save()

                #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        city_ratecard = Company_city_ratecard.objects.filter(city_id=x,company_id=c)
        serializer = Company_city_ratecardSerializer(city_ratecard, many=True)
        return Response(serializer.data)

