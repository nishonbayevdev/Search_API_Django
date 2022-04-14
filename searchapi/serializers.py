from .models import DataImageStores
from .models import DataVideoStores
from .models import ToursData
from .models import Employes
from .models import Questions
from .models import Foods
from .models import FoodCatagories
from .models import Devolopers
from .models import Carousel
from .models import PhoneProduct
from .models import TheDrinks
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
class catagoryData(serializers.ModelSerializer):
    class Meta :
        model = FoodCatagories
        fields = "__all__"
class SerializerDataFoods(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id' , 'image' , 'name' , 'description' , 'rate' , 'catagory']
class SerializerDataDevolopers(serializers.ModelSerializer):
    class Meta:
        model = Devolopers
        fields = "__all__"
class SerializerDataCarousel(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = fields = ['id' , 'image' , 'name' , 'profesion' , 'description' ,]
class SerializerDataPhoneProduct(serializers.ModelSerializer):
    class Meta:
        model = PhoneProduct
        fields = "__all__"
class SerializerDataTheDrinks(serializers.ModelSerializer):
    class Meta:
        model = TheDrinks
        fields = "__all__"
