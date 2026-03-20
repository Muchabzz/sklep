from django.db import models

<<<<<<< HEAD
class Product(models.Model):
=======
class products(models.Model):
>>>>>>> ee5f70b2a57eca1aaa111d23c83862cd244708a5
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
