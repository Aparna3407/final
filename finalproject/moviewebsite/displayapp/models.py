from django.db import models



class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.DateField()
    img = models.ImageField(upload_to='gallery/')
    director = models.CharField(max_length=250)
    producer = models.CharField(max_length=250)
    cast = models.TextField()

    def __str__(self):
        return self.name

