from .models import DataImageStores
from .models import DataVideoStores
from rest_framework import serializers
class SerializerDataImg(serializers.ModelSerializer):
    class Meta:
        model = DataImageStores
        fields = ['id','title','description','img','dateTime',]
class SerializerDataVideo(serializers.ModelSerializer):
    class Meta:
        model = DataVideoStores
        fields = ['id','title','description','video','dateTime',]