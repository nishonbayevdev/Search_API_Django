from django.db import models

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