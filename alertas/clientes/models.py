from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=200,blank=True,null=True)
	contacto = models.EmailField(max_length=200,blank=True,null=True)