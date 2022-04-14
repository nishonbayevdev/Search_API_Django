from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import SerializerDataImg 
from .serializers import SerializerDataVideo
from .serializers import SerializerDataTours
from .serializers import SerializerDataEmployes
from .serializers import SerializerDataQuestions
from .serializers import SerializerDataFoods
from .serializers import catagoryData
from .serializers import SerializerDataDevolopers
from .serializers import SerializerDataCarousel
from .serializers import SerializerDataPhoneProduct
from .serializers import SerializerDataTheDrinks
from .models import Carousel, DataImageStores
from .models import Foods
from .models import Questions
from .models import Employes
from .models import DataVideoStores
from .models import ToursData
from .models import FoodCatagories
from .models import Devolopers
from .models import Carousel
from .models import PhoneProduct
from .models import TheDrinks
# Create your views here.
@api_view(['GET'])
def Search(request):
    if request.method == 'GET':
        try:
            key = request.GET['query']
            token = request.GET['token']
            if key is not None and token == 'adasdlasmdlksa5a1d5s1d51d21cs21csd0c2':
                data : list = []
                source = DataImageStores.objects.all()
                data = SearchFunc(key , source)
                if len(data) >= 1 :
                    serializer = SerializerDataImg(data , many = True)
                    return Response(serializer.data,status=200)
                else :
                    return Response([])
            else:
                error = {'error':'Error'}
                return Response(error,status=400)
        except:
                return Response({'error':'404'},status=404)

@api_view(['GET'])
def SearchVideo(request):
    if request.method == 'GET':
        try:
            key = request.GET['query']
            token = request.GET['token']
            if key is not None and token == 'adasdlasmdlksa5a1d5s1d51d21cs21csd0c2':
                data : list = []
                source = DataVideoStores.objects.all()
                data = SearchFunc(key , source)
                if len(data) >= 1 :
                    serializer = SerializerDataVideo(data , many = True)
                    return Response(serializer.data,status=200)
                else :
                    notFound =  {
                        'NotFound':'We have\'nt found'
                    }
                    return Response(notFound)
            else:
                error = {'error':'Error'}
                return Response(error,status=400)
        except: 
            return Response({'error':'404'},status=404)
def SearchFunc(key : str , data : list) -> list:
    newData = []
    for obj in data:
        if obj.title.lower().count(key.lower()) >= 1:
            newData.append(obj)
    return newData


# madel Tours
@api_view(['GET'])
def ToursDataRender(request):
    Tours = ToursData.objects.all()
    serializer = SerializerDataTours(Tours , many = True)
    return Response(serializer.data,status=200)


@api_view(['GET'])
def GetEmployes(request):
    employes = Employes.objects.all()
    serializer = SerializerDataEmployes(employes , many = True)
    if serializer.data is not []:
        return Response(serializer.data,status=200)
    else:
        return Response([])
@api_view(['GET'])
def GetQuestions(request):
    questions = Questions.objects.all()
    serializer = SerializerDataQuestions(questions , many = True)
    if serializer is not []:
        return Response(serializer.data , status=200)
    else :
        return Response([])
@api_view(['GET'])
def GetFoods(request):
    foods = Foods.filterFoods()
    serializer = SerializerDataFoods(foods , many = True)
    catagoty = FoodCatagories.objects.all()
    serializerCat = catagoryData(catagoty , many = True)
    newData = []
    for food in serializer.data:
        newFood = dict(food)
        index = newFood['catagory']
        for cata in serializerCat.data:
            if cata['id'] == index:
                newFood['catagory'] = dict(cata)
                newData.append(newFood)

    if serializer is not []:
        return Response(newData, status=200)
    else :
        return Response([])
@api_view(['GET'])
def GetDevolopers(request):
    devolopers = Devolopers.objects.all()
    serializer = SerializerDataDevolopers(devolopers , many=True)
    if serializer.data is not []:
        return Response(serializer.data , status=200)
    return Response([])
@api_view(['GET'])
def GetCarousel(request):
    carousel = Carousel.toFilterShowWithIsShow()
    serializer = SerializerDataCarousel(carousel , many=True)
    if serializer.data is not []:
        return Response(serializer.data , status=200)
    return Response([])
@api_view(["GET"])
def GetPhones(request):
    phone = PhoneProduct.objects.all()
    serializer = SerializerDataPhoneProduct(phone,many=True)
    if serializer.data is not []:
        return Response(serializer.data , status = 200)
    else:
        return Response([])
@api_view(["GET"])
def GetTheDrinks(request) :
    key = request.GET.get('q')
    if key != "" and key is not None:
        drinks = TheDrinks.Search(key)
        serializer = SerializerDataTheDrinks(drinks , many=True)
        return Response(serializer.data)
    else:
        return Response([])
@api_view(["GET"])
def GetTheDrinksById(request , id):
    try :
        drink = TheDrinks.SearchId(id)
        serializer = SerializerDataTheDrinks(drink)
        return Response(serializer.data)
    except TheDrinks.DoesNotExist:
        return Response([]);

