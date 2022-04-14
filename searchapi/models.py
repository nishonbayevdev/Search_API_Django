from django.db import models
from django.db.models import Q
# Create your models here.
class DataImageStores(models.Model):
    title = models.CharField(max_length=128) 
    description = models.TextField()
    img = models.ImageField(upload_to = 'media/Images')
    dateTime = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Malumotlar'
class DataVideoStores(models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)
    video = models.FileField()
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Malumotlar'
class ToursData (models.Model) :
    picture = models.ImageField(upload_to ='media/Tours')
    name = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.TextField() 
    dateTime = models.DateTimeField(auto_now_add=True ,editable=True)
    location = models.CharField(max_length=128)
    class Meta:
        verbose_name_plural = 'Malumotlar'
    def __str__(self) -> str:
        return self.name

class Employes (models.Model):
    img = models.ImageField(upload_to='media/employes')
    name = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)
    hobby = models.TextField()
    facebook = models.URLField(max_length=1024,blank=False)
    instagram = models.URLField(max_length=1024,blank=False)
    linkedin = models.URLField(max_length=1024,blank=False)
    github = models.URLField(max_length=1024,blank=False)
    class Meta:
        verbose_name_plural = 'Ishchilar'
    def __str__(self) -> str:
        return self.name
class Questions(models.Model):
    title = models.CharField(blank=False , max_length=512)
    context = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)
    poll = models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Savollar'
class FoodCatagories(models.Model):
    catagory = models.CharField(max_length=128,blank=False)
    datetime = models.DateTimeField(auto_now=False , editable=True)
    def __str__(self) -> str:
        return self.catagory
    class Meta:
        verbose_name_plural = 'Ovqatlar katagoriyalari'
class Foods(models.Model):
    catagory = models.ForeignKey(FoodCatagories,related_name="main", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/foods')
    name = models.CharField(max_length=128 , blank=False)
    description = models.TextField(blank=False)
    isShow = models.BooleanField(default=False,blank=False)
    rate = models.PositiveSmallIntegerField(blank=False)

    def filterFoods():
        filterArr = []
        for food in Foods.objects.all():
            if food.isShow:
                filterArr.append(food)
        return filterArr

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = 'Ovqatlar'
class Devolopers(models.Model):
    job = models.CharField(max_length=128 , blank=False)
    hobby = models.TextField(blank=False)
    company = models.CharField(max_length=128 , blank=False)
    exprience = models.PositiveSmallIntegerField(blank=False)
    def __str__(self) -> str:
        return self.job
    class Meta:
        verbose_name_plural = 'Devolopers'
class Carousel(models.Model):
    image = models.ImageField(upload_to='media/carousel' , verbose_name='Rasm')
    name = models.CharField(max_length=128,blank=False,verbose_name='Ism')
    profesion = models.CharField(max_length=128 ,blank=False,verbose_name='Kasb' )
    description = models.TextField(blank=False,verbose_name='Tafsilot')
    isShow = models.BooleanField(default=False , verbose_name='Ko\'rsatish')
    def __str__(self) -> str:
        return self.name
    def toFilterShowWithIsShow():
        filterDatas = []
        for filterData in Carousel.objects.all():
            if filterData.isShow:
                filterDatas.append(filterData)
        return filterDatas
    class Meta:
        verbose_name_plural = 'Carousel'
class PhoneProduct(models.Model):
    price = models.DecimalField(max_digits=1000 , blank=False , decimal_places=2 , verbose_name="Telefon narxi")
    image = models.ImageField(upload_to='media/phone' , verbose_name="Rasm" )
    title = models.CharField(max_length=128 , blank=False , verbose_name="Nomi")
    published_at = models.DateField(auto_now_add=True, blank=True)
    amount = models.PositiveSmallIntegerField(default=1,editable=True, verbose_name="Soni" , blank=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Telfonlar'
class TheDrinks(models.Model):
    MADE_PLACE = (
        (0 , 'UZ'),
        (1 , 'RU'),
        (2 , 'US'),
        (3 , 'EN'),
        (4 , 'FR'),
    )
    title = models.CharField(max_length=128,verbose_name="Ichimlik nomi",blank=False)
    image = models.ImageField(upload_to='media/drinks' , verbose_name='Ichimlik rasmi')
    packageAt = models.DateField(blank = False, auto_now=True , editable=False)
    endAt = models.DateField(blank=False , verbose_name="Yaraqligigi")
    description = models.TextField(blank=False,verbose_name="Tarif")
    isPublish = models.BooleanField(default=False,verbose_name='Korsatish')
    volume = models.PositiveSmallIntegerField(blank=False, verbose_name="hajmi L da")
    price = models.DecimalField(decimal_places=2 , max_digits=1000 , verbose_name="Narxi")
    madePlace = models.PositiveSmallIntegerField(choices=MADE_PLACE , blank=False , verbose_name="Ishlab chiqarilgan davlat")
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = "Ichimliklar"
    def SearchId(id : int) :
        return TheDrinks.objects.get(id=id)
    def Search(key : str) :
        return TheDrinks.objects.filter(Q(title__icontains = key ) | Q(packageAt__icontains = key ) | Q(endAt__icontains = key) | Q(description__icontains = key) | Q(madePlace__icontains = key) | Q(price__icontains = key)).filter(isPublish=True)