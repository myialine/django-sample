from django.db import models
class Machine(models.Model):
    STATUS = [('Y', 'Active'), ('N', 'Not Active')]
    name = models.CharField(max_length=100)
    current_status = models.CharField(max_length=1, choices=STATUS, default='N')


