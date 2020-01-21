from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    hunt_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    votes = models.IntegerField(default=1)
    hunter = models.ForeignKey(User,on_delete= models.CASCADE)

    def summary(self):
        return self.body[:100]

    def short_date(self):
        return self.hunt_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
