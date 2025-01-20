from django.db import models
from django.contrib.auth.models import User
import uuid

class RelationshipDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()  

    def __str__(self):
        return f"Start date of relationship for {self.user.username}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    mood = models.CharField(max_length=100, blank=True, null=True)
    unique_code = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    partner = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username




