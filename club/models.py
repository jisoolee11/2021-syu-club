from django.db import models
from accounts.models import CustomUser

class ClubType(models.Model):
    club_type_name = models.CharField(max_length=200)
    club_type_desc = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.club_type_name


class Club(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='owner')
    club_type = models.ForeignKey(ClubType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
