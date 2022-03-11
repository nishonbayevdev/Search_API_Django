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
