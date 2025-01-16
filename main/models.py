from django.db import models
from django.contrib.auth.models import User

class RelationshipDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()  

    def __str__(self):
        return f"Start date of relationship for {self.user.username}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='pictures/')



