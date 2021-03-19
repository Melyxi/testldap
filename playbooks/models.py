from django.db import models

# Create your models here.
class Playbook(models.Model):
    name = models.CharField(max_length=100)
    image_product = models.ImageField(upload_to="image_product", blank=True)

