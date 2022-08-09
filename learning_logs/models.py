from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text=models.CharField(max_length=200)
    data_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    public=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text

class Entry(models.Model):
    '''The specific knowledge about certain project/topic'''
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    data_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Entries'
    
    def __str__(self) -> str:
        if len(self.text)>50:
            return f'{self.text[:50]}...'
        else:
            return f'{self.text}'