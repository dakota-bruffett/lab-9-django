from django.db import models

# Create your models here.
class Place(models.Model):
    user = models.ForeignKey('auth.User',null=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited =models.DateTimeField(blank=True, null=True)


    #heres where the models are made.

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'
        return f'{self.pk}: {self.name} Visited {self.visited} on {self.date_visited} '