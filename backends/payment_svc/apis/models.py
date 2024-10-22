from django.db import models

class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100)
