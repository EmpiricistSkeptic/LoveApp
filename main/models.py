from django.db import models
from django.contrib.auth.models import User

class RelationshipDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()  

    def __str__(self):
        return f"Start date of relationship for {self.user.username}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='pictures/')
    bio = models.TextField(blank=True, null=True)
    mood = models.CharField(max_length=40, blank=True, null=True)




