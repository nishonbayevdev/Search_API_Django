from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import SerializerDataImg , SerializerDataVideo
from .models import DataImageStores, DataVideoStores
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
                    notFound =  {
                        'NotFound':'We have\'nt found'
                    }
                    return Response(notFound)
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