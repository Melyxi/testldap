from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Playbook(models.Model):
    name = models.CharField(max_length=100)
    image_product = models.ImageField(upload_to="image_product", blank=True, validators =[FileExtensionValidator(allowed_extensions=['jpg'])])
    create_at = models.DateTimeField(auto_now_add=True)
