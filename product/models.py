from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField('Name' , max_length=100)
    description = models.TextField('Description' , blank=True)
    price = models.DecimalField('Price' , decimal_places=2 , max_digits=8)
    created = models.DateTimeField('Created' , default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('view-product', kwargs={'pk': self.pk})