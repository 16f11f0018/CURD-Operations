from django.db import models

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=40,null=True,blank=False)
    description=models.TextField(max_length=40,null=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)