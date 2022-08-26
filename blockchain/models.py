from django.db import models

class Blockchain(models.Model):
    user_id=models.IntegerField()
    nonce = models.CharField(max_length=50)
    data = models.CharField(max_length=100)
    prev_hash = models.CharField(max_length=100)
    time_stamp = models.TimeField()
    mined=models.BooleanField()
    

# Create your models here.
