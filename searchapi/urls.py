
from django.urls import path
from .views import Search
from .views import SearchVideo
urlpatterns = [
    path('images/' , Search , name='search'),
    path('video/' , SearchVideo , name='searchvideo')

]