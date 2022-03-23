from pickle import TRUE
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_profile = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)


    def __str__(self):
        return self.title