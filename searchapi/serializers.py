from .models import DataImageStores
from .models import DataVideoStores
from .models import ToursData
from .models import Employes
from .models import Questions
from rest_framework import serializers
class SerializerDataImg(serializers.ModelSerializer):
    class Meta:
        model = DataImageStores
        fields = ['id','title','description','img','dateTime',]
class SerializerDataVideo(serializers.ModelSerializer):
    class Meta:
        model = DataVideoStores
        fields = ['id','title','description','video','dateTime',]
class SerializerDataTours (serializers.ModelSerializer):
    class Meta:
        model = ToursData
        fields = ['id' , 'picture' , 'name' , 'price' , 'description' , 'dateTime' , 'location' ,]
class SerializerDataEmployes(serializers.ModelSerializer):
    class Meta:
        model = Employes
        fields = ['id' , 'img' , 'name' , 'profession' , 'hobby' , 'facebook' , 'instagram' , 'linkedin' , 'github' ,]
class SerializerDataQuestions(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id' , 'title' , 'context' , 'date' , 'poll' ,]
