from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.CharField(max_length=255)
    runtime = models.IntegerField()
    vote_average = models.IntegerField()
    poster = models.URLField()
    genres = models.CharField(max_length=255)


    def __int__(self):
        return self.title+","+self.user