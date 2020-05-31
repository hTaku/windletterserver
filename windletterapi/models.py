from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=64)
    divice_id = models.CharField(max_length=64,blank=True)
    divice_position = models.CharField(max_length=64,blank=True)
    send_message_text = models.CharField(max_length=256,blank=True)
    receive_message_text = models.CharField(max_length=256,blank=True)
    trajectory_id = models.CharField(max_length=64,blank=True)
    send_time = models.CharField(max_length=10,blank=True)
    
class Trajectory(models.Model):
    send_position = models.CharField(max_length=64,blank=True)
    receive_position = models.CharField(max_length=64,blank=True)
    trajectory = models.CharField(max_length=255,blank=True)
    trajectory_id = models.CharField(max_length=64,blank=True)