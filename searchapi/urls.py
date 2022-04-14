from django.urls import path
from .views import Search
from .views import SearchVideo
from .views import ToursDataRender
from .views import GetEmployes
from .views import GetQuestions
from .views import GetFoods
from .views import GetDevolopers
from .views import GetCarousel
from .views import GetPhones
from .views import GetTheDrinks
from .views import GetTheDrinksById
urlpatterns = [
    path('images/' , Search , name='search'),
    path('video/' , SearchVideo , name='searchvideo'),
    path('tours/' , ToursDataRender , name='tours'),
    path('employes/' , GetEmployes , name='emplyes'),
    path('questions/' , GetQuestions , name='questions'),
    path('foods/' , GetFoods , name='foods'),
    path('devolopers/' , GetDevolopers , name='devolopers'),
    path('carousel/' , GetCarousel , name='carousel'),
    path('phones/' , GetPhones , name='phones'),
    path('drinks/' , GetTheDrinks , name='drinks'),
    path('drink/<int:id>' , GetTheDrinksById, name='drinks'),
]