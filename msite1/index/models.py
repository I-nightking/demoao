from django.db import models

# Create your models here.

class AndroidTitle(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class AndroidSubtitle(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    androidTitle = models.ForeignKey('AndroidTitle',on_delete=models.CASCADE,related_name='modeltitle')
    def __str__(self):
        return self.title

class AndroidFile(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    indexFile = models.FileField(upload_to='file')
    androidSubtitle = models.ForeignKey('AndroidSubtitle', on_delete=models.CASCADE,related_name='modelfile')
    def __str__(self):
        return self.title

class AndroidText(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    text_content = models.TextField()
    androidSubtitle = models.ForeignKey('AndroidSubtitle', on_delete=models.CASCADE,related_name='modeltext')
    def __str__(self):
        return self.title

