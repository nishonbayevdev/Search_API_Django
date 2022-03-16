from django.urls import path
from .views import Search
from .views import SearchVideo
from .views import ToursDataRender
from .views import GetEmployes
from .views import GetQuestions
urlpatterns = [
    path('images/' , Search , name='search'),
    path('video/' , SearchVideo , name='searchvideo'),
    path('tours/' , ToursDataRender , name='tours'),
    path('employes/' , GetEmployes , name='emplyes'),
    path('questions/' , GetQuestions , name='questions')
]